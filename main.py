from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
Root = Tk()
Var = StringVar()
def Add():
    TextBox.delete("1.0", END)
def Save():
    File_name = fd.asksaveasfilename()
    File = open(File_name, "w")
    File.write(TextBox.get("1.0", END))
    File.close()
def Open():
    File_Name = fd.askopenfilename()
    File = open(File_Name, "r")
    for i in File:
        print(i)
    File.close()
def Help():
    messagebox.showinfo("About us", "This is a custom notepad where you can write and save files")
MenuBar = Menu(Root)
FileMenu = Menu(MenuBar, tearoff=0)
HelpMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label="New", command=Add)
FileMenu.add_command(label="Save", command=Save)
FileMenu.add_command(label="Open", command=Open)
FileMenu.add_command(label="Exit", command=exit)
MenuBar.add_cascade(label="File", menu=FileMenu)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="About", command=Help)
TextBox = Text(Root)
TextBox.pack()
Root.config(menu=MenuBar)
Root.mainloop()
