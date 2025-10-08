import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Caesar Cipher")
    parser.add_argument(
        "operation", choices=["encrypt", "decrypt"], help="encrypt or decrypt text"
    )
    parser.add_argument("--offset", type=int, help="initial cipher offset")
    parser.add_argument("--shift", type=int, help="continuously shift cipher N times")
    parser.add_argument("--input-file", type=str, help="input file (default: stdin)")
    parser.add_argument("--output-file", type=str, help="output file (default: stdout)")
    return parser.parse_args()


def encrypt(offset, shift, input_file, output_file):
    # Initialize plain wheel
    plaintext_wheel = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Initialize cipher wheel
    # E.g. "XYZABCDEFGHIJKLMNOPQRSTUVW"
    cipher_wheel = plaintext_wheel[-offset:] + plaintext_wheel[:-offset]

    # Read and capitalize input plain text
    plaintext = input_file.read().upper()

    for character in plaintext:
        if character in plaintext_wheel:
            # Transform plain text into cipher
            index = plaintext_wheel.index(character)
            character = cipher_wheel[index]

        # Write character to cipher text
        output_file.write(character)

        # Rotate cipher to the right
        cipher_wheel = cipher_wheel[-shift:] + cipher_wheel[:-shift]


def decrypt(offset, shift, input_file, output_file):
    # Decryption is done in reverse
    encrypt(-offset, -shift, input_file, output_file)


def main():
    args = parse_args()

    # Open input / output file (or stdin / stdout)
    input_file = open(args.input_file, "rt") if args.input_file else sys.stdin
    output_file = open(args.output_file, "wt") if args.output_file else sys.stdout

    if args.operation == "encrypt":
        encrypt(args.offset, args.shift, input_file, output_file)
    else:
        decrypt(args.offset, args.shift, input_file, output_file)

    input_file.close()
    output_file.close()


if __name__ == "__main__":
    main()
