import json
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
    new_data = {web_name.lower(): {"email": email, "password": password}}

    if web_name == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please fill all the fields!")
    else:
        to_save = messagebox.askokcancel(
            title=web_name,
            message=f"These are the details:\nEmail: {email}\nPassword: {password}\nIs it OK to save?",
        )

        if to_save:
            try:
                with open("data.json", "r") as f_in:
                    # Reading old data
                    data = json.load(f_in)
                    # Update old data with new data (but consider the case when the website already exists)
                    if data.get(web_name.lower()) is not None:
                        exist_site = messagebox.askokcancel(
                            title="Warning", message="Website already exists!\nDo you want to overwrite?"
                        )
                        if exist_site:
                            data.update(new_data)
                    else:
                        data.update(new_data)

            except FileNotFoundError:
                data = new_data
            except json.decoder.JSONDecodeError:
                data = new_data
            finally:
                with open("data.json", "w") as f_out:
                    # saving updated data
                    json.dump(data, f_out, indent=4)

            ent_website.delete(0, tk.END)
            ent_password.delete(0, tk.END)
            pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_action():
    """search password from data file"""
    web_name = ent_website.get()

    try:
        with open("data.json", "r") as f_in:
            data = json.load(f_in)
    except FileNotFoundError:
        messagebox.showwarning(title="File Missing", message="No Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showwarning(title="Data Missing", message="No Data in the Data File")
    else:
        if web_name.lower() in data:
            email = data[web_name.lower].get("email")
            password = data[web_name.lower].get("password")
            messagebox.showinfo(title=web_name, message=f"Email: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showwarning(title="Website Missing", message=f"No Website with name {web_name} found")


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
ent_website.grid(column=1, row=1, sticky="EW")
ent_website.focus()

btn_search = tk.Button(text="Search", command=search_action)
btn_search.grid(column=2, row=1, sticky="EW")

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
