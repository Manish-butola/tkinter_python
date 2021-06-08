from tkinter import *

root = Tk()
root.state("zoomed")

def showFrame(fr):
    fr.tkraise()

frame1 = Frame(root,bg="red")
frame1.place(x=20,y=20,width=500,height=500)

frame2 = Frame(root,bg="green")
frame2.place(x=20,y=20,width=500,height=500)


b1=Button(frame1,text="Click Me",command=lambda:showFrame(frame2))
b1.pack()

b2=Button(frame2,text="Click Me",command=lambda:showFrame(frame1))
b2.pack()

root.mainloop()
