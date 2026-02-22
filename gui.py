from functions import (
    load_key,
    verify_master_password,
    load_passwords,
    add_password,
    find_password,
    delete_password
)
from cryptography.fernet import Fernet
import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
FONT_FAMILY="Segoe UI"
def Label(parent, text="", font=None, **kwargs):
    if font is None:
        font = (FONT_FAMILY, 15)
    return ctk.CTkLabel(parent, text=text, font=font, **kwargs)

def Button(parent, text="", command=None, **kwargs):
    return ctk.CTkButton(parent, text=text, command=command, font=(FONT_FAMILY, 15), **kwargs)

def Entry(parent, **kwargs):
    return ctk.CTkEntry(parent, font=(FONT_FAMILY, 15), **kwargs)



def login_window(root):
    login = ctk.CTkToplevel()
    login.title("Login")
    login.geometry("350x250")
    login.lift()
    login.focus_force()
    login.grab_set()

    Label(login, text="Master Password").pack()
    entry = Entry(login, show="*")
    entry.pack()

    def attempt():
        if verify_master_password(entry.get()):
            key = load_key()
            fernet = Fernet(key)

            login.destroy()      # close login window
            root.deiconify()     # show main window
            main_window(fernet, root)
        else:
            messagebox.showerror("Error", "Incorrect password")

    Button(login, text="Unlock Vault", command=attempt).pack(pady=5)

def main_window(fernet,root):
    win=root
    win.title("Password Manager")
    Label(win,text="Password Manager Main Menu",font=("Inter",20)).pack()
    Button(win,text="Add password",width=170,command=lambda:add_window(fernet)).pack(pady=5)
    Button(win,text="Find password",width=170,command=lambda:find_window(fernet)).pack(pady=5)
    Button(win,text="Delete password",width=170,command=lambda:delete_window(fernet)).pack(pady=5)
    Button(win,text="Exit app",width=170,command=win.destroy).pack(pady=5)

def add_window(fernet):
    win=ctk.CTkToplevel()
    win.title("Password Manager: add password")
    win.lift()
    win.focus_force()
    win.grab_set()

    Label(win,text="Add Entry",font=("Inter",20)).pack()
    Label(win,text="Enter the site's name:").pack(pady=5)
    site_entry=Entry(win)
    site_entry.pack()
    Label(win,text="Enter the username of the site: ").pack(pady=5)
    user_entry=Entry(win)
    user_entry.pack()
    Label(win,text="Enter the password of the site: ").pack(pady=5)
    password_entry=Entry(win)
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
    Button(win,text="Submit",width=170,command=submit).pack(pady=5)
def find_window(fernet):
    win = ctk.CTkToplevel()
    win.title("Password Vault: Find Password")
    win.lift()
    win.focus_force()
    win.grab_set()
    Label(win, text="Search for Password",font=("Inter",20)).pack(pady=5)
    Label(win, text="Enter website: ").pack(pady=5)
    site_entry = Entry(win)
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

    Button(win, text="Search", command=search).pack(pady=10)


def delete_window(fernet):
    win.lift()
    win.focus_force()
    win.grab_set()
    win = ctk.CTkToplevel()
    win.title("Delete Password")

    Label(win, text="Website",font=("Inter",20)).pack(pady=5)
    site_entry = Entry(win)
    site_entry.pack(pady=5)

    def submit():
        website = site_entry.get()
        success = delete_password(website)

        if success:
            messagebox.showinfo("Success", f"Password for '{website}' deleted.")
            win.destroy()
        else:
            messagebox.showerror("Error", f"No password found for '{website}'.")

    Button(win, text="Delete", command=submit).pack(pady=10)

root = ctk.CTk()
root.withdraw()
login_window(root)       # pass root into login window
root.mainloop()          # only ONE mainloop

