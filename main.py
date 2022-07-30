#import tkinter library, the * is used to import all build in functions and modules in the library and ttk
# and ttk is used to use the package to style the program's properties and its look and feel

import tkinter
from tkinter import *
from tkinter import ttk

#colors
co0 = "#444466" #black
co1 = "#feffff" #white
co2 = "#6f9fbd" #blue
co3 = "#403d3d" #ash

window = Tk()
window.title("Monpi's Pokedex!")
window.geometry('550x510')
window.resizable(width=False, height=False)
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(window, width=500, height=395, bg=co2)
main_frame.grid(row=0, column=0, padx=1, pady=1)

pk_name = Label(main_frame,text="Squirtle", anchor="center", font=("Ivy 20 bold"), fg=co0)
pk_name.place(x=15, y=15)

pk_type = Label(main_frame,text="type", anchor="center", font=("Verdana 10 bold"), fg=co0)
pk_type.place(x=20, y=50)

pk_number = Label(main_frame,text="number", anchor="center", font=("Verdana 10 bold"), fg=co0)
pk_number.place(x=20, y=75)
window.mainloop()