# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# TODO1: create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    starting_letter_content = starting_letter.read()
# print(type(starting_letter_content))

# TODO2: find all the names in invited_names.txt
with open("Input/Names/invited_names.txt", "r") as invited_names:
    names = invited_names.readlines()
# print(names)

# TODO3: Replace the [name] placeholder with the actual name.
for name in names:
    # print(starting_letter_content.replace("[name]", name.strip()))
    new_content = starting_letter_content.replace("[name]", name.strip())
    with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", "w", newline="\n") as new_letter:
        new_letter.write(new_content)
