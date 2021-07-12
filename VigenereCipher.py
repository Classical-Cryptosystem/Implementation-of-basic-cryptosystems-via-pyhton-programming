#Implementation Vigenere Cipher
def encryption(plaintext,key):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        keychar = key[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr(((ord(char)-65)+(ord(keychar)-65)) % 26 + 65)
 
        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr(((ord(char)-97)+(ord(keychar)-97)) % 26 + 97)
        
        # Skips punctuations and blanks
        else: 
            continue;
    return result
 
def decryption(ciphertext,key) :
    resultt = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        keychar = key[i]
        # Encrypt uppercase characters
        if (char.isupper()):
            resultt += chr(((ord(char)-65)-(ord(keychar)-65)) % 26 + 65)
 
        # Encrypt lowercase characters
        elif (char.islower()):
            resultt += chr(((ord(char)-97)-(ord(keychar)-97)) % 26 + 97)
        
        # Skips punctuations and blanks
        else: 
            continue;
    return resultt
 
 
value=int(input("1-Encryption? \n2-Decryption? \n"))
if value==1:
            plaintext= input("Enter the plaintext: \n")
            key= int(input("Enter the key: \n"))
            print ("Plaintext:",plaintext)
            print ("Key:",key)
            print ("Ciphertext:",encryption(plaintext,key)),
    
elif value==2:    
            ciphertext= input("Enter the ciphertext: \n")
            key= int(input("Enter the key: \n"))
            print ("Ciphertext:",ciphertext)
            print ("Key:",key)
            print ("Plaintext:",decryption(ciphertext,key)),
else:   
            print("Invalid value!")
            
© 2021 GitHub, Inc.
