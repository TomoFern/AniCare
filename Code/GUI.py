#These 2 lines of code import the Tkinter Library which allows me to create a GUI
from tkinter import *
from tkinter import ttk
import LoginValidation

app = Tk()
frm = ttk.Frame(app, padding = 10)
frm.grid()
app.title("AniCare")
app.geometry('500x500')
app['bg'] = '#de6969'
userentry = Entry(app, bg = 'white', bd=5)
userentry.place(relx=0.5, rely=0.5, anchor=CENTER)
testvar = (userentry.get())

app.mainloop()
