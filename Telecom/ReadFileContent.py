from cryptography.fernet import Fernet

key = ""
with open("key.txt", 'r') as file:
    key = file.read().rstrip("\n")
    key = str.encode(key)
    print("Key is : ",key)
fernet_object = Fernet(key)

with open("referenceID.txt", 'r') as file:
    lines = file.readlines()
    print("Reference IDS")
    for line in lines:
        line = str.encode(line.rstrip("\n"))
        decrypted_text = fernet_object.decrypt(line)
        print(decrypted_text)
