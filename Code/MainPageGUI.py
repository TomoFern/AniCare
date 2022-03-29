from tkinter import *
from tkinter import ttk

def StartMain():
        homeScreen = Tk()
        frma = ttk.Frame(homeScreen, padding = 10)
        frma.grid()
        homeScreen.title('AniCare Home Screen')
        homeScreen.geometry('1920x1080')
        homeScreen['bg'] = "#de6969"
        homeScreen.wm_attributes("-fullscreen" , True )

        boxa = Label(text="")
        boxa.config(height = 55, width = 240)
        boxa.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        homeScreen.mainloop()
