#GUI Program to demonstrate Register window

from tkinter import *
from tkinter import messagebox
from Bean_Student import *
import StudentDB

class Register(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Register")

    def displayComponents(self,login_win):

        self.lblhead = Label(self,text="Registration",font=("Arial Bold",22))
        self.lblhead.place(x=100,y=50,width=200,height=50)

        self.lblusername = Label(self,text="Username:",font=("Arial",15))
        self.lblusername.place(x=50,y=150,width=100,height=30)

        self.txtusername = Entry(self,width=100,font=("Arial",13))
        self.txtusername.place(x=160,y=150,width=140,height=30)

        self.lblpassword = Label(self,text="Password:",font=("Arial",15))
        self.lblpassword.place(x=50,y=200,width=100,height=30)

        self.txtpassword = Entry(self,width=100,show="*",font=("Arial",13))
        self.txtpassword.place(x=160,y=200,width=140,height=30)

        self.lblsug = Label(self,text="Please Login after Registeration",font=("Arial Bold",12))
        


        def onRegClicked():
            stud_obj = Student()
            stud_obj.Username = self.txtusername.get()
            stud_obj.Password = self.txtpassword.get()

            res=StudentDB.insertLoginDetails(stud_obj)
            if res:
                self.lblsug.place(x=75,y=350,width=250,height=50)
                messagebox.showinfo("Authentication","Registration Successful")
                self.destroy()
                login_win.deiconify()
            else:
                messagebox.showinfo("Authentication","Error Saving Registration Detials..!!")

        def onBackClicked():
            self.destroy()
            login_win.deiconify()

         

        self.btnreg = Button(self,text="Register",font=("Cambria Bold",13),command=onRegClicked)
        self.btnreg.place(x=160,y=250,width=80,height=30)


        self.btnback = Button(self,text="Back",font=("Cambria Bold",13),command=onBackClicked)
        self.btnback.place(x=160,y=290,width=80,height=30)