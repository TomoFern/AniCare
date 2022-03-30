#These 2 lines of code import the Tkinter Library which allows me to create a GUI
from textwrap import shorten
from tkinter import *
from tkinter import ttk

from soupsieve import escape
import LoginValidation
import os
import sys
import MainPageGUI
from MainPageGUI import *

def LoginScreen():
     global app
     global userstore
     global passstore
     app = Tk()
     frm = ttk.Frame(app, padding = 10)
     frm.grid()
     app.title("AniCare")
     app.geometry('1920x1080')
     app['bg'] = '#de6969'
     app.wm_attributes("-fullscreen", True)

     userstore = StringVar()
     passstore = StringVar()

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

     def Minimize(e):
          app.wm_attributes("-fullscreen", False)

     app.bind('<Escape>', lambda e: Minimize(e))
     app.bind('<Enter>', lambda en: Checker(en))

     app.mainloop()

def Checker(en):
     username = LoginValidation.UsernameValidator(userstore.get())
     if username == -1:
          print("Invalid Username")
     else:
          password = LoginValidation.PasswordValidator(passstore.get(), username)
          if password == -1:
               print("Invalid Password") 
          else:
               app.destroy()
               StartMain()
               print("Access Granted")


def StartMain():
        global homeScreen
        homeScreen = Tk()
        frma = ttk.Frame(homeScreen, padding = 10)
        frma.grid()
        homeScreen.title('AniCare Home Screen')
        homeScreen.geometry('1920x1080')
        homeScreen['bg'] = "#de6969"
        homeScreen.wm_attributes("-fullscreen" , True)

        boxa = Label(text="")
        boxa.config(height = 55, width = 240)
        boxa.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        homeScreen.mainloop()

LoginScreen()
