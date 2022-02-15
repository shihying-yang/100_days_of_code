import tkinter as tk
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
SLEEP_MS = 1000
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """reset timer with the following actions: reset timer text, change timer title,
    reset the check mark, reset the reps"""
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # timer title "Timer"
    lbl_title.config(text="Timer", fg=GREEN)
    # reset check marks
    lbl_check.config(text="")
    # reset the reps
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """start timer, set the timer to 25 minutes"""
    global REPS

    REPS += 1
    if REPS % 8 == 0:
        lbl_title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif REPS % 2 == 0:
        lbl_title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        lbl_title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """count down mechanism"""
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{str(count_min)}:{str(count_sec).zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(SLEEP_MS, count_down, count - 1)
    else:
        # # my way, maybe not the best way?
        # if REPS % 2 == 1:
        #     to_print_count = REPS // 2 + 1
        #     to_print_text = "✔" * to_print_count
        #     lbl_check.config(text=to_print_text)
        winsound.Beep(440, 500)
        start_timer()
        # add the check mark
        marks = ""
        work_session = REPS // 2
        for _ in range(work_session):
            marks += "✔"
        lbl_check.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
# create the window
window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=500, height=500)
window.config(padx=100, pady=40, bg=YELLOW)

## Complete the UI with lables and buttons etc
# timer label
lbl_title = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
lbl_title.grid(column=1, row=0)

# create the canvas to hold the image
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

# count_down(5)

# start and reset buttons
btn_start = tk.Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
btn_reset.grid(column=2, row=2)

# show check marks for current status
lbl_check = tk.Label(font=(FONT_NAME, "15", "normal"), fg=GREEN, bg=YELLOW)
lbl_check.grid(column=1, row=3)

window.mainloop()
