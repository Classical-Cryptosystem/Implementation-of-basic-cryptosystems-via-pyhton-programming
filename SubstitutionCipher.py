#Substitution of single letters separately—simple substitution—can be demonstrated by writing out the alphabet in some order to represent the substitution.
# Plaintext alphabet:	  ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Ciphertext alphabet:	ZEBRASCDFGHIJKLMNOPQTUVWXY



key=['L', 'F', 'W', 'O', 'A', 'Y','U', 'I','S','V','K','M','N','X','P','B','D','C','R','J','T','Q','E','G','H','Z'] # for uppercase character
key1=['l','f','w','o','a','y','u','ı','s','v','k','m','n','x','p','b','d','c','r','j','t','q','e','g','h','z'] # for lowercase character

alphabet=['A', 'B', 'C', 'D', 'E', 'F','G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # for uppercase character
alphabet1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # for lowercase character





def encryption(plaintext):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += key[(ord(char) -65)]
 
        # Encrypt lowercase characters
        elif (char.islower()):
            result += key1[(ord(char) -97)]
        
        # Skips punctuations and blanks
        else: 
            continue;
    return result

def decryption(ciphertext):

    resultt = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            
            for k in range(len(key)):
                if(char ==key[k]):
                    resultt += alphabet[k]
                else:
                    continue;
 
        # Encrypt lowercase characters
        elif (char.islower()):
            
                for t in range(len(key1)):  
                    if(char ==key1[t]):
                        resultt += alphabet[t]
                    else:
                        continue;
        
        # Skips punctuations and blanks
        else: 
            continue;
    return resultt    


value=int(input("1-Encryption? \n2-Decryption? \n"))
if value==1:
            plaintext= input("Enter the plaintext in capital letters: \n")
            print ("Plaintext:",plaintext)
            print ("Ciphertext:",encryption(plaintext)),
    
elif value==2:    
            ciphertext= input("Enter the ciphertext in capital letters: \n")
            print ("Ciphertext:",ciphertext)
            print ("Plaintext:",decryption(ciphertext)),
else:    
            print("Invalid value!")
            
