#Implement Hill Cİpher
#Encryption:  [Key][Plaintext]=[Ciphertext]
#Decryption:  [Key][Ciphertext]=[Plaintext]
#plaintext and ciphertex block_size=2 & Key  = 2X2 matrix
import numpy as np
from scipy import linalg



key_array = [[0] * 2 for i in range(2)]
key_inverse_array = [[0] * 2 for i in range(2)]
plaintext_converter = [[0] for i in range(2)]
cipher_array = [[0] for i in range(2)]
ciphertext_converter  = [[0] for i in range(2)]
plain_array = [[0] for i in range(2)]

def key_converter(key):
    k = 0
    for i in range(2):
        for j in range(2):
            key_array[i][j] = ord(key[k]) % 65
            k += 1


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
            
def key_inverse(key):
    determinant=(key_array[0][0]* key_array[1][1])-(key_array[0][1]* key_array[1][0])
    x=greatest_common_divisor(determinant, 26)
    if x==1:
        inverse_determinant=a_inverse_in_mod_m(determinant, 26)
        key_inverse_array[0][0] = inverse_determinant*ord(key[3]) % 65
        key_inverse_array[1][1] = inverse_determinant*ord(key[0]) % 65
        key_inverse_array[0][1] = inverse_determinant*(-1*ord(key[1])) % 65
        key_inverse_array[1][0] = inverse_determinant*(-1*ord(key[2])) % 65    
        
    else:
        print("Key is not invertible in mod 26. Please Try Again!")

         





def encryption(plaintext_converter):
    for i in range(2):
        for j in range(1):
            cipher_array[i][j] = 0
            for x in range(2):
                plain_array[i][j] += (key_array[i][x] * 
                                       ciphertext_converter[x][j])
            plain_array[i][j] = plain_array[i][j] % 26
            
def decryption(ciphertext_converter):
    for i in range(2):
        for j in range(1):
            plain_array[i][j] = 0
            for x in range(2):
                cipher_array[i][j] += (key_inverse_array[i][x] * 
                                       plaintext_converter[x][j])
            cipher_array[i][j] = cipher_array[i][j] % 26
  
def HillCipher_encryption(plaintext, key):
    key_converter(key)
    for i in range(2):
        plaintext_converter[i][0] = ord(plaintext[i]) % 65
    encryption(plaintext_converter)
    CipherText = []
    for i in range(2):
        CipherText.append(chr(cipher_array[i][0] + 65))
        
    print("Ciphertext: ", "".join(CipherText))
    
    
def HillCipher_decryption(ciphertext, key):
    key_converter(key)
    for i in range(2):
        ciphertext_converter[i][0] = ord(ciphertext[i]) % 65
    decryption(ciphertext_converter)
    PlainText = []
    for i in range(2):
        PlainText.append(chr(plain_array[i][0] + 65))
        
    print("Plaintext: ", "".join(PlainText))
  

def main():


        value=int(input("1-Encryption? \n2-Decryption? \n"))
        if value==1:
            plaintext= input("Enter the plaintext: \n")
            print ("Plaintext:",plaintext, "\n")
            key= input("Enter the key: \n")
            print ("Key:",key, "\n")
            HillCipher_encryption(plaintext, key),
    
        elif value==2:    
            ciphertext= input("Enter the ciphertext: \n")
            print ("Ciphertext:",ciphertext, "\n")
            key= input("Enter the key: \n")
            print ("Key:",key, "\n")
            HillCipher_decryption(ciphertext, key),
        else:   
            print("Invalid value!")

