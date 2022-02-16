import csv
import os
import shutil
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
WAIT_TIME = 3
INPUT_DATA = "data/french_words.csv"

# button functions
def correct_action():
    """function for correct button"""
    pass


def wrong_action():
    """function for wrong button"""
    pass


# canvas functions
def flip_card(img, language, meaning):
    """function for canvas to flip the card"""
    canvas.create_image(400, 300, image=img)
    canvas.create_text(400, 150, text=language, font=("Arial", "40", "italic"))
    canvas.create_text(400, 263, text=meaning, font=("Arial", "60", "bold"))


def front_and_back_action(img_1, img_2, language_1, language_2, meaning_1, meaning_2):
    """function for canvas to create one set of cards"""
    flip_card(img_1, language_1, meaning_1)
    window.after(WAIT_TIME * 1000, flip_card, img_2, language_2, meaning_2)


# handle the input

# make a backup of the input file
input_path = os.path.dirname(INPUT_DATA)
orig_file = INPUT_DATA + ".orig"
orig_name = os.path.basename(orig_file)
print(f"orig_file: {orig_file}\norig_name: {orig_name}")
if orig_name in os.listdir(input_path):
    pass
else:
    shutil.copy(INPUT_DATA, orig_file)


with open(INPUT_DATA, "r") as f_in:
    pass


# build the GUI

window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")

img_front = tk.PhotoImage(file="images/card_front.png")
img_bck = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

front_and_back_action(img_front, img_bck, "French", "English", "Bonjour", "Hello")
canvas.grid(row=0, column=0, columnspan=2)

img_wrong = tk.PhotoImage(file="images/wrong.png")
btn_wrong = tk.Button(image=img_wrong, highlightthickness=0)
btn_wrong.grid(row=1, column=0)

img_right = tk.PhotoImage(file="images/right.png")
btn_right = tk.Button(image=img_right, highlightthickness=0)
btn_right.grid(row=1, column=1)

window.mainloop()
