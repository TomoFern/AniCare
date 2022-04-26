#These lines of code import the necessary libraries which allow me to create a GUI
from textwrap import shorten 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#This line of code imports the LoginValidaion script which allows me to use the functions
import LoginValidation

#Here, the LoginScreen function is created where the GUI for the login screen is created
def LoginScreen():
     #These statements make the app, userstore and passstore variales global
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

     app.mainloop()

#Here the checker function is defined
def Checker():  
     username = LoginValidation.UsernameValidator(userstore.get())
     if userstore.get() == "":
          messagebox.showwarning("Oops!", "Please Enter A Username")
     elif username == -1:
          print("Invalid Username")
          messagebox.showinfo("Oops!", "Invalid Username")
     else:
          password = LoginValidation.PasswordValidator(passstore.get(), username)
          if passstore.get() == "":
               messagebox.showwarning("Oops!", "Please Enter A Password")
          elif password == -1:
               print("Invalid Password")
               messagebox.showinfo("Oops!", "Invalid Password")
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

     box = Label(text="Current Animals")
     box.config(height = 50, width = 100)
     box.place(relx = 0.03, rely = 0.2)

     boxb = Label(text="Add New Animal")
     boxb.config(height = 50, width = 100)
     boxb.place(relx = 0.6, rely = 0.2)

     navbar = Label(text = "")
     navbar.config(height = 5, width = 250)
     navbar.place(relx = 0.04, rely = 0.02)

     def Minimize(esc):
          homeScreen.wm_attributes("-fullscreen", False)
     
     homeScreen.bind('<Escape>', lambda esc: Minimize(esc))

     homeScreen.mainloop()

LoginScreen()
