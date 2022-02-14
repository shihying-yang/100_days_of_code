# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Button
def button_clicked():
    """[summary]"""
    # print("I got clicked")
    # my_label["text"] = "I got clicked"
    # my_label.config(text="I got clicked")
    content = my_input.get()
    # print(content)
    if content:
        my_label.config(text=content)
    else:
        my_label.config(text="I got clicked")


# label
my_label = Label(text="I Am a Label", font=("Arial", 24))
# my_label["text"] = "I have changed"
# my_label.config(text="I have changed again")

# my_label.pack()
# my_label.pack(side="left")
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
my_button = Button(text="click me", command=button_clicked)
# my_button.pack()
my_button.grid(column=1, row=1)

new_button = Button(text="new Button")
new_button.grid(column=2, row=0)

# Entry

my_input = Entry(width=10)
# my_input.pack()
# my_input.grid(column=2, row=2)
my_input.grid(column=3, row=2)

# print(my_input.get())

# Text

# Spinbox

# Scale

# checkbutton

# Radiobutton

# Listbox


window.mainloop()
