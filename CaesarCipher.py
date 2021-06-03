#Implementation Caesar Cipher
def encryption(plaintext,s):
    result = ""
    s = 3
    for i in range(len(plaintext)):
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        
        # Skips punctuations and blanks
        else: 
            continue;
    return result
 
def decryption(ciphertext,u) :
    resultt = ""
    u=3
    for i in range(len(ciphertext)):
        char = ciphertext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            resultt += chr((ord(char) - u-65) % 26 + 65)
 
        # Encrypt lowercase characters
        elif (char.islower()):
            resultt += chr((ord(char) - u - 97) % 26 + 97)
        
        # Skips punctuations and blanks
        else: 
            continue;
    return resultt
 
 
value=int(input("1-Encryption? \n2-Decryption? \n"))
if value==1:
            plaintext= input("Enter the plaintext: \n")
            s=3
            print ("Plaintext:",plaintext)
            print ("Shift:",str(s))
            print ("Ciphertext:",encryption(plaintext,s)),
    
elif value==2:    
            ciphertext= input("Enter the ciphertext: \n")
            u=3
            print ("Ciphertext:",ciphertext)
            print ("Shift:",str(u))
            print ("Plaintext:",decryption(ciphertext,u)),
else:   
            print("Invalid value!")
            
        
        
        
        
