#Implement Hill Cİpher
#Encryption:  [Key][Plaintext]=[Ciphertext]
#Decryption:  [Key][Ciphertext]=[Plaintext]
#plaintext and ciphertex block_size=2 & Key  = nxn matrix
import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg



def encryption(Key, message):
    x=np.dot(Key, message)
    return x    

def decryption(Key, Ciphertext):
    xx = np.dot(linalg.pinv(Key), Ciphertext)
    return xx

key = np.array([[1,2,2], [4,4,2], [4,4,4]]) 
plain = np.array([3, 6,10])

cipher= np.array([35, 56, 76])






value=int(input("1-Encryption? \n2-Decryption? \n"))
if value==1:
            plaintext= input("Enter the plaintext: \n")
            print ("Plaintext:",plaintext, "\n")
            print("Ciphertext:",encryption(key, plain)),
    
elif value==2:    
            ciphertext= input("Enter the ciphertext: \n")
            print ("Ciphertext:",ciphertext, "\n")
            print("Plaintext:",decryption(key, cipher)),
else:   
            print("Invalid value!")
