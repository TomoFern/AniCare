#These 2 lines of code import the Tkinter Library which allows me to create a GUI
from textwrap import shorten
from tkinter import *
from tkinter import ttk
import LoginValidation

app = Tk()
frm = ttk.Frame(app, padding = 10)
frm.grid()
app.title("AniCare")
app.geometry('1920x1080')
app['bg'] = '#de6969'

userstore = StringVar()
passstore = StringVar()

def Checker():
     username = LoginValidation.UsernameValidator(userstore.get())
     if username == -1:
          print("Invalid Username")
     else:
          password = LoginValidation.PasswordValidator(passstore.get(), username)
          if password == -1:
               print("Invalid Password")
          else:
               print("Access Granted")

box = Label(text="")
box.config(height = 50, width = 100)
box.place(relx = 0.5, rely = 0.5, anchor = CENTER)

usertext = Label(text = "Username")
usertext.place(relx = 0.5, rely = 0.275, anchor = CENTER)
userentry = Entry(app, bg = 'white', bd = 5, textvariable = userstore)
userentry.config(width = 30)
userentry.focus()
userentry.place(relx = 0.5, rely = 0.3, anchor = CENTER)

passtext = Label(text = "Password")
passtext.place(relx = 0.5, rely = 0.375, anchor = CENTER)
passentry = Entry(app, bg = 'white', bd = 5, textvariable = passstore, show = "*")
passentry.config(width = 30)
passentry.place(relx = 0.5, rely = 0.4, anchor = CENTER)

enterbutton = Button(text = "Enter", command = Checker)
enterbutton.place(relx = 0.5, rely = 0.6, anchor = CENTER)

app.mainloop()
