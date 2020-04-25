#Program to demonstrate the use of various GUI components using Tkinter
'''
1. Label
2. Button
3. TextBox
4. TextArea
5. CheckBox
6. Radio button
'''

from tkinter import *
from tkinter import messagebox

class StudentDetails(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x700")
        self.title("Student Information")

    def display(self):
        self.lbl_heading = Label(self, text="Student Details", font=("Arial Bold",28))
        self.lbl_heading.place(x=70,y=10,width=300,height=90)

        self.lbl_name = Label(self, text="Name:   ", font=("Arial",15))
        self.lbl_name.place(x=50,y=110,width=100,height=20)

        self.txt_name = Entry(self, width=50)
        self.txt_name.place(x=160,y=110,width=150,height=20)

        self.lbl_usn = Label(self, text="USN:    ", font=("Arial",15))
        self.lbl_usn.place(x=50,y=140,width=100,height=20)

        self.txt_usn = Entry(self, width=50)
        self.txt_usn.place(x=160,y=140,width=150,height=20)



        #TextArea

        self.lbl_addr = Label(self, text="Address:", font=("Arial",15))
        self.lbl_addr.place(x=50,y=170,width=100,height=20)

        self.txt_addr = Text(self)
        self.txt_addr.place(x=160,y=170,width=150,height=80)


        

        #RadioButtons

        self.lbl_sex = Label(self, text="Sex:    ", font=("Arial",15))
        self.lbl_sex.place(x=50,y=260,width=100,height=20)


        self.sexvar = IntVar()

        def displaySex():
            st = ""
            if self.sexvar.get() == 1:
                st = "Male"
            elif self.sexvar.get() == 2:
                st = "Female"
            messagebox.showinfo("Info",st+" selected")

        self.male = Radiobutton(self,text="MALE",variable=self.sexvar,value=1,command=displaySex)
        self.male.place(x=160,y=260,width=100,height=30)

        self.female = Radiobutton(self,text="FEMALE",variable=self.sexvar,value=2,command=displaySex)
        self.female.place(x=270,y=260,width=100,height=30)
        



        self.lbl_clg = Label(self, text="College:", font=("Arial",15))
        self.lbl_clg.place(x=50,y=300,width=100,height=23)

        self.colvar = IntVar()

        def displayCollege():
            st = ""
            if self.colvar.get() == 1:
                st = "BVB college"
            elif self.colvar.get() == 2:
                st = "KLE college"
            elif self.colvar.get() == 3:
                st = "SDM college"
            messagebox.showinfo("Info",st+" selected")

        self.colbvb = Radiobutton(self,text="BVB college",variable=self.colvar,value=1,command=displayCollege)
        self.colbvb.place(x=50,y=330,width=100,height=30)

        self.colkle = Radiobutton(self,text="KLE college",variable=self.colvar,value=2,command=displayCollege)
        self.colkle.place(x=170,y=330,width=100,height=30)

        self.colsdm = Radiobutton(self,text="SDM college",variable=self.colvar,value=3,command=displayCollege)
        self.colsdm.place(x=290,y=330,width=100,height=30)
        


        #CheckBoxs

        self.lbl_edu = Label(self, text="Education:", font=("Arial",15))
        self.lbl_edu.place(x=50,y=370,width=100,height=20)
        

        self.sslc = IntVar()

        def displayPercentage():
            if self.sslc.get()==1:
                self.lbl_per = Label(self, text="Percentage:", font=("Arial",12))
                self.lbl_per.place(x=160,y=400,width=80,height=23)
                self.txt_per = Entry(self, width=50)
                self.txt_per.place(x=250,y=400,width=150,height=20)

        self.cb_sslc = Checkbutton(self,variable=self.sslc,onvalue=1,offvalue=0,text="SSLC",command=displayPercentage)
        self.cb_sslc.place(x=50,y=400,width=100,height=30)

       

        self.puc = IntVar()

        def displayPercentage():
            if self.puc.get()==1:
                self.lbl_per = Label(self, text="Percentage:", font=("Arial",12))
                self.lbl_per.place(x=160,y=450,width=80,height=23)
                self.txt_per = Entry(self, width=50)
                self.txt_per.place(x=250,y=450,width=150,height=20)

        self.cb_puc = Checkbutton(self,variable=self.puc,onvalue=1,offvalue=0,text="PUC",command=displayPercentage)
        self.cb_puc.place(x=50,y=450,width=100,height=30)

        

        self.ug = IntVar()

        def displayPercentage():
            if self.ug.get()==1:
                self.lbl_per = Label(self, text="Percentage:", font=("Arial",12))
                self.lbl_per.place(x=160,y=500,width=80,height=23)
                self.txt_per = Entry(self, width=50)
                self.txt_per.place(x=250,y=500,width=150,height=20)

        self.cb_ug = Checkbutton(self,variable=self.ug,onvalue=1,offvalue=0,text="UG",command=displayPercentage)
        self.cb_ug.place(x=50,y=500,width=100,height=30)

        

        self.pg = IntVar()

        def displayPercentage():
            if self.pg.get()==1:
                self.lbl_per = Label(self, text="Percentage:", font=("Arial",12))
                self.lbl_per.place(x=160,y=550,width=80,height=23)
                self.txt_per = Entry(self, width=50)
                self.txt_per.place(x=250,y=550,width=150,height=20)

        self.cb_pg = Checkbutton(self,variable=self.pg,onvalue=1,offvalue=0,text="PG",command=displayPercentage)
        self.cb_pg.place(x=50,y=550,width=100,height=30)




        #Buttons

        def onOkClicked():
            messagebox.showinfo("Info","Thank you for entering the details :"+self.txt_name.get())
        
        self.btnOk = Button(self,text="OK",command=onOkClicked)
        self.btnOk.place(x=110,y=600,width=100,height=50)

        def onExitClicked():
            self.withdraw()

        self.btnExit = Button(self,text="Exit",command=onExitClicked)
        self.btnExit.place(x=230,y=600,width=100,height=50)

        



if __name__ == "__main__":
    stud_win = StudentDetails()
    stud_win.display()
