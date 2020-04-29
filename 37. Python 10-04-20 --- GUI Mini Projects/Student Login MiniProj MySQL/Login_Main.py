# GUI Program to demonstrate a Login window

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Bean_Student import *
from StudentDB import *
from Student_Window import *
from Register import *


class Login(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Login")
        self.displayComponents()

    def displayComponents(self):

        self.lblhead = Label(self,text="Student Login",font=("Arial Bold",22))
        self.lblhead.place(x=100,y=50,width=200,height=50)

        self.lblusername = Label(self,text="Username:",font=("Arial",15))
        self.lblusername.place(x=50,y=150,width=100,height=30)

        self.txtusername = Entry(self,width=100,font=("Arial",13))
        self.txtusername.place(x=160,y=150,width=140,height=30)

        self.lblpassword = Label(self,text="Password:",font=("Arial",15))
        self.lblpassword.place(x=50,y=200,width=100,height=30)

        self.txtpassword = Entry(self,width=100,show="*",font=("Arial",13))
        self.txtpassword.place(x=160,y=200,width=140,height=30)


        def onLoginClicked():
            stud_obj = Student()
            stud_obj.Username = self.txtusername.get()
            stud_obj.Password = self.txtpassword.get()

            res = StudentDB.checkPassword(stud_obj)
            if len(res) == 1:
                messagebox.showinfo("Authentication","Login Successful")
                stud_win = StudentWindow(self,stud_obj)
                stud_win.display()
                self.withdraw()
            else:
                messagebox.showinfo("Authentication","Invalid Credentials")

        def onRegisterClicked():
            reg_win = Register()
            reg_win.displayComponents(self)
            self.withdraw()
            
            

        self.btnlogin = Button(self,text="Login",font=("Cambria Bold",13),command=onLoginClicked)
        self.btnlogin.place(x=160,y=250,width=80,height=30)

        self.lblregister = Label(self,text="New User..?",font=("Cambria",13))
        self.lblregister.place(x=50,y=290,width=100,height=30)

        self.btnregister = Button(self,text="Register",font=("Cambria Bold",13),command=onRegisterClicked)
        self.btnregister.place(x=160,y=290,width=80,height=30)
        

        



if __name__ == "__main__":
    login_win = Login()
    
