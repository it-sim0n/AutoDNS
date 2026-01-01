from autodns.core import bruteforce, resolve, wait_with_spinner
from pathlib import Path


def main():
    print_banner()

    choice = input("> ").strip()
    domain = input("Please enter the target domain: ").strip()
    resolvers = Path.home() / ".resolvers"

    if choice == "1":
        path = input("Please provide the path to the subdomain list: ").strip()
        outfile = f"{domain}_resolved.txt"

        p, msg = resolve(domain, path, resolvers)
        wait_with_spinner(p, msg)

        Path(outfile).write_text(p.stdout.read())
        print(f"[+] Results have been saved to: {outfile}")

    elif choice == "2":
        wl = input("Please provide the path to the wordlist file: ").strip()
        outfile = f"{domain}_pure.txt"

        p, msg = bruteforce(domain, wl, resolvers, outfile)
        wait_with_spinner(p, msg)

        print(f"[+] Results have been saved to: {outfile}")
