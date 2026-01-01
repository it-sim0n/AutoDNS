from pathlib import Path
from threading import Thread
from .utils import run, spinner
from .resolvers import create_resolvers_file

def resolve(domain, sublist, dynamic=False):
    """
    Resolve subdomains using puredns.
    If dynamic=True, dnsgen is used to generate subdomains.
    """
    resolvers = create_resolvers_file()
    tmp = None

    if dynamic:
        tmp = Path("/tmp/autodns_dnsgen.txt")
        # dnsgen output to tmp file
        dnsgen_proc = run(["dnsgen", sublist, "-f", "-", ])
        with tmp.open("w") as f:
            f.write(dnsgen_proc.stdout.read())
        dnsgen_proc.wait()
        input_file = tmp
        msg = "dnsgen | puredns resolve running"
    else:
        input_file = sublist
        msg = "puredns resolve running"

    p = run(["puredns", "resolve", str(input_file), domain, "-r", str(resolvers)])
    return p, msg, tmp  # tmp is returned to delete later

def bruteforce(domain, wordlist):
    """
    Bruteforce subdomains using puredns.
    """
    resolvers = create_resolvers_file()
    p = run(["puredns", "bruteforce", wordlist, domain, "-r", str(resolvers)])
    msg = "puredns bruteforce running"
    return p, msg

def collect_results(proc, msg, outfile, tmp=None):
    """
    Collect output from a puredns process and save to file.
    Optionally delete temporary dnsgen file.
    """
    t = Thread(target=spinner, args=(proc, msg))
    t.start()

    results = sorted(set(proc.stdout.read().splitlines()))
    proc.wait()
    t.join()

    Path(outfile).write_text("\n".join(results) + "\n")

    if tmp and tmp.exists():
        tmp.unlink()
