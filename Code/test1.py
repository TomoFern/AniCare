#These 2 lines of code import the Tkinter Library which allows me to create a GUI
from tkinter import *
from tkinter import ttk

app = Tk()
frm = ttk.Frame(app, padding = 10)
frm.grid()
app.title("AniCare")
app.geometry('500x500')
app['bg'] = '#de6969'
app.mainloop()