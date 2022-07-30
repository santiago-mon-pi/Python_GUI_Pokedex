#import tkinter library, the * is used to import all build in functions and modules in the library and ttk
# and ttk is used to use the package to style the program's properties and its look and feel
from curses import window
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

window.mainloop()