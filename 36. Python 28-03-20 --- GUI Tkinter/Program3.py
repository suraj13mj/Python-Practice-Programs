#Program to demonstrate the use of Messagebox (Dialogbox) using Tkinter module 

from tkinter import *
from tkinter import messagebox

class MyWindow(Tk):
    
    def onOkClicked(self):
        messagebox.showinfo("Window","Your name is :"+self.txtName.get())
        
    def onCancelClicked(self):
        messagebox.showinfo("Window","You clicked on CANCEL")

    def onExitClicked(self):
        self.withdraw()

    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("GUI component demo")

        self.lbl = Label(self,text="Name")
        self.lbl.place(x=40,y=90,width=60,height=50)

        self.txtName = Entry(self)
        self.txtName.place(x=110,y=100,width=100,height=30)

        self.btnOk = Button(self,text="OK",command=self.onOkClicked)
        self.btnOk.place(x=20,y=200,width=80,height=50)

        self.btnCncl = Button(self,text="CANCEL",command=self.onCancelClicked)
        self.btnCncl.place(x=110,y=200,width=80,height=50)

        self.btnExit = Button(self,text="Exit",command=self.onExitClicked)
        self.btnExit.place(x=200,y=200,width=80,height=50)


if __name__ == "__main__":
    win = MyWindow()
