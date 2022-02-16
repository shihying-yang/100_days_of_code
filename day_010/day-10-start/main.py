# Already used functions with outputs
# length = len(format_name("John", "Doe"))


# Function with Outputs


def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    name = f"{f_name.title()} {l_name.title()}"
    return f"Result: {name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))
