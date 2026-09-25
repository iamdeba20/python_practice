from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("flower classification")
Label(root,text="sepal length").grid(row=0,column=0)
entry1=Entry(root)
entry1.grid(row=0,column=1)
Label(root,text="petal length").grid(row=2,column=0)
entry2=Entry(root)
entry2.grid(row=2,column=1)
def show_message():
    messagebox.showinfo("message","button clicked")

btn=Button(root,text="click me",command="show message")
btn.grid(row=2,column=2)
root.geometry("400x300")
root.mainloop()