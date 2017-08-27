from Crypto.Cipher import AES
ciper_list = []

print "+"*15
print "\n ARIS : A personal Encryption tool ~ by Shaz"
print "+"*15

choice = raw_input("Enter E for ENCRYPTION or D to DECRYPT your file: ")

def Encrypt_File():
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    with open('Decrypted.txt','r') as FILE_TO_READ:
        for line in FILE_TO_READ:
            cipher_line = obj.encrypt(line)
            ciper_list.append(cipher_line)
    FILE_TO_READ.close()
    with open('Encrypted.txt','w') as FILE_TO_WRITE:
        for line in ciper_list:
            FILE_TO_WRITE.write(line)
    FILE_TO_WRITE.close()

def Decrypt_File():
    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    with open('Encrypted.txt','r') as FILE_TO_READ:
        for line in FILE_TO_READ:
            print obj2.decrypt(line)
if choice in ['E','e']:
    Encrypt_File()
elif choice in ['D','d']:
    Decrypt_File()
