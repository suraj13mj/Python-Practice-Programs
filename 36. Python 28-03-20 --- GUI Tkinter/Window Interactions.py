# Tkinter GUI Program to demonstrate how to implement Windows Interactions
# Invoking a Child window from Parent window and then again going to back to the Parent Window



from tkinter import *

class StudentWindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Student Window")

    def displayComponents(self,main_win):

        def btnBackClicked():
            main_win.deiconify()
            self.destroy()
            
        self.lblstud = Label(self,text="STUDENT",font=('Arial Bold',40))
        self.lblstud.place(x=50,y=50,width=300,height=50)

        self.btnback = Button(self,text="Back",command=btnBackClicked)
        self.btnback.place(x=150,y=200,width=80,height=30)

        


class EmployeeWindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Employee Window")

    def displayComponents(self,main_win):

        def btnBackClicked():
            main_win.deiconify()
            self.destroy()
            
        self.lblemp = Label(self,text="EMPLOYEE",font=('Arial Bold',40))
        self.lblemp.place(x=50,y=50,width=300,height=50)

        self.btnback = Button(self,text="Back",command=btnBackClicked)
        self.btnback.place(x=150,y=200,width=80,height=30)

        


class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Main Window")


    def displayComponents(self):

        def onStudentClicked():
            stud_win = StudentWindow()
            stud_win.displayComponents(self)
            self.withdraw()

        def onEmployeeClicked():
            emp_win = EmployeeWindow()
            emp_win.displayComponents(self)
            self.withdraw()
        
        self.btnStudent = Button(self,text="Student",command=onStudentClicked)
        self.btnStudent.place(x=150,y=100,width=100,height=30)

        self.btnEmployee = Button(self,text="Employee",command=onEmployeeClicked)
        self.btnEmployee.place(x=150,y=150,width=100,height=30)

        self.btnExit = Button(self,text="Exit",command=win.destroy)
        self.btnExit.place(x=150,y=200,width=100,height=30)


        


if __name__ == "__main__":
    win = MainWindow()
    win.displayComponents()
        

    
        
        
