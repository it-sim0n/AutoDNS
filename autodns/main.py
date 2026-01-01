from .banner import show_banner
from .resolvers import create_resolvers_file
from .runner import resolve, bruteforce, collect_results

def main():
    show_banner()
    resolvers = create_resolvers_file()

    print("Please select the action you want to perform:")
    print("1) Resolve subdomains from an existing list")
    print("2) Bruteforce subdomains using a wordlist")
    action = input("> ").strip()

    domain = input("Please enter the target domain: ").strip()
    out = f"{domain}_pure.txt"

    if action == "1":
        path = input("Please provide the path to the subdomain list file: ").strip()
        print("Please specify the input type you want to use:")
        print("1) Use a plain subdomain list")
        print("2) Generate permutations dynamically using dnsgen")
        itype = input("> ").strip()
        p, msg = resolve(domain, path, resolvers, dynamic=(itype == "2"))

    elif action == "2":
        wl = input("Please provide the path to the wordlist file: ").strip()
        p, msg = bruteforce(domain, wl, resolvers)

    else:
        raise SystemExit("Invalid action selected.")

    collect_results(p, msg, out)
    print(f"[+] Results have been saved to: {out}")

