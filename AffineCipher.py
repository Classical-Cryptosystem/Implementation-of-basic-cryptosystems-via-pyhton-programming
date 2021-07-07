#Implementation Affine Cipher (Ciphertext = a(Plaintext)+b)

def encryption(plaintext, a, b):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += (a *(ord(char)-65) +b)%26+65;
 
        # Encrypt lowercase characters
        elif (char.islower()):
           result += (a *(ord(char)-97) +b)%26+97;
        
        # Skips punctuations and blanks
        else: 
            continue;
    return result
