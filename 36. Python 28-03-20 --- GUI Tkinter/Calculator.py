#Simple Calculator GUI Program using Tkinter

from tkinter import *
from tkinter import messagebox

class MyWindow(Tk):
    def __init__(self, title="My Window"):
        super().__init__()
        self.geometry("500x350")
        self.title = title

    def onAddClicked(self):
        v1 = int(self.txt_value1.get())
        v2 = int(self.txt_value2.get())
        res = v1 + v2
        messagebox.showinfo("ADDITION","Sum is: "+str(res))
    
    def onDiffClicked(self):
        v1 = int(self.txt_value1.get())
        v2 = int(self.txt_value2.get())
        res = v1 - v2
        messagebox.showinfo("SUBTRACTION","Difference is: "+str(res))

    def onMulClicked(self):
        v1 = int(self.txt_value1.get())
        v2 = int(self.txt_value2.get())
        res = v1 * v2
        messagebox.showinfo("MULTIPLICATION","Product is: "+str(res))

    def onDivClicked(self):
        v1 = int(self.txt_value1.get())
        v2 = int(self.txt_value2.get())
        res = v1 / v2
        messagebox.showinfo("DIVISION","Quotient is: "+str(res))

    def onClearClicked(self):
        first=0
        last1=len(self.txt_value1.get())
        last2=len(self.txt_value2.get())
        self.txt_value1.delete(first,last1)
        self.txt_value2.delete(first,last2)

    def onExitClicked(self):
        self.withdraw()
        
        

    def display(self):
        self.lbl_heading = Label(self, text="CALCULATOR", font=("Arial Bold",28))
        self.lbl_heading.place(x=100,y=10,width=300,height=90)

        self.lbl_value1 = Label(self, text="Value 1:", font=("Arial",15))
        self.lbl_value1.place(x=80,y=110,width=100,height=20)

        self.txt_value1 = Entry(self, width=50)
        self.txt_value1.place(x=200,y=110,width=150,height=20)

        self.lbl_value2 = Label(self, text="Value 2:", font=("Arial",15))
        self.lbl_value2.place(x=80,y=140,width=100,height=20)

        self.txt_value2 = Entry(self, width=50)
        self.txt_value2.place(x=200,y=140,width=150,height=20)

        self.btnAdd = Button(self,text="ADD",command=self.onAddClicked)
        self.btnAdd.place(x=80,y=180,width=80,height=50)

        self.btnDiff = Button(self,text="DIFFERENCE",command=self.onDiffClicked)
        self.btnDiff.place(x=170,y=180,width=80,height=50)

        self.btnMul = Button(self,text="MULTIPLY",command=self.onMulClicked)
        self.btnMul.place(x=260,y=180,width=80,height=50)

        self.btnDiv = Button(self,text="DIVIDE",command=self.onDivClicked)
        self.btnDiv.place(x=350,y=180,width=80,height=50)

        self.btnExit = Button(self,text="EXIT",command=self.onExitClicked)
        self.btnExit.place(x=170,y=250,width=80,height=50)

        self.btnClear = Button(self,text="CLEAR ALL",command=self.onClearClicked)
        self.btnClear.place(x=260,y=250,width=80,height=50)

        

if __name__ == "__main__":
    win = MyWindow()
    win.display()
