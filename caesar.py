import argparse

PLAIN_TEXT_WHEEL = "abcdefghijklmnopqrstuvwxyz"


def parse_args():
    parser = argparse.ArgumentParser(description="Caesar Cipher")
    parser.add_argument(
        "operation",
        choices=["encrypt", "decrypt", "crack"],
        help="encrypt, decrypt or crack cipher",
    )
    parser.add_argument("--offset", type=int, default=0, help="initial cipher offset")
    parser.add_argument(
        "--shift", type=int, default=0, help="continuously shift cipher"
    )
    return parser.parse_args()


def encrypt(offset, shift, plain_text):
    # Initialize cipher wheel. E.g. "xyzabcdefghijklmnopqrstuvw"
    cipher_text_wheel = PLAIN_TEXT_WHEEL[-offset:] + PLAIN_TEXT_WHEEL[:-offset]

    # Capitalize plain text
    plain_text = plain_text.lower()

    cipher_text = ""
    for character in plain_text:
        if character in PLAIN_TEXT_WHEEL:
            # Transform plain text into cipher
            index = PLAIN_TEXT_WHEEL.index(character)
            character = cipher_text_wheel[index]

            # Rotate cipher to the right
            cipher_text_wheel = cipher_text_wheel[-shift:] + cipher_text_wheel[:-shift]

        # Append character to cipher text
        cipher_text += character

    return cipher_text


def decrypt(offset, shift, cipher_text):
    # Decryption is the reverse of encryption
    return encrypt(-offset, -shift, cipher_text)


def crack(cipher_text):
    num_possibilities = len(PLAIN_TEXT_WHEEL)

    # Try all possible cipher offsets and shifts
    for offset in range(num_possibilities):
        for shift in range(num_possibilities):
            plain_text = decrypt(offset, shift, cipher_text)

            # We assume that it starts with flag
            if plain_text.startswith("flag"):
                return plain_text

    return "Failed to crack!"


def main():
    args = parse_args()

    input_text = input()

    if args.operation == "encrypt":
        output_text = encrypt(args.offset, args.shift, input_text)
    elif args.operation == "decrypt":
        output_text = decrypt(args.offset, args.shift, input_text)
    else:  # args.operation == "crack"
        output_text = crack(input_text)

    print(output_text)


if __name__ == "__main__":
    main()
