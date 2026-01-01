from pathlib import Path
from threading import Thread
from .utils import run, spinner


def resolve(domain, path, resolvers):
    p = run([
        "puredns", "resolve",
        path, domain,
        "-r", resolvers
    ])
    msg = "puredns resolve is running"
    return p, msg


def bruteforce(domain, wordlist, resolvers, outfile):
    p = run([
        "puredns", "bruteforce",
        wordlist, domain,
        "-r", resolvers,
        "--wildcard-tests", "5",
        "--rate-limit", "1000",
        "-w", outfile
    ])
    msg = "puredns bruteforce is running"
    return p, msg


def wait_with_spinner(proc, msg):
    t = Thread(target=spinner, args=(proc, msg))
    t.start()
    proc.wait()
    t.join()
