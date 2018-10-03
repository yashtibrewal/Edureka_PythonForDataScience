from cryptography.fernet import Fernet

reference_ID = input("Enter the reference ID:\n")
key = ""
if len(reference_ID) is 12:
    # allow number and alphabets only
    constraint = True
    for letter in reference_ID:
        if letter.isalpha() or letter.isdigit() or letter in ["@$"]:
            pass
        else:
            constraint = False
    if constraint:
        # read the key
        with open("key.txt",'r') as file:
            key = file.read().strip("\n")
            key = str.encode(key)
            # print(key)
        # encrypt and store in the local file
        with open("referenceID.txt",'a') as file:
            ferent_object = Fernet(key)
            byte_form_reference_ID = str.encode(reference_ID)
            cipher_text = ferent_object.encrypt(byte_form_reference_ID)
            file.write(cipher_text.decode()+"\n")
            print("Your Reference ID has been stored")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
