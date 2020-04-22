# Program to demonstrate the use of Labels and Buttons using Tkinter

from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("GUI component Demo")

def okClicked():
  lbl.configure(text="You clicked on OK")

def cancelClicked():
  lbl.configure(text="You clicked on CANCEL")

def exitClicked():
  win.withdraw()

lbl = Label(win,text="",font=("Arial Bold",20))
lbl.place(x=30,y=50,width=350,height=100)


btnOk = Button(win,text="OK",bg="orange",fg="white",command=okClicked)
btnOk.place(x=60,y=200,width=80,height=50)


btnCncl = Button(win,text="CANCEL",bg="white",fg="blue",command=cancelClicked)
btnCncl.place(x=150,y=200,width=80,height=50)


btnExit = Button(win,text="EXIT",bg="green",fg="white",command=win.withdraw)
btnExit.place(x=240,y=200,width=80,height=50)
