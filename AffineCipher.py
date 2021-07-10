#Implementation Affine Cipher (Ciphertext = a*(Plaintext)+b (mod m))
# gcd(a, m) must be equal to 1, if not a^-1 does not exist and cannot decrypt the Ciphertext.

#Using Extended Euclidean Algorithm for finding a_inverse in mod m

def greatest_common_divisor(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q = b//a
        r = b%a
        m = x-u*q
        n =  y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def a_inverse_in_mod_m(a, m):
    gcd, x, y = greatest_common_divisor(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

 #Encryption
def encryption(plaintext, a, b):
    result = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((a *(ord(char)-ord('A')) +b)%26+ord('A'));
 
        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((a *(ord(char)-ord('a')) +b)%26+ord('a'));
        
        # Skips punctuations and blanks
        else: 
            continue;
    return result

#Decryption

def decryption(ciphertext, a, b):
    result = ""
    a_inverse= a_inverse_in_mod_m(a, 26)
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        
        
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr(a_inverse *(ord(char)-ord('A') -b)%26+ord('A'))
 
        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((a_inverse *(ord(char)-ord('a') -b))%26+ord('a'))
        
        # Skips punctuations and blanks
        else: 
            continue;
    return result

value=int(input("1-Encryption? \n2-Decryption? \n"))
if value==1:
            plaintext= input("Enter the plaintext to encrypt in affine cipher (of the format a*(plaintext)+b): \n")
            a= int(input("Enter the a: \n"))
            b= int(input("Enter the b: \n"))
            print ("Plaintext:",plaintext)
            print ("Ciphertext:",encryption(plaintext,a,b)),
    
elif value==2:    
            ciphertext= input("Enter the ciphertext to decrypt in affine cipher (of the format a_inverse(*(plaintext)-b)): \n")
            a= int(input("Enter the a: \n"))
            b= int(input("Enter the b: \n"))
            print ("Ciphertext:",ciphertext)
            print ("Plaintext:",decryption(ciphertext,a,b)),
else:   
            print("Invalid value!")
            
