from re import X
from time import strftime
import tkinter as tk

scherm = tk.Tk()
scherm.title("tkinter klok ")
scherm.geometry("200x80")
scherm.configure(bg="gold")
scherm.resizable(False, False)



clock_label = tk.Label(scherm, bg="silver", fg="blue", font=("Times", 30, 'bold'),relief='flat')
clock_label.place(x = 20, y = 20)


def maak_klok():
    tegenwoordige_tijd = strftime('%H: %M: %S')
    clock_label.configure(text= tegenwoordige_tijd)
    clock_label.after(80,maak_klok)


maak_klok()
scherm.mainloop()
