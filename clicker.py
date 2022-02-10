from cgitb import text
import tkinter as tk
from turtle import down 


# Maak een programmatje met een GUI van 2 buttons met daartussen een label.

# Het heeft de volgende eisen:
# 1 knop zorgt er voor dat het nummer in de label met 1 omhoog gaat
# 1 knop zorgt er voor dat het nummer in de label met 1 omlaag gaat.
# Als het nummer 0 is moet de achtergrond grijs zijn.
# Als het nummer kleiner dan 0 is moet de achtergrond rood zijn.
# Als het nummer groter dan 0 is moet de achtergrond groen zijn


opteller = [0]

def optellen_up(opteller):
    opteller[0] = opteller[0] + 1
    teller.configure(text=opteller[0])

    opteller_up = opteller[0]
    if opteller_up > 0:
        clicker.configure(bg="green")
    if opteller_up < 0:
        clicker.configure(bg="red")


def afteller_down(opteller):
    opteller[0] = opteller[0] - 1
    teller.configure(text=opteller[0])
    opteller_up = opteller[0]
    
    if opteller_up > 0:
        clicker.configure(bg="green")
    if opteller_up < 0:
        clicker.configure(bg="red")

    
    

clicker=tk.Tk() 
clicker.title("place() methode") 
clicker.geometry("300x300")
clicker.configure(bg="grey")

button_up=tk.Button(clicker, text="UP",padx=80,pady=2,command=lambda:optellen_up(opteller))
button_up.place(x=60, 
                y=40,)

button_down=tk.Button(clicker, text="down",padx=80,pady=2,command=lambda:afteller_down(opteller))
button_down.place(x=50, 
                  y=220,)                

teller = tk.Label(clicker,bg="white",text=opteller,padx=85,pady=2)
teller.place(relx = 0.5,
             rely = 0.5,
             anchor = 'center')



clicker.mainloop()



