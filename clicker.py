import tkinter as tk 


# Maak een programmatje met een GUI van 2 buttons met daartussen een label.

# Het heeft de volgende eisen:
# 1 knop zorgt er voor dat het nummer in de label met 1 omhoog gaat
# 1 knop zorgt er voor dat het nummer in de label met 1 omlaag gaat.
# Als het nummer 0 is moet de achtergrond grijs zijn.
# Als het nummer kleiner dan 0 is moet de achtergrond rood zijn.
# Als het nummer groter dan 0 is moet de achtergrond groen zijn

opteller = [0]

def opteller_up(opteller):
    up_teller = len(opteller)
    opteller[0] = opteller[0] + 1
    teller.configure(text=opteller[0])

    up_teller = len(opteller)
    if up_teller > 0:
        clicker.configure(bg="red")

    
    

clicker=tk.Tk() 
clicker.title("place() methode") 
clicker.geometry("300x300")
clicker.configure(bg="grey")

button_up=tk.Button(clicker, text="UP",padx=80,pady=2,command=lambda:opteller_up(opteller))
button_up.place(x=60, 
                y=60,)

teller = tk.Label(clicker,bg="white",text=opteller,padx=85,pady=2)
teller.place(relx = 0.5,
            rely = 0.5,
            anchor = 'center')


clicker.mainloop()



