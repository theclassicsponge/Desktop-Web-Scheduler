from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
import time


def submit():
    """Sets the time and the URL and opens the URL at the specified time. """
    global entry1, entry2, label3
    alarmtime = entry1.get()
    currenttime = time.strftime("%H:%M")
    alarmmessage = entry2.get()
    print(f"The Alarm time is: {alarmtime}")
    while alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if alarmtime == currenttime:
        print("Webpage Opening...")
        label3.config(text="Webpage Open")
        messagebox.showinfo("URL", f"This URL will open: {alarmmessage}. Press 'OK' to continue. ")
        webbrowser.open(entry2.get())


def createwidgets():
    """Creates the widgets for the tkinter UI."""
    label1 = Label(root, text="Enter the time in hh:mm - ")
    label1.grid(row=0, column=0, padx=5, pady=5)

    global entry1, submit
    entry1 = Entry(root, width=15)
    entry1.grid(row=0, column=1)

    label2 = Label(root, text="Enter the URL - ")
    label2.grid(row=1, column=0, padx=5, pady=5)

    global entry2
    entry2 = Entry(root, width=15)
    entry2.grid(row=1, column=1)

    but = Button(root, text="OK", width=10, command=submit)
    but.grid(row=2, column=1)

    global label3
    label3 = Label(root, text="")
    label3.grid(row=3, column=0)




root = tk.Tk()
root.title("Desktop Web Scheduler")
root.geometry("400x150")

createwidgets()

root.mainloop()
#git version
