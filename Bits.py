import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Dummy credentials for demonstration
VALID_USERNAME = "student"
VALID_PASSWORD = "bits123"

# Login check function
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Main window
root = tk.Tk()
root.title("BITS Pilani Student Login Portal")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="white")

# Load and display logo (Make sure 'bits_logo.png' is in the same directory)
try:
    logo_img = Image.open("bits_logo.png")
    logo_img = logo_img.resize((150, 150), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo, bg="white")
    logo_label.pack(pady=20)
except Exception as e:
    tk.Label(root, text="BITS PILANI", font=("Arial", 20, "bold"), bg="white").pack(pady=30)
    print("Logo not found or error loading image:", e)

# Login form
tk.Label(root, text="Username", font=("Arial", 12), bg="white").pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

tk.Label(root, text="Password", font=("Arial", 12), bg="white").pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", font=("Arial", 12), command=login, bg="#0066cc", fg="white").pack(pady=20)

tk.Label(root, text="© BITS Pilani 2025", font=("Arial", 10), bg="white", fg="gray").pack(side="bottom", pady=10)

root.mainloop()
