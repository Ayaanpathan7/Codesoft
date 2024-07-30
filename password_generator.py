import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_var.get())
    if length < 1:
        messagebox.showerror("Invalid Input", "Password length should be greater than 0")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg='#2c3e50')

# Create StringVar to hold the password and length
password_var = tk.StringVar()
length_var = tk.StringVar(value='12')

# Create and place the widgets with styles
tk.Label(root, text="Password Length:", bg='#2c3e50', fg='white',font=()).grid(row=0, column=0, pady=5, padx=5, sticky='e')
tk.Entry(root, textvariable=length_var, bg='#34495e', fg='white', insertbackground='white').grid(row=0, column=1, pady=5, padx=5)
tk.Button(root, text="Generate Password", command=generate_password, bg='#e74c3c', fg='white', activebackground='#c0392b', activeforeground='white').grid(row=1, column=1,columnspan=2, pady=10, padx=5)
tk.Entry(root, textvariable=password_var, state='readonly', bg='#34495e', fg='black').grid(row=2, column=1, columnspan=3, pady=5, padx=5)
tk.Button(root, text="Copy", command=copy_to_clipboard, bg='#3498db', fg='white', activebackground='#2980b9', activeforeground='white').grid(row=3, column=1,columnspan=4,pady=10, padx=5)


# Start the Tkinter event loop
root.mainloop()

