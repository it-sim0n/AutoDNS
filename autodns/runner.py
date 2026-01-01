from pathlib import Path
from threading import Thread
import subprocess

from .utils import spinner
from .resolvers import create_resolvers_file


def resolve(domain, sublist, dynamic=False):
    """
    Static:
      puredns resolve sublist domain -r resolvers

    Dynamic (EXACT bash behavior):
      puredns resolve "$(cat sublist | dnsgen -f - > tmp; echo tmp)" domain -r resolvers
    """
    resolvers = create_resolvers_file()
    tmp = None

    if dynamic:
        tmp = Path("/tmp/autodns_dnsgen.txt")

        cmd = (
            f'puredns resolve "$(cat {sublist} | dnsgen -f - > {tmp}; echo {tmp})" '
            f'{domain} -r {resolvers}'
        )

        proc = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )

        msg = "dnsgen | puredns resolve running"
        return proc, msg, tmp

    # -------- static mode --------
    proc = subprocess.Popen(
        ["puredns", "resolve", sublist, domain, "-r", str(resolvers)],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    msg = "puredns resolve running"
    return proc, msg, None


def bruteforce(domain, wordlist):
    """
    puredns bruteforce wordlist domain -r resolvers
    """
    resolvers = create_resolvers_file()

    proc = subprocess.Popen(
        ["puredns", "bruteforce", wordlist, domain, "-r", str(resolvers)],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True
    )

    msg = "puredns bruteforce running"
    return proc, msg


def collect_results(proc, msg, outfile, tmp=None):
    t = Thread(target=spinner, args=(proc, msg))
    t.start()

    results = sorted(set(proc.stdout.read().splitlines()))
    proc.wait()
    t.join()

    Path(outfile).write_text("\n".join(results) + "\n")

    if tmp and tmp.exists():
        tmp.unlink()
