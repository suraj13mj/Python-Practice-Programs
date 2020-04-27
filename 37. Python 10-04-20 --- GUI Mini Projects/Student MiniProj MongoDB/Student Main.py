#Program to demonstrate the use of various GUI components using Tkinter


from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from Bean_Student import *
import StudentDB


class StudentWindow(Tk):
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

        self.lbl_roll = Label(self, text="Roll No:", font=("Arial",15))
        self.lbl_roll.place(x=50,y=140,width=100,height=20)

        self.txt_roll = Entry(self, width=50)
        self.txt_roll.place(x=160,y=140,width=150,height=20)


        #Text Area

        self.lbl_addr = Label(self, text="Address:", font=("Arial",15))
        self.lbl_addr.place(x=50,y=170,width=100,height=20)

        self.txt_addr = Text(self)
        self.txt_addr.place(x=160,y=170,width=150,height=80)

        
        #Radio Button

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



        #Combo Box
        
        self.lbl_clg = Label(self, text="College:", font=("Arial",15))
        self.lbl_clg.place(x=50,y=300,width=100,height=23)

        self.cmb_college = ttk.Combobox(self)
        self.cmb_college.place(x=160,y=300,width=100,height=30)

        items = ['KLEIT','BVB','SDM','AGMR','RVCE','MSRIT','PES','IIT-D']
        self.cmb_college['values'] = items
        self.cmb_college.current(0)
        


        self.lbl_branch = Label(self,text="Branch :",font=("Arial",15))
        self.lbl_branch.place(x=50,y=360,width=100,height=23)

        self.cmb_branch = ttk.Combobox(self)
        self.cmb_branch.place(x=160,y=360,width=100,height=30)

        items = ('CSE','ECE','EEE','Mech','Civil','ISE','Telecom','Robotics','Aerospace')
        self.cmb_branch['values'] = items
        self.cmb_branch.current(0)


        

        #Check Box
        

        self.sub = IntVar()

        def displaySub():
            if self.sub.get()==1:
                messagebox.showinfo("Subscription : ","Subscribed to Newsletter!!")
                

        self.cb_sub = Checkbutton(self,variable=self.sub,onvalue=1,offvalue=0,text="Subscribe to daily newsletter for Student Placement News",command=displaySub)
        self.cb_sub.place(x=20,y=420,width=400,height=30)


        #Buttons


        def onNewClicked():
            self.txt_name.delete(0,len(self.txt_name.get()))
            self.txt_roll.delete(0,len(self.txt_roll.get()))
            self.txt_addr.delete("1.0","end-1c")
            self.cmb_college.clearselection()
                
        
        self.btnNew = Button(self,text="New",command=onNewClicked)
        self.btnNew.place(x=65,y=460,width=100,height=50)

        

        def onSaveClicked():
        	stud = Student()
        	stud.Name = self.txt_name.get()
        	stud.Rollno = int(self.txt_roll.get())
        	stud.Address = self.txt_addr.get("1.0","end-1c")
        	stud.College = self.cmb_college.get()
        	stud.Branch = self.cmb_branch.get()
        	if self.sexvar.get() == 1:
        		stud.Sex = "MALE"
        	else:
        		stud.Sex = "FEMALE"
        	stud.News = self.sub.get()

        	res = StudentDB.insertStudent(stud)
        	if res:
        		messagebox.showinfo("Save","Student Record saved successfully..!!")
        	else:
        		messagebox.showinfo("Save","Error saving Student Record!!")

        
        self.btnSave = Button(self,text="Save",command=onSaveClicked)
        self.btnSave.place(x=180,y=460,width=100,height=50)
        
        

        def onExitClicked():
            self.withdraw()

        self.btnExit = Button(self,text="Exit",command=onExitClicked)
        self.btnExit.place(x=295,y=460,width=100,height=50)

        



if __name__ == "__main__":
    stud_win = StudentWindow()
    stud_win.display()
