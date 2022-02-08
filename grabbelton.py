from cgitb import text
from distutils import command
import tkinter as tk
from tkinter import Button, font
from tkinter import messagebox
import random

# Een GUI opend met een knop er in waarop grabbelen staat
# Een label met het aantal items in de grabbelton
# Als je op de knop drukt moet je het bericht te zien krijgen: “Gefeliciteerd, je hebt een {item} gegrabbeld!”
# Op de plek van {item} in de tekst moet een woord komen die je random uit een lijst met minimaal 10 verschillende woorden haalt
# Daarna moet het aantal items worden aangepast en mag dat woord niet meer terug komen


producten = ["bal","vliegtuig","vogel","flesje bier","koekje","sigaretten","jacht","mercedes","tijger","granaat"]

def aanmaak_bericht():
    random.shuffle(producten)
    LengteProduct = len(producten)

    if LengteProduct > 0:
        messagebox.showinfo("druk oke ","gefeliciteert u heeft een  " + producten[0])
        producten.pop(0)
        knop.configure(text=len(producten))
    else: 
        knop.configure(text="0")
        messagebox.showwarning("druk oke om af te slutien","er zijn helaas geen items meer ")
        exit()


grabbelton = tk.Tk()
grabbelton.geometry("300x300")
grabbelton.configure(bg="silver")
grabbelton.title("grabbel maar raak !!!! ")

knop = tk.Button(grabbelton,bg="red",fg="black",text=len(producten),padx=20,pady=20,command=aanmaak_bericht)
naam_grabbelton = tk.Label(grabbelton,text="grabbelton",bg="blue",fg="white",font=(None, 20))


naam_grabbelton.pack()
knop.pack()
grabbelton.mainloop()
