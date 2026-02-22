# 🔐 Password Manager

A secure, modern password manager built with **Python**, **CustomTkinter**, and **Fernet encryption**. This application provides a clean GUI for storing, retrieving, and deleting passwords, all protected by a master password and encrypted vault.

---

## ✨ Features

### 🔑 Master Password Protection
- Secure login screen  
- Master password stored as a hashed value  
- Prevents unauthorized access to the vault  

### 🔒 Strong Encryption
- Uses **Fernet (AES‑128)** symmetric encryption  
- All passwords stored in encrypted form  
- Encryption key stored separately for safety  

### 🖥️ Modern GUI
- Built with **CustomTkinter**  
- Dark mode enabled  
- Clean, consistent UI with Segoe UI / Inter fonts  
- Custom window icons supported  

### 📁 Vault Operations
- **Add Password** → Save website, username, and password  
- **Find Password** → Search and decrypt entries instantly  
- **Delete Password** → Remove entries securely  
- All operations use the same encryption key  

---

## 📦 Installation

### 1. Clone the repository
git clone https://github.com/yourname/password-manager.git  
cd password-manager

### 2. Install dependencies
pip install customtkinter cryptography

### 3. Setup (Run this only once)
python init.py

### 4. Run
python gui.py

---

## 📁 Project Structure

password-manager/  
├── gui.py — Main GUI application  
├── functions.py — Encryption + vault logic  
├── init.py — First-time setup (creates key + master hash)  
├── key.key — Fernet encryption key (auto-generated)  
├── master.hash — Hashed master password  
├── vault.csv / json — Encrypted password storage  
├── icon.ico — App icon  
└── README.md

> ⚠️ **Important:**  
> `key.key`, `master.hash`, and your vault file **must NOT be committed to Git**. Add them to `.gitignore` to protect your personal data.

---

## 🔧 How It Works

### Login Flow
1. User enters master password  
2. Password is hashed and compared to `master.hash`  
3. If correct → load encryption key → open main window  
4. If incorrect → show error message  

### Adding a Password
- User enters website, username, password  
- Password is encrypted using Fernet  
- Entry is saved to the vault file  

### Finding a Password
- User enters website  
- App searches vault  
- If found → decrypts password → displays it  

### Deleting a Password
- Removes the entry from the vault file  

---

## 🔐 Security Details

- Encryption: **Fernet (AES‑128 + HMAC‑SHA256)**  
- Vault cannot be decrypted without the original key  
- Master password is hashed (never stored in plaintext)  
- Vault entries are encrypted individually  

---

## 🚀 Future Improvements

- Password generator  
- Clipboard auto‑copy  
- Export/import encrypted vault  
- Multi‑vault support  
- Windows Hello biometric unlock  
- EXE packaging with PyInstaller  

---

## 🤝 Contributing

Pull requests are welcome. If you have ideas for improvements, feel free to open an issue.

---

## 📜 License

MIT License — free to use, modify, and distribute.
