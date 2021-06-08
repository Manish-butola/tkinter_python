from tkinter import *
from tkinter import messagebox

def sum():
    a=int(e1.get())
    b=int(e2.get())
    c=a+b
    messagebox.showinfo("Title ","Sum is "+str(c))
    l3.config(text=str(c))
    e3.delete(0,len(e3.get()))
    e3.insert(0,str(c))
    
    

root = Tk()
root.state("zoomed")

l1 = Label(root,text="Enter Number ")
l1.place(x=20,y=20,width=100,height=20)
e1 = Entry(root)
e1.place(x=130,y=20,width=100,height=20)

l2 = Label(root,text="Enter Number ")
l2.place(x=20,y=50,width=100,height=20)
e2 = Entry(root)
e2.place(x=130,y=50,width=100,height=20)

e3 = Entry(root)
e3.place(x=20,y=80,width=100,height=20)
l3 = Label(root,text="Please Wait ...")
l3.place(x=130,y=80,width=100,height=20)

b1 = Button(root,text=" Sum ",command=sum)
b1.place(x=50,y=110,width=100,height=20)

root.mainloop()
