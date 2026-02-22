from functions import (
    load_key,
    verify_master_password,
    load_passwords,
    add_password,
    find_password,
    delete_password
)
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def login_window():
    root=tk.Tk()
    root.title("Login")
    ttk.Label(root,text="Master Password").pack()
    entry=ttk.Entry(root)
    entry.pack()
    def attempt():
        if verify_master_password(entry.get()):
            key=load_key()
            fernet=Fernet(key)
            root.destroy()
            main_window(fernet)
        else:
            messagebox.showerror("Error: incorrect password")
    ttk.Button(root,text="Unlock Vault",command=attempt).pack(pady=5)
    root.mainloop()

def main_window(fernet):
    win=tk.Tk()
    win.title("Password Manager")
    ttk.Label(win,text="Password Manager Main Menu",font=("Segoe UI",20)).pack()
    ttk.Button(win,text="Add password",width=20,command=lambda:add_window(fernet)).pack(pady=5)
    ttk.Button(win,text="Find password",width=20,command=lambda:find_window(fernet)).pack(pady=5)
    ttk.Button(win,text="Delete password",width=20,command=lambda:delete_window(fernet)).pack(pady=5)
    ttk.Button(win,text="Exit app",width=20,command=win.destroy).pack(pady=5)

def add_window(fernet):
    win=tk.Toplevel()
    win.title("Password Manager: add password")
    ttk.Label(win,text="Add Entry",font=("Segoe UI",20)).pack()
    ttk.Label(win,text="Enter the site's name:").pack(pady=5)
    site_entry=ttk.Entry(win)
    site_entry.pack()
    ttk.Label(win,text="Enter the username of the site: ").pack(pady=5)
    user_entry=ttk.Entry(win)
    user_entry.pack()
    ttk.Label(win,text="Enter the password of the site: ").pack(pady=5)
    password_entry=ttk.Entry(win)
    password_entry.pack()
    def submit():
        success=add_password(
            site_entry.get(),
            user_entry.get(),
            password_entry.get(),
            fernet
        )
        if success:
            messagebox.showinfo("Success","Password Added Successfully")
            win.destroy()
        else:
            messagebox.showerror("Error","A password for this site already exists, please delete it first")
    ttk.Button(win,text="Submit",width=20,command=submit).pack(pady=5)
def find_window(fernet):
    win = tk.Toplevel()
    win.title("Password Vault: Find Password")

    ttk.Label(win, text="Search for Password",font=("Segoe UI",20)).pack(pady=5)
    ttk.Label(win, text="Enter website: ").pack(pady=5)
    site_entry = ttk.Entry(win)
    site_entry.pack(pady=5)

    def search():
        website = site_entry.get()
        result = find_password(website, fernet)

        if result is None:
            messagebox.showerror("Not Found", f"No password stored for '{website}'.")
            return

        # Show the decrypted result
        messagebox.showinfo(
            "Password Found",
            f"Website: {result['website']}\n"
            f"Username: {result['username']}\n"
            f"Password: {result['password']}"
        )

    ttk.Button(win, text="Search", command=search).pack(pady=10)


def delete_window(fernet):
    win = tk.Toplevel()
    win.title("Delete Password")

    ttk.Label(win, text="Website",font=("Segoe UI",20)).pack(pady=5)
    site_entry = ttk.Entry(win)
    site_entry.pack(pady=5)

    def submit():
        website = site_entry.get()
        success = delete_password(website)

        if success:
            messagebox.showinfo("Success", f"Password for '{website}' deleted.")
            win.destroy()
        else:
            messagebox.showerror("Error", f"No password found for '{website}'.")

    ttk.Button(win, text="Delete", command=submit).pack(pady=10)

login_window()

