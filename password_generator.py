import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showwarning("Invalid Input", "Password length must be greater than 0")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
window = tk.Tk()
window.title("🔐 Password Generator")
window.geometry("400x250")
window.resizable(False, False)

tk.Label(window, text="Password Length:", font=("Arial", 12)).pack(pady=10)

length_var = tk.IntVar(value=12)
tk.Entry(window, textvariable=length_var, width=10, font=("Arial", 12)).pack()

tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=15)

result_var = tk.StringVar()
tk.Entry(window, textvariable=result_var, width=30, font=("Arial", 12)).pack()

tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=10)

window.mainloop()
