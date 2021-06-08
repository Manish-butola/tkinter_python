from tkinter import *
from tkinter import messagebox


def sumee():
    a = int(e1.get())
    b = int(e2.get())
    c = a + b
    messagebox.showinfo("Title ", "Sum is " + str(c))
    l3.config(text=str(c))
    e3.delete(0, len(e3.get()))
    e3.insert(0, str(c))


root = Tk()
root.geometry("500x500")

l1 = Label(root, text="Enter Number ")
l1.pack()
e1 = Entry(root)
e1.pack()
l2 = Label(root, text="Enter Number ")
l2.pack()
e2 = Entry(root)
e2.pack()

e3 = Entry(root)
e3.pack()
l3 = Label(root, text="Please Wait ...");
l3.pack()

b1 = Button(root, text=" Sum ", command=sumee())
b1.pack()

root.mainloop()
