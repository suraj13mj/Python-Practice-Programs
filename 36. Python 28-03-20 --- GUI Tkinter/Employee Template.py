#Program to demonstrate the use of various GUI components using Tkinter
'''
1. Label
2. Button
3. TextBox
4. TextArea
'''

from tkinter import *
from tkinter import messagebox

class Employee(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x700")
        self.title("Employee Information")

    def display(self):
        self.lbl_heading = Label(self, text="Employee Details", font=("Arial Bold",28))
        self.lbl_heading.place(x=70,y=10,width=320,height=90)

        self.lbl_name = Label(self, text="Name:         ", font=("Arial",15))
        self.lbl_name.place(x=50,y=110,width=120,height=20)

        self.txt_name = Entry(self, width=50)
        self.txt_name.place(x=160,y=110,width=150,height=20)

        self.lbl_empno = Label(self, text="Emp No:       ", font=("Arial",15))
        self.lbl_empno.place(x=50,y=140,width=120,height=20)

        self.txt_empno = Entry(self, width=50)
        self.txt_empno.place(x=160,y=140,width=150,height=20)


        #Text Area

        self.lbl_addr = Label(self, text="Address:      ", font=("Arial",15))
        self.lbl_addr.place(x=50,y=170,width=120,height=20)

        self.txt_addr = Text(self)
        self.txt_addr.place(x=160,y=170,width=150,height=80)


        #Salary Details

        def getSalary(event):
            basic = int(self.txt_basic.get())
            da = basic *0.10
            hra = basic * 0.73
            gross = basic + hra + da
            tax = 0.30 * gross
            net = gross - tax
            
            self.txt_da.insert(0,str(da))
            self.txt_hra.insert(0,str(hra))
            self.txt_gross.insert(0,str(gross))
            self.txt_tax.insert(0,str(tax))
            self.txt_net.insert(0,str(net))
            


        self.lbl_basic = Label(self, text="Basic Salary:", font=("Arial",13))
        self.lbl_basic.place(x=40,y=270,width=120,height=20)

        self.txt_basic = Entry(self, width=50)
        self.txt_basic.place(x=160,y=270,width=150,height=20)

        self.txt_basic.bind("<FocusOut>",getSalary)

        


        self.lbl_da = Label(self, text="DA: ", font=("Arial",13))
        self.lbl_da.place(x=100,y=300,width=80,height=20)

        self.txt_da = Entry(self, width=50)
        self.txt_da.place(x=160,y=300,width=150,height=20)


        self.lbl_hra = Label(self, text="HRA:   ", font=("Arial",13))
        self.lbl_hra.place(x=100,y=330,width=80,height=20)

        self.txt_hra = Entry(self, width=50)
        self.txt_hra.place(x=160,y=330,width=150,height=20)


        self.lbl_gross = Label(self, text="Gross Salary:", font=("Arial",13))
        self.lbl_gross.place(x=40,y=360,width=120,height=20)

        self.txt_gross = Entry(self, width=50)
        self.txt_gross.place(x=160,y=360,width=150,height=20)


        self.lbl_tax = Label(self, text="Income Tax:", font=("Arial",13))
        self.lbl_tax.place(x=40,y=390,width=120,height=20)

        self.txt_tax = Entry(self, width=50)
        self.txt_tax.place(x=160,y=390,width=150,height=20)


        self.lbl_net = Label(self, text="Net Salary:", font=("Arial",13))
        self.lbl_net.place(x=40,y=420,width=120,height=20)

        self.txt_net = Entry(self, width=50)
        self.txt_net.place(x=160,y=420,width=150,height=20)

        
        


        #Buttons


        def onNewClicked():
            messagebox.showinfo("Info","You clicked on New")
        
        self.btnNew = Button(self,text="New",command=onNewClicked)
        self.btnNew.place(x=65,y=480,width=100,height=50)
        

        def onSaveClicked():
            messagebox.showinfo("Info","You clicked on Save")
        
        self.btnSave = Button(self,text="Save",command=onSaveClicked)
        self.btnSave.place(x=180,y=480,width=100,height=50)
        

        def onExitClicked():
            self.withdraw()

        self.btnExit = Button(self,text="Exit",command=onExitClicked)
        self.btnExit.place(x=295,y=480,width=100,height=50)

        



if __name__ == "__main__":
    emp_win = Employee()
    emp_win.display()
