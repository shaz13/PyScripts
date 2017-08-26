import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ciper_list = []

def Encrypt_File():
    salt_num = input("Enter the SALT")
    salt = os.urandom(salt_num)
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
            )
    password = str(raw_input("Enter the Encrption password: "))
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    with open('Decrypted.txt','r') as FILE_TO_READ:
        for line in FILE_TO_READ:
            cipher_line = f.encrypt(line)
            ciper_list.append(cipher_line)
    FILE_TO_READ.close()
    with open('Encrypted_file.txt','w') as FILE_TO_WRITE:
        for line in ciper_list:
            FILE_TO_WRITE.write(line)
    FILE_TO_WRITE.close()

    with open('Encrpted_file.txt','r') as FILE_TO_READ:
        for line in FILE_TO_READ:
            print f.decrypt(line)
Encrypt_File()

def Decrypt_File():
    password = str(raw_input("Enter the Encrption password: "))
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    with open('Encrpted_file.txt','r') as FILE_TO_READ:
        for line in FILE_TO_READ:
            print line
            print f.decrypt("gAAAAABZoaIUaUun__3xNjozMy77sahBO2KFh14Jou0EaKTgMETGLtoGE516bDhlbXM63KhpLonyLd89xZTbBpQ14aCvskXuzb_-FOxpXX6owHIBH7AlIdS7wPfe-VCrs3pOyMF3AtO3DqJk0QtJSAqEc3f-y28YHdjiXMDfsCv9tUky_dL9BzkHw8xeYfLiXhhLiJv61VGi")
Decrypt_File()
