import threading, words, random
import tkinter as tk
from tkinter import Button, Text, Label, END
import time

sts_running = False
time_counting = 0.00


def reset():
    global sts_running, time_counting
    sts_running = False
    inputtext.delete(1.0, END)
    time_label.config(text=f'{0.00} : CPS')
    time_label_min.config(text=f'{0.00} : CPM')
    screen_label.config(text=random.choice(words.sentence_list), fg='black')
    inputtext.config(background='white', fg='black')


def start(event):
    global sts_running
    sts_running = True
    if sts_running:
        threading.Thread(target=timer).start()
        typed_text = inputtext.get('1.0', 'end-1c')
        text_to_type = screen_label.cget('text')
        try:

            if typed_text == text_to_type[:len(typed_text)]:
                screen_label.config(fg='green')

            else:
                screen_label.config(fg='red')
        except IndexError:
            pass

        if len(text_to_type) <= len(typed_text):
            if typed_text == text_to_type:
                inputtext.config(background='green', fg='white')
            else:
                inputtext.config(background='red', fg='white')
            sts_running = False
    else:
        sts_running = False


def timer():
    global time_counting
    while sts_running:
        time.sleep(0.1)
        time_counting += 0.1
        try:
            cps = len(inputtext.get('1.0', 'end-1c')) / time_counting
            time_label.config(text=f"{cps:.2f} : CPS")
            time_label_min.config(text=f"{cps * 60:.2f} : CPM")
        except ZeroDivisionError:
            pass


screen = tk.Tk()
screen.geometry('800x600')
frame = tk.Frame(screen)
screen_label = Label(frame, text=random.choice(words.sentence_list), font=('Arial', 18), padx=20, pady=20)
screen_label.pack()
inputtext = Text(frame, width=50, height=10, font=('Arial', 14), padx=20, pady=20)
inputtext.bind('<KeyRelease>', start)
inputtext.pack()
time_label = Label(frame, text=f'{time_counting} : CPS', font=('Arial', 18), padx=20, pady=20)
time_label.pack()
time_label_min = Label(frame, text=f'{time_counting} : CPM', font=('Arial', 18), padx=20, pady=20)
time_label_min.pack()
reset_button = Button(frame, text='Reset', command=reset)
reset_button.pack()
frame.pack(expand=True)
screen.mainloop()

