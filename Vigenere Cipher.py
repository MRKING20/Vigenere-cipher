#cipher = (key + plain) mod 26
#plain = (cipher - key) mod 26
#BY The "KING" 
print(r"""
     
    
 ██████╗████████╗███████╗    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗       ██╗██╗  ██╗██╗███╗   ██╗ ██████╗ ██╗  
██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗     ██╔╝██║ ██╔╝██║████╗  ██║██╔════╝ ╚██╗ 
██║        ██║   █████╗      ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ██╔╝ █████╔╝ ██║██╔██╗ ██║██║  ███╗ ╚██╗
██║        ██║   ██╔══╝      ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚██╗ ██╔═██╗ ██║██║╚██╗██║██║   ██║ ██╔╝
╚██████╗   ██║   ██║         ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║     ╚██╗██║  ██╗██║██║ ╚████║╚██████╔╝██╔╝ 
 ╚═════╝   ╚═╝   ╚═╝         ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝      ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  
                                                                                                                          

                                     

                               
**********************************************
*       http://nidhal-mabrouk.tech/          *
*       Welcome to My Vigenere Cipher!       *
*       Copyright of King, 2024              *
**********************************************
""")




alp = 'abcdefghijklmnopqrstuvwxyz'

#This loop to create a new key has a same length as the plain text or cipher text
def samelength(c_np,k):
    nk = k

    for j in range(len(c_np)):
        for i in range (len(k)):
            if len(nk) != len(c_np):
                nk += k[i] 
            else:
                break

    return nk

#Encryption Phase:
def encrypt(plain,key):
    np = plain.replace(" ", "") #to remove spaces from the plain text 
    nk = samelength(np, key)

    cipher = ""

    for k in range(len(nk)):
        ck = ((alp.find(nk[k]) + alp.find(np[k])) % 26)
        cipher += alp[ck]

    print("Here is your encrypted text",cipher)



#Decryption Phase: 
def decrypt(cipher,key):
    nk = samelength(cipher,key)

    plain = ""

    for k in range(len(nk)):
            pk = ((alp.find(cipher[k]) - alp.find(nk[k])) % 26)
            plain += alp[pk]

    print("Here is your decrypted text",plain)


def validate_input():    
    var = input("Enter '1' to Encrypt or Enter '2' to Decrypt: ")
    
    while True:
        if var == '1':
            plain = input("Put your plain text: ").lower()  # Convert to lowercase to match the alphabet
            key = input("Put your key to encrypt: ").lower()  # Convert to lowercase to match the alphabet
            
            # Check if all characters in 'plain' and 'key' are in the alphabet
            if all(c in alp + " " for c in plain) and all(c in alp for c in key):
                print("Input is valid.")
                encrypt(plain, key)
                break  # Exit the loop if the condition is met
            else:
                print("Invalid input. Only lowercase alphabetic characters are allowed.")
                continue
        
        elif var == '2':
            cipher = input("Put your cipher text: ").lower()
            key = input("Put your key to decrypt: ").lower()
            
            # Check if all characters in 'cipher' and 'key' are in the alphabet
            if all(c in alp for c in cipher) and all(c in alp for c in key):
                print("Input is valid.")
                decrypt(cipher, key)
                break  # Exit the loop if the condition is met
            else:
                print("Invalid input. Only lowercase alphabetic characters are allowed.")
                continue
        
        else:
            print("Invalid choice. Please enter '1' for encryption or '2' for decryption.")
            var = input("Enter '1' to Encrypt or Enter '2' to Decrypt: ") # Ask again if input is invalid

validate_input()
