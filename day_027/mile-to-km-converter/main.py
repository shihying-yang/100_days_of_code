import tkinter as tk

CONVERT_RATE = 1.609

window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


def convert_m_km():
    """convert miles to km"""
    miles = entry_miles.get()
    km = round(float(miles) * CONVERT_RATE, 2)
    lbl_km_num.config(text=f"{km}")


# entry for inputing miles
entry_miles = tk.Entry(width=7)
entry_miles.insert(0, string="0")
entry_miles.grid(column=1, row=0)

# miles wording
lbl_miles_word = tk.Label(text="Miles")
lbl_miles_word.grid(column=2, row=0)

# equals wording
lbl_equal = tk.Label(text="is equal to")
lbl_equal.grid(column=0, row=1)

# km number after calculation
lbl_km_num = tk.Label(text="0")
lbl_km_num.grid(column=1, row=1)

# km wording
lbl_km_word = tk.Label(text="Km")
lbl_km_word.grid(column=2, row=1)

# calculate button
calc_btn = tk.Button(text="Calculate", command=convert_m_km)
calc_btn.grid(column=1, row=2)

window.mainloop()
