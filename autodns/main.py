from .banner import show_banner
from .runner import resolve, bruteforce, collect_results


def main():
    show_banner()

    print("Please select the action you want to perform:")
    print("1) Resolve subdomains from an existing list")
    print("2) Bruteforce subdomains using a wordlist")
    action = input("> ").strip()

    domain = input("Please enter the target domain: ").strip()
    outfile = f"{domain}_pure.txt"

    if action == "1":
        sublist = input("Please provide the path to the subdomain list file: ").strip()

        print("Please specify the input type you want to use:")
        print("1) Use a plain subdomain list")
        print("2) Generate permutations dynamically using dnsgen")
        itype = input("> ").strip()

        proc, msg, tmp = resolve(
            domain=domain,
            sublist=sublist,
            dynamic=(itype == "2")
        )

        collect_results(proc, msg, outfile, tmp)

    elif action == "2":
        wordlist = input("Please provide the path to the wordlist file: ").strip()

        proc, msg = bruteforce(domain, wordlist)
        collect_results(proc, msg, outfile)

    else:
        raise SystemExit("Invalid action selected.")

    print(f"[+] Results have been saved to: {outfile}")
