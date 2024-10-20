"""
Using Fernet to generate a random key.
Using argparse to optionally choosing save-file name.
 """
import argparse
from cryptography.fernet import Fernet

def key_gen(*args):
    """Generate a key with Fernet and saves it to a file"""
    key = Fernet.generate_key()

    with open(f"{args[0]}.key", "wb") as key_file:
        key_file.write(key)
    print('---------------------------------')
    print(f"Key saved as: {args[0]}.key")
    print(f"Key: {key.decode()}\n")

parser = argparse.ArgumentParser(description="Key Generator")
parser.add_argument("-s", "--save", action="store_true", help="optional to change savefile-name")
arg = parser.parse_args()

if arg.save:
    save_file = input("Choose a name for the file: ")
    key_gen(save_file)
else:
    key_gen("default")
