"""
comments for modules.
"""
import argparse
import cryptotool
import kg
from scan import _scan, _scan_os

def cli():
    """Function for running the argparse commands"""
    parser = argparse.ArgumentParser(description="---Toolbox---")

    subparser = parser.add_subparsers(dest="tool")
    nmap_parser = subparser.add_parser("nmap", help="'nmap -h' for more information")
    crypto_parser = subparser.add_parser("crypto", help="'crypto -h' for more information")

    nmap_parser.add_argument("target", nargs='?', help="To scan multiple ip's use -m")
    nmap_parser.add_argument("-m", "--multiple", nargs=1, help="Scan a list of ip's in a file")
    nmap_parser.add_argument("-s", "--save", help="Used to save nmap output to file")
    nmap_parser_group = nmap_parser.add_mutually_exclusive_group()
    nmap_parser_group.add_argument("-os", action="store_true", help="Used to scan for os")
    nmap_parser_group.add_argument("-c", "--custom", help="Enter custom flags(e.g '-sV -Pn -p')")

    crypto_parser.add_argument("-s", "--save", help="Used with decryption to save output to file")
    crypto_parser_group = crypto_parser.add_mutually_exclusive_group()
    crypto_parser_group.add_argument(
        "-d",
        "--decryption",
        nargs=2,
        help="For Decryption add File and Key")

    crypto_parser_group.add_argument(
        "-e",
        "--encryption",
        nargs=2,
        help="For Encryption add File and Key")

    crypto_parser_group.add_argument(
        "-g",
        "--generatekey",
        nargs='?',
        const='default',
        help="Optional, enter a name for key-file")

    args = parser.parse_args()

    return args

def crypto(args):
    """Taking argparse input and calls the correct function"""
    if args.generatekey:
        kg.key_gen(args.generatekey)
    elif args.decryption:
        try:
            file = args.decryption[0]
            key = args.decryption[1]
            if args.save:
                cryptotool.decrypt(file, key, args.save)
            else:
                cryptotool.decrypt(file, key)
        except FileNotFoundError as e:
            print(e)
    elif args.encryption:
        try:
            file = args.encryption[0]
            key = args.encryption[1]
            cryptotool.encrypt(file, key)
        except FileNotFoundError as e:
            print(e)

def nmap(args):
    """Taking argparse input and calls the correct function"""
    targets = []
    save_file = []

    if args.target:
        targets.append(args.target)

    if args.save:
        save_file = args.save

    if args.multiple:
        try:
            with open(args.multiple[0], 'r') as ip_file:
                targets = ip_file.read().splitlines()
        except FileNotFoundError as e:
            print(e)

    if args.os:
        _scan_os(targets, save_file)
    elif args.custom:
        print(args.custom)
        _scan(targets, save_file, args.custom)
    else:
        _scan(targets, save_file)

def main():
    """Mainscript for running the toolbox"""
    args = cli()

    if args.tool == "crypto":
        crypto(args)

    if args.tool == "nmap":
        nmap(args)

if __name__ == "__main__":
    main()
