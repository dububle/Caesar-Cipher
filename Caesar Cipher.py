def shift_right(atext):    
    atext = atext[-1] + atext[:-1]
    return atext

def shift_left(atext):    
    atext = atext[1:] + atext[0]
    return atext

def encrypt (word, key):
    for i in range(key):
        word = shift_right(word)
    return word

def decrypt (word, key):
    for i in range(key):
        word = shift_left(word)
    return word

choice = input("Would you like to encrypt or decrypt a message?")
if choice == 'encrypt':
    en = input("Input the sentence you would like to encrypt: ")
    key = int(input("Input the key: "))
    print("Here is your encrypted message: ")
    print(encrypt(en,key))
elif choice == 'decrypt':
    de = input("Input the sentence you would like to decrypt: ")
    key = int(input("Input the key: "))
    print("Here is your decrypted message: ")
    print(decrypt(de,key))
