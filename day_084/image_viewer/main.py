"""A Desktop program where you can upload images and add a watermark.
"""
# from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

"""Find the correct library to do this
"""
BASE_IMG_PATH = None

# ---- Load Image from file ---- #
def load_image():
    """Select an image to show in the viewer"""
    global BASE_IMG_PATH
    BASE_IMG_PATH = filedialog.askopenfilename(
        initialdir=".", title="Select an image", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
    )
    new_img = ImageTk.PhotoImage(file=BASE_IMG_PATH)
    canvas.itemconfig(canvas_img, image=new_img)
    canvas.mainloop()


# ----- Watermark Mechanism ----- #
def apply_watermark():
    base_image = Image.open(BASE_IMG_PATH)
    watermark = Image.open("watermark.png")
    base_image.paste(watermark, (10, 10))
    new_image = ImageTk.PhotoImage(base_image)
    canvas.itemconfig(canvas_img, image=new_image)
    base_image.save("modified_image.jpg")
    canvas.mainloop()


# ----- UI SETUP ----- #
window = tk.Tk()
window.title("Image Viewer")
# window.geometry("500x500")
window.config(padx=20, pady=20, bg="#ffffcc")


btn_load = tk.Button(text="Select Image", highlightthickness=0, command=load_image)
btn_load.grid(row=0, column=0)

btn_apply = tk.Button(text="Apply Watermark", highlightthickness=0, command=apply_watermark)
btn_apply.grid(row=0, column=1)

logo_img = tk.PhotoImage(file="no-image.png")

canvas = tk.Canvas(width=500, height=500, bg="#ffffff", highlightthickness=0)
canvas_img = canvas.create_image(0, 0, image=logo_img, anchor="nw")
canvas.grid(column=0, row=1, columnspan=2, pady=20)


window.mainloop()
