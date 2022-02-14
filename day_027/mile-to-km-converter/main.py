import tkinter as tk

CONVERT_RATE = 1.609

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert_m_km():
    """convert miles to km"""
    miles = entry_num_to_convert.get()
    km = round(float(miles) * CONVERT_RATE, 2)
    lb_converted_num.config(text=f"{km}")


def convert_km_m():
    """convert miles to km"""
    km = entry_num_to_convert.get()
    miles = round(float(km) / CONVERT_RATE, 2)
    lb_converted_num.config(text=f"{miles}")


def radio_used():
    """convert both ways"""
    # print(radio_selected.get())
    if radio_selected.get() == 1:
        lb_to_convert_unit.config(text="Miles")
        lb_convert_to_unit.config(text="Km")
    else:
        lb_to_convert_unit.config(text="Km")
        lb_convert_to_unit.config(text="Miles")


def calculate_func():
    """encapulate the functions for both way conversion"""
    if radio_selected.get() == 1:
        convert_m_km()
    else:
        convert_km_m()


# entry for inputing miles
entry_num_to_convert = tk.Entry(width=7)
entry_num_to_convert.insert(0, string="0")
entry_num_to_convert.grid(column=1, row=0)

# miles wording
lb_to_convert_unit = tk.Label(text="Miles")
lb_to_convert_unit.grid(column=2, row=0)

# equals wording
lbl_equal = tk.Label(text="is equal to")
lbl_equal.grid(column=0, row=1)

# km number after calculation
lb_converted_num = tk.Label(text="0")
lb_converted_num.grid(column=1, row=1)

# km wording
lb_convert_to_unit = tk.Label(text="Km")
lb_convert_to_unit.grid(column=2, row=1)

# calculate button
calc_btn = tk.Button(text="Calculate", command=calculate_func)
calc_btn.grid(column=1, row=2)

## Extra work, make it converting both ways
radio_selected = tk.IntVar(value=1)
mk_radio = tk.Radiobutton(text="Miles ➡ Km", value=1, variable=radio_selected, command=radio_used)
km_radio = tk.Radiobutton(text="Km ➡ Miles", value=2, variable=radio_selected, command=radio_used)
mk_radio.grid(column=3, row=0)
km_radio.grid(column=3, row=1)


window.mainloop()
