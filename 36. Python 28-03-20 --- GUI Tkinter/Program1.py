# Program to demonstrate how to create a GUI Window using Tkinter module in Python

from tkinter import *

class MyWindow(Tk):

    def __init__(self,title='My window'):
        super().__init__()
        self.geometry('600x600')
        self.title(title)

        self.lbl = Label(self,text='Hello world',font=('Arial Bold',48))
        self.lbl.place(x=60,y=180,width=450,height=200)
                                                           

if __name__ == "__main__":
	win1 = MyWindow('GUI demo')







