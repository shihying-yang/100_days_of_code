import random
import string
import tkinter as tk
from tkinter import messagebox

import pyperclip

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = random.randint(8, 10)
nr_numbers = random.randint(2, 4)
nr_symbols = random.randint(2, 4)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    """generate a random password"""
    password = [random.choice(letters) for _ in range(nr_letters)]
    password.extend([random.choice(numbers) for _ in range(nr_numbers)])
    password.extend([random.choice(symbols) for _ in range(nr_symbols)])
    random.shuffle(password)
    new_password = "".join(password)
    ent_password.delete(0, tk.END)
    ent_password.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_action():
    """save password to a text file, and copy the password to the clipboard"""
    web_name = ent_website.get()
    email = ent_email.get()
    password = ent_password.get()

    if web_name == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please fill all the fields!")
    else:
        to_save = messagebox.askokcancel(
            title=web_name,
            message=f"These are the details:\nEmail: {email}\nPassword: {password}\nIs it OK to save?",
        )

        if to_save:
            with open("data.md", "a") as f_out:
                f_out.write(f"| {web_name} | {email} | {password} |\n")
                ent_website.delete(0, tk.END)
                ent_password.delete(0, tk.END)
            pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website row
lbl_website = tk.Label(text="Website:")
lbl_website.grid(column=0, row=1)

ent_website = tk.Entry()
ent_website.grid(column=1, row=1, columnspan=2, sticky="EW")
ent_website.focus()

# email/username row
lbl_email = tk.Label(text="Email/Username:")
lbl_email.grid(column=0, row=2)

ent_email = tk.Entry()
ent_email.grid(column=1, row=2, columnspan=2, sticky="EW")
ent_email.insert(0, "ysying888@gmail.com")

# password row
lbl_password = tk.Label(text="Password:")
lbl_password.grid(column=0, row=3)

ent_password = tk.Entry()
ent_password.grid(column=1, row=3, sticky="EW")

btn_password = tk.Button(text="Generate Password", command=create_password)
btn_password.grid(column=2, row=3)

# add to file row
btn_add = tk.Button(text="Add", command=save_action)
btn_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
