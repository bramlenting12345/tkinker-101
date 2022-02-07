from asyncio import sleep
from cgitb import text
from distutils import command
from re import A
from time import time
import tkinter as tk
from turtle import bgcolor 
import random
import time 

# ========================{-variabelen / lijsten-}=============================

x=[50]
kleuren = ["red","yellow","orange","green","purple","black"]
positie = [0]
afteller = [6]

# =============================={-def vergroot programmma-}=====================

def vergroot(x,afteller):
   
    x[0]= x[0] + 50   
    begin.configure(bg=kleuren[positie[0]])
      
    positie[0] = positie[0] + 1
    afteller[0] = afteller[0]  - 1

    for i in range(len(afteller)):
        print(afteller[i])

    begin.geometry(str(x[0])+'x'+str(x[0]))

    if positie[0] == 6:
        print("boom") 
        label = tk.Label(begin,text="BOOM!!!!")  
        label.pack()     

 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{-hoofdprogramma-}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.

begin = tk.Tk()
begin.title("kik hier om de kleur te verranderen en de groote  ")
begin.geometry(str(x[0])+ 'x' + str(x[0]))
      

btn1 = tk.Button(begin, text = "button 1", command = lambda:vergroot(x,afteller))
btn1.pack() 

begin.mainloop()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{-hoofdprogramma-}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>