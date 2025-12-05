import os
import re
import tkinter as tk
from tkinter import messagebox, filedialog

class User:
    def __init__(self, name):
        self.name = name.strip()


class Post:
    def __init__(self, user, title, content):
        self.user = user
        self.title = title.strip()
        self.content = content.strip()

    def get_filename(self):
        safe_name = re.sub(r'[^A-Za-z0-9_]', "_", self.user.name)
        safe_title = re.sub(r'[^A-Za-z0-9_]', "_", self.title)
        return f"{safe_name}_{safe_title}.txt"

    def save_to_file(self, directory="posts"):
        if not os.path.exists(directory):
            os.makedirs(directory)
        filepath = os.path.join(directory, self.get_filename())
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Author: {self.user.name}\n")
                f.write(f"Title: {self.title}\n\n")
                f.write(self.content)
            return filepath
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save post: {e}")
            return None


class MiniBlogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog - Simple Blogging App")
        self.root.geometry("600x500")

        self.posts_dir = "posts"

        tk.Label(root, text="Your Name:").pack(anchor="w", padx=10, pady=5)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(padx=10, pady=5)

        tk.Label(root, text="Post Title:").pack(anchor="w", padx=10, pady=5)
        self.title_entry = tk.Entry(root, width=50)
        self.title_entry.pack(padx=10, pady=5)

        tk.Label(root, text="Post Content:").pack(anchor="w", padx=10, pady=5)
        self.content_text = tk.Text(root, height=8, width=60)
        self.content_text.pack(padx=10, pady=5)

        tk.Button(root, text="Save Post", command=self.save_post).pack(pady=5)

        tk.Label(root, text="Saved Posts:").pack(anchor="w", padx=10, pady=5)
        self.post_listbox = tk.Listbox(root, width=50, height=8)
        self.post_listbox.pack(padx=10, pady=5)
        self.post_listbox.bind("<<ListboxSelect>>", self.load_post)

        self.view_content = tk.Text(root, height=8, width=60, state="disabled")
        self.view_content.pack(padx=10, pady=5)

        tk.Button(root, text="Refresh List", command=self.load_post_list).pack(pady=5)
        tk.Button(root, text="Delete Post", command=self.delete_post).pack(pady=5)

        self.load_post_list()

    def save_post(self):
        name = self.name_entry.get().strip()
        title = self.title_entry.get().strip()
        content = self.content_text.get("1.0", tk.END).strip()

        if not name or not title or not content:
            messagebox.showwarning("Warning", "All fields must be filled!")
            return

        user = User(name)
        post = Post(user, title, content)
        filepath = post.save_to_file(self.posts_dir)

        if filepath:
            messagebox.showinfo("Success", f"Post saved as {filepath}")
            self.load_post_list()
            self.title_entry.delete(0, tk.END)
            self.content_text.delete("1.0", tk.END)

    def load_post_list(self):
        self.post_listbox.delete(0, tk.END)
        if not os.path.exists(self.posts_dir):
            return
        for file in os.listdir(self.posts_dir):
            if file.endswith(".txt"):
                self.post_listbox.insert(tk.END, file)

    def load_post(self, event):
        selection = self.post_listbox.curselection()
        if not selection:
            return
        filename = self.post_listbox.get(selection[0])
        filepath = os.path.join(self.posts_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.view_content.config(state="normal")
            self.view_content.delete("1.0", tk.END)
            self.view_content.insert(tk.END, content)
            self.view_content.config(state="disabled")
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not load post: {e}")

    def delete_post(self):
        selection = self.post_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Select a post to delete")
            return
        filename = self.post_listbox.get(selection[0])
        filepath = os.path.join(self.posts_dir, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            self.load_post_list()
            self.view_content.config(state="normal")
            self.view_content.delete("1.0", tk.END)
            self.view_content.config(state="disabled")
            messagebox.showinfo("Deleted", f"{filename} removed.")


if __name__ == "__main__":
    root = tk.Tk()
    app = MiniBlogApp(root)
    root.mainloop()
