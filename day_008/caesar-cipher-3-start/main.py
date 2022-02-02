alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(input_text, shift_amount, cipher_direction):
    output_text = ""
    code_direction = "encoded"
    if cipher_direction.lower().startswith("d"):
        shift_amount *= -1
        code_direction = "decoded"
    for letter in input_text:
        position = alphabet.index(letter)
        new_position = (position + shift_amount) % 26
        output_text += alphabet[new_position]
    print(f"The {code_direction} text is {output_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text, shift, direction)
