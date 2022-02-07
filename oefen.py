import tkinter as tk
from tkinter.constants import LEFT
from typing import Sized
scherm = tk.Tk()



x = ["uit"]

# schijf hier tussen je code

def knop_switch():
    if x[0]== "uit":
        x[0] = "aan"
        print(x[0])
        scherm.configure(background="yellow")
        knop.configure(text="licht is aan ")
    else: 
        x[0] = "uit"
        print(x[0])
        scherm.configure(background="black")
        knop.configure(text="licht is uit")


scherm.configure(padx=100,pady=100)
knop = tk.Button(text='knop', bg="yellow", fg="black",command=knop_switch,height=1,width=15)
knop.pack()
titel = tk.Label(text="gemaakt door Bram",bg="purple",fg="orange",height=1,width=20)
titel.pack(side="top")



