import tkinter as tk
from tkinter import messagebox, filedialog
import os
import subprocess 


class MenuBarApp:
    def __init__(self, root): 
        self.root = root
        self.root.title("@parmar dharmrajsinh")
        self.root.geometry("600x400")
        

        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

    
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        
        self.apps_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Apps", menu=self.apps_menu)
        self.apps_menu.add_command(label="Calculator", command=self.open_calculator)
        self.apps_menu.add_command(label="Notepad", command=self.open_notepad)
        self.apps_menu.add_command(label="Google Chrome", command=self.open_chrome)

        
        self.menubar.add_command(label="About", command=self.show_about)
        self.menubar.add_command(label="Contact", command=self.show_contact)

        
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill="both")

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("MenuBar Application - New File")

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.root.title(f"MenuBar Application - {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.root.title(f"MenuBar Application - {os.path.basename(file_path)}")
                messagebox.showinfo("Success", "File saved successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()

    def open_calculator(self):
        try:
            if os.name == "nt":  
                subprocess.Popen("calc.exe")
            elif os.name == "posix":  
                subprocess.Popen(["gnome-calculator"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Calculator: {e}")

    def open_notepad(self):
        try:
            if os.name == "nt": 
                subprocess.Popen("notepad.exe")
            elif os.name == "posix":  
                subprocess.Popen(["gedit"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Notepad: {e}")

    def open_chrome(self):
        try:
            if os.name == "nt": 
                subprocess.Popen(["start", "chrome"], shell=True)
            elif os.name == "posix":  
                subprocess.Popen(["google-chrome"])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Google Chrome: {e}")

    def show_about(self):
        messagebox.showinfo("About", "MenuBar Application\nVersion 1.0\nCreated with Tkinter")

    def show_contact(self):
        messagebox.showinfo("Contact", "For support, contact:parmardharmrajsinh99@gmail.com")


if __name__ == "__main__":
    root = tk.Tk()
    app = MenuBarApp(root)
    root.mainloop()

# module_oop-3/task_tkinter.py




