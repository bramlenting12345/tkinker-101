from email import message
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from turtle import mainloop 

popup = tk.Tk()
popup.title("bericht oefenen")
popup.iconbitmap('dit is een test ')

def popup():
    messagebox.showinfo("gefelisiteert u heeft een item ","hello world ")





Button(popup,text="popup", command=popup) . pack()




mainloop()