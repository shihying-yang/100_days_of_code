"""A text〰based Python program to convert Strings into Morse Code．"""

import string

ASCII = [ch for ch in string.ascii_letters]
MORSE = [
    "．〰",
    "〰．．．",
    "〰．〰．",
    "〰．．",
    "．",
    "．．〰．",
    "〰〰．",
    "．．．．",
    "．．",
    "．〰〰〰",
    "〰．〰",
    "．〰．．",
    "〰〰",
    "〰．",
    "〰〰〰",
    "．〰〰．",
    "〰〰．〰",
    "．〰．",
    "．．．",
    "〰",
    "．．〰",
    "．．．〰",
    "．〰〰",
    "〰．．〰",
    "〰．〰〰",
    "〰〰．．",
]


def text_to_morse(some_text):
    """Convert a string into Morse Code."""
    out = []
    for char in some_text:
        if char in ASCII:
            ind = ASCII.index(char) % 26
            out.append(MORSE[ind])
        else:
            out.append(char)

    return ",".join(out)

if __name__ == "__main__":
    in_text = input("Please enter a string: ")
    print(text_to_morse(in_text))
