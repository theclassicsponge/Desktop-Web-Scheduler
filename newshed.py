from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser
import time, os


def submit():
    global entry1, entry2, label3
    Alarmtime = entry1.get()
    #message1()
    currenttime = time.strftime("%H:%M")
    alarmmessage = entry2.get()
    print(f"The Alarm time is: {Alarmtime}")
    while Alarmtime != currenttime:
        currenttime = time.strftime("%H:%M")
        time.sleep(1)
    if Alarmtime == currenttime:
        print("Webpage Opening...")
        label3.config(text="Webpage Open")
        messagebox.showinfo("URL", f"This URL will open: {alarmmessage}. Press 'OK' to continue. ")
        webbrowser.open(entry2.get())

def createWidgets():
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

    def message1():

        global entry1, label3
        Alarmtimelable = entry1.get()
        label3.config(text="The Time is Set...")
        messagebox.showinfo("Webpage", f"The time is {Alarmtimelable}")

    #def submit():

        #global entry1, entry2, label3
        #Alarmtime = entry1.get()
        #message1()
        #currenttime = time.strftime("%H:%M")
        #alarmmessage = entry2.get()
        #print(f"The Alarm time is: {Alarmtime}")
        #while Alarmtime != currenttime:
            #currenttime = time.strftime("%H:%M")
           # time.sleep(1)
        #if Alarmtime == currenttime:
            #print("Webpage Opening...")
            #label3.config(text="Webpage Open")
           # messagebox.showinfo("URL", f"The URL is:{alarmmessage}")
            #webbrowser.open(entry2.get())


root = tk.Tk()
root.title("Desktop Web Scheduler")
root.geometry("400x150")

createWidgets()

root.mainloop()
#git version
