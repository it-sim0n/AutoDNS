from pathlib import Path
from threading import Thread
from .utils import run, spinner


def resolve(domain, path, resolvers, dynamic=False):
    if dynamic:
        dnsgen = run(["dnsgen", path])
        p = run(
            ["puredns", "resolve", "/dev/stdin", domain, "-r", resolvers],
            stdin=dnsgen.stdout
        )
        msg = "dnsgen | puredns resolve is running"
    else:
        p = run(
            ["puredns", "resolve", path, domain, "-r", resolvers]
        )
        msg = "puredns resolve is running"

    return p, msg

def bruteforce(domain, wordlist, resolvers):
    p = run(
        ["puredns", "bruteforce", wordlist, domain, "-r", resolvers]
    )
    msg = "puredns bruteforce is running"
    return p, msg

def collect_results(proc, msg, outfile):
    t = Thread(target=spinner, args=(proc, msg))
    t.start()

    results = sorted(set(proc.stdout.read().splitlines()))
    proc.wait()
    t.join()

    Path(outfile).write_text("\n".join(results) + "\n")
