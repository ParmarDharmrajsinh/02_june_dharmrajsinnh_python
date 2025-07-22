import tkinter

window=tkinter.Tk()
window.title("My First GUI")  
window.geometry("150x250") 
window.config(bg="lightblue")
"""
tkinter.Label(text="firstname:").place(x=0, y=0)
tkinter.Label(text="lastname:").place(x=0, y=30)

tkinter.Label(text="firstname:",bg='lightblue',fg='orange',font='dubai 15 bold').grid(row=0, column=0)
tkinter.Label(text="lastname:",bg='lightblue',fg='yellow', font='elephant 25').grid(row=1, column=0)

tkinter.Entry().grid(row=0, column=1)
tkinter.Entry().grid(row=1, column=1)"""
tkinter.Label(text="Enter first number:",font="Elephant 50").grid(row=0,column=0)
tkinter.Label(text="Enter second number:",font="Elephant 50").grid(row=1,column=0)
fn=tkinter.Entry(font="Elephant 50")
fn.grid(row=0,column=1)
sn=tkinter.Entry(font="Elephant 50")
sn.grid(row=1,column=1)
def add():
    print("Addition:",int(fn.get())+int(sn.get()))
    
def sub():
    print("Subtraction:",int(fn.get())-int(sn.get()))
    
def mul():
    print("Multiplication:",int(fn.get())*int(sn.get()))
    
def div():
    print("Division:",int(fn.get())/int(sn.get()))

tkinter.Button(text="+",command=add,font="Elephant 50").grid(row=2,column=0)
tkinter.Button(text="-",command=sub,font="Elephant 50").grid(row=3,column=0)
tkinter.Button(text="*",command=mul,font="Elephant 50").grid(row=4,column=0)
tkinter.Button(text="/",command=div,font="Elephant 50").grid(row=5,column=0)


window.mainloop()

window=tkinter.Tk()
window.title("My First GUI")  
window.geometry("150x250") 
window.config(bg="lightblue")
"""
tkinter.Label(text="firstname:").place(x=0, y=0)
tkinter.Label(text="lastname:").place(x=0, y=30)

tkinter.Label(text="firstname:",bg='lightblue',fg='orange',font='dubai 15 bold').grid(row=0, column=0)
tkinter.Label(text="lastname:",bg='lightblue',fg='yellow', font='elephant 25').grid(row=1, column=0)

tkinter.Entry().grid(row=0, column=1)
tkinter.Entry().grid(row=1, column=1)"""
tkinter.Label(text="Enter first number:",font="Elephant 10").grid(row=0,column=0)
tkinter.Label(text="Enter second number:",font="Elephant 10").grid(row=1,column=0)
fn=tkinter.Entry(font="Elephant 10")
fn.grid(row=0,column=1)
sn=tkinter.Entry(font="Elephant 10")
sn.grid(row=1,column=1)
def add():
    print("Addition:",int(fn.get())+int(sn.get()))
    
def sub():
    print("Subtraction:",int(fn.get())-int(sn.get()))
    
def mul():
    print("Multiplication:",int(fn.get())*int(sn.get()))
    
def div():
    print("Division:",int(fn.get())/int(sn.get()))

tkinter.Button(text="+",command=add,font="Elephant 10").grid(row=2,column=0)
tkinter.Button(text="-",command=sub,font="Elephant 10").grid(row=3,column=0)
tkinter.Button(text="*",command=mul,font="Elephant 10").grid(row=4,column=0)
tkinter.Button(text="/",command=div,font="Elephant 10").grid(row=5,column=0)


window.mainloop()