"""A Desktop program where you can upload images and add a watermark.
"""
from tkinter import *
from tkinter import filedialog


"""Find the correct library to do this
"""


def select_image():
    """Select an image to show in the viewer"""
    f = filedialog.askopenfilename(initialdir="/", title="Select an image", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    # f = tk.filedialog.askopenfile(mode="r", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    # ! Stopped here, should return a photoimage object for viewer later
    print(f)


# ----- UI SETUP ----- #
window = Tk()
window.title("Image Viewer")
window.geometry("500x500")
window.config(padx=20, pady=20, bg="#ffffcc")

canvas = Canvas(width=500, height=500, bg="#ffffcc", highlightthickness=0)

btn = Button(text="Select", highlightthickness=0, command=select_image)
btn.grid(column=0, row=2, columnspan=2)


# ----- Watermark Mechanism ----- #


window.mainloop()
