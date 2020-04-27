# Tkinter GUI Program to demonstrate how to implement Menubars


from tkinter import *
from tkinter import messagebox

class Menubar(Tk):
    def __init__(self,title="Demo Window"):
        super().__init__()
        self.geometry("300x300")
        self.title(title)

        
    def displayComponents(self):
        self.menubar = Menu(self)
        self.configure(menu=self.menubar)

        def onNewClicked():
            messagebox.showinfo("New","You clicked on New")

        def onOpenClicked():
            messagebox.showinfo("Open","You clicked on Open")

        def onSaveClicked():
            messagebox.showinfo("Save","You clicked on Save")

        def onCopyClicked():
            messagebox.showinfo("Copy","You clicked on Copy")

        def onCutClicked():
            messagebox.showinfo("Cut","You clicked on Cut")

        def onPasteClicked():
            messagebox.showinfo("Paste","You clicked on Paste")

        def onFindClicked():
            messagebox.showinfo("Find","You clicked on Find")

        def onReplaceClicked():
            messagebox.showinfo("Replace","You clicked on Replace")

        def onFormatClicked():
            messagebox.showinfo("Format","You clicked on Format")

        #File Menu
		    
        self.menuFile = Menu(self.menubar,tearoff=0)
        self.menuFile.add_command(label="New",command=onNewClicked)
        self.menuFile.add_command(label="Open",command=onOpenClicked)
        self.menuFile.add_command(label="Save",command=onSaveClicked)
        self.menuFile.add_separator()
        self.menuFile.add_command(label="Exit",command=self.withdraw)

        self.menubar.add_cascade(label="File",menu=self.menuFile)

        #Edit Menu
		
        self.menuEdit = Menu(self.menubar,tearoff=0)
        self.menuEdit.add_command(label="Copy",command=onCopyClicked)
        self.menuEdit.add_command(label="Cut",command=onCutClicked)
        self.menuEdit.add_command(label="Paste",command=onPasteClicked)

        self.menubar.add_cascade(label="Edit",menu=self.menuEdit)

        #Tools Menu

        self.menuTools = Menu(self.menubar,tearoff=0)
        self.menuTools.add_command(label="Find",command=onFindClicked)
        self.menuTools.add_command(label="Replace",command=onReplaceClicked)
        self.menuTools.add_command(label="Format",command=onFormatClicked)

        self.menubar.add_cascade(label="Tools",menu=self.menuTools)

   


if __name__ == "__main__":
	win = Menubar("Menubar Demo")
	win.displayComponents()
