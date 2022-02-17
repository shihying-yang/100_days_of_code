import os
import random
import shutil
import tkinter as tk

import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
WAIT_TIME = 3
INPUT_DATA = "data/french_words.csv"
current_words = {}

# general fuctions
def get_words(w_list):
    """Get the words in a list"""

    global current_words
    if len(w_list) > 0:
        current_words = random.choice(w_list)


# correct button functions
def known_card_action():
    """function for correct button"""
    words_list.remove(current_words)
    data = pd.DataFrame(words_list)
    data.to_csv(INPUT_DATA, index=False)
    next_card()


def next_card():
    """function for wrong button"""
    global flip_timer
    window.after_cancel(flip_timer)
    get_words(words_list)
    canvas.itemconfig(background_img, image=img_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(meaning_text, text=current_words["French"], fill="black")
    flip_timer = window.after(WAIT_TIME * 1000, flip_back)


# canvas functions
def flip_back():
    """function for canvas to flip the card"""
    canvas.itemconfig(background_img, image=img_bck)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(meaning_text, text=current_words["English"], fill="white")


# handle the input

# make a backup of the original input file
input_path = os.path.dirname(INPUT_DATA)
orig_file = INPUT_DATA + ".orig"
orig_name = os.path.basename(orig_file)
if orig_name in os.listdir(input_path):
    # the backup of the original file has been done
    pass
else:
    # make the backup of the original file
    shutil.copy(INPUT_DATA, orig_file)


# read the input csv file with pandas
data = pd.read_csv(INPUT_DATA)
words_list = data.to_dict(orient="records")


# build the GUI

window = tk.Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Card")

flip_timer = window.after(WAIT_TIME * 1000, flip_back)

img_front = tk.PhotoImage(file="images/card_front.png")
img_bck = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = canvas.create_image(400, 263, image=img_front)
title_text = canvas.create_text(400, 150, text="French", font=("Arial", "40", "italic"))
meaning_text = canvas.create_text(400, 263, text="English", font=("Arial", "60", "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# create the buttons
img_unknown = tk.PhotoImage(file="images/wrong.png")
btn_unknown = tk.Button(image=img_unknown, highlightthickness=0, command=next_card)
btn_unknown.grid(row=1, column=0)

img_known = tk.PhotoImage(file="images/right.png")
btn_known = tk.Button(image=img_known, highlightthickness=0, command=known_card_action)
btn_known.grid(row=1, column=1)

# show the first card
next_card()

window.mainloop()
