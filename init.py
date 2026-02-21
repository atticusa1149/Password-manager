from cryptography.fernet import Fernet
import hashlib

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
import hashlib

def set_master_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    with open("master.hash", "w") as f:
        f.write(hashed)

#generate_key()
#set_master_password("helloworld67")