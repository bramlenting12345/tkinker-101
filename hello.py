import tkinter as tk
from typing import Sized

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

buiten_scherm = tk.Tk()
buiten_scherm.geometry("200x200")
buiten_scherm.configure(bg="gold")

binnen_scherm = tk.Label(buiten_scherm,padx=20,pady=30,fg="white",bg="blue",text="Hello Tkinter !",font=(None, 15))


binnen_scherm.pack()
buiten_scherm.mainloop()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>