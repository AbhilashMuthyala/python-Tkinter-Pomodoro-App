from tkinter import *
import time
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    global reps
    window.after_cancel(timer)
    label1.config(text='TIMER', fg=RED)
    canvas.itemconfig(timer_text, text='00:00')
    checkmark_label.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label1.config(text='LONG BREAK',fg=YELLOW)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        label1.config(text='SHORT BREAK',fg=YELLOW)
    else:
        countdown(WORK_MIN * 60)
        label1.config(text='WORK TIME',fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):

    #mins = count % 3600 // 60
    #seconds = count % 60
    mins = count // 60
    seconds = count-(mins*60)

    global timer

    var = str(mins) + ":" + str(seconds)
    canvas.itemconfig(timer_text, text = var)
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        work_session = reps // 2
        mark = ''
        for _ in range(work_session):
            mark += str('✓')
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=GREEN)


label1 = Label(text='Timer', bg=GREEN,fg=RED, font=(FONT_NAME,35,'bold'))
label1.grid(row=0,column=1)

canvas = Canvas(width=200,height=224,bg=GREEN, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text = canvas.create_text(100,130,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

# Creating Button for start
button_start = Button(text='Start',bg=GREEN,font=(FONT_NAME,8,'bold'),highlightthickness=0,command=start_timer)
button_start.grid(row=2,column=0)

# Creating Button for reset
button_reset = Button(text='Reset',bg=GREEN,font=(FONT_NAME,8,'bold'),highlightthickness=0,command=reset_timer)
button_reset.grid(row=2,column=2)

# Creating check marks
checkmark_label = Label()
checkmark_label.config(fg=RED,bg=GREEN)
checkmark_label.grid(row=2,column=1)

window.mainloop()

