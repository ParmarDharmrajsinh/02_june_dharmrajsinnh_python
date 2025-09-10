import tkinter

window=tkinter.Tk()
window.title("myapp")
window.geometry("400x300")
window.config(bg="lightblue")

"""tkinter.Label(text="first name").pack()
tkinter.Label(text=" first name ").place(x=10, y=50)"""

tkinter.Label(text="last name").grid(row=1, column=0)
tkinter.Label(text="last name").grid(row=3, column=0)
tkinter.Label(text="email").grid(row=2, column=0)
tkinter.Entry().grid(row=1, column=1)
tkinter.Entry().grid(row=2, column=1)
tkinter.Entry().grid(row=3, column=1)
tkinter.Button(text="submit").grid(row=4, column=1) 

tkinter.Checkbutton(text="I agree").grid(row=5, column=1)
tkinter.Radiobutton()







window.mainloop()



