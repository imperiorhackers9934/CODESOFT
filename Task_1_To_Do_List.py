import tkinter as tk
from tkinter import *
from tkinter import messagebox
#Geometry and Configurations
root=tk.Tk()
root.title("To Do List")
root.geometry("400x555")
root.resizable(False,False)
#Data Storage
arr=[]
#Defining Functions of Button
def additem():
    global inp,k
    txt=inp.get()
    if(len(txt)==0 or txt.isspace()):
        messagebox.showerror('Error', 'Entry should not be empty')
        return
    k.insert(0,txt)
    inp.delete(0,END)
def remove_all():
    global k
    try:
        k.delete(0,END)
    except Exception as e:
        messagebox.showerror('Error', 'An Empty List Cannot be Deleted')
    finally:
        pass
def remove_selected():
    global k
    try:
        sltd=k.curselection()
        k.delete(sltd)
    except Exception as e:
        messagebox.showerror('Error', 'Please Select an item to Delete')
    finally:
        pass
def update_sel():
    global inp,k
    try:
        get_txt=inp.get()
        sltd=k.curselection()
        k.delete(sltd)
        k.insert(sltd,get_txt)
        inp.delete(0,END)
    except Exception as e:
        messagebox.showerror('Error', 'Please Select an item to Update')
    finally:
        pass
#Elements of GUI
top=Label(root,text="Tasks to Do")
k=Listbox(root,height=17,width=34,font=("Arial", 15))
b1=Button(root,text="Add Task",command=additem)
b2=Button(root,text="Remove Selected Task",command=remove_selected)
b3=Button(root,text="Clear All Tasks",command=remove_all)
b4=Button(root,text="Update Selected",command=update_sel)
inp=Entry(root,width=62,font=("Arial", 15))
#Packing of Elements
top.pack()
k.pack()
b1.place(x=5,y=470,width=90,height=40)
b2.place(x=95,y=470,width=150,height=40)
b3.place(x=245,y=470,width=150,height=40)
b4.place(x=5,y=510,width=390,height=40)
inp.place(x=5,y=440,width=390)
root.mainloop()