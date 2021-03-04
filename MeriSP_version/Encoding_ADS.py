from random import randint

def random_encrypt(string, shift):
    
    # Creating an empty list to store characters
    CesarCipher= []
    for character in string:
        ASCIIcharacter = ord(character)
        # ASCII character set for puntuation and numbers:
        if 32 <= ASCIIcharacter <=57:
            NewOrd = 32 +((ASCIIcharacter -32 + shift) % 26)
        # ASCII character set for uppercase letters:
        elif 65 <= ASCIIcharacter <=90:
            NewOrd = 65 +((ASCIIcharacter -65 + shift) % 26)
        # ASCII character set for lowercase letters:   
        elif 97 <= ASCIIcharacter <=122:
            NewOrd = 97 +((ASCIIcharacter -97 + shift) % 26)
        else:
            NewOrd = ASCIIcharacter

        NewChar = chr(NewOrd)
        CesarCipher.append(NewChar)
        
    return "".join(CesarCipher)

def random_decrypt(string, shift):
    
    # Creating an empty list to store characters
    CesarCipher= []
    for character in string:
        ASCIIcharacter = ord(character)
        # ASCII character set for puntuation and numbers:
        if 32 <= ASCIIcharacter <=57:
            NewOrd = 32 +((ASCIIcharacter -32 - shift) % 26)
        # ASCII character set for uppercase letters:
        elif 65 <= ASCIIcharacter <=90:
            NewOrd = 65 +((ASCIIcharacter -65 - shift) % 26)
        # ASCII character set for lowercase letters:   
        elif 97 <= ASCIIcharacter <=122:
            NewOrd = 97 +((ASCIIcharacter -97 - shift) % 26)
        else:
            NewOrd = ASCIIcharacter

        NewChar = chr(NewOrd)
        CesarCipher.append(NewChar)
        
    return "".join(CesarCipher)


message = 'Version Control is fun!'
n = randint(0,26)

encrypted_message = random_encrypt(message, n)
decrypted_message = random_decrypt(encrypted_message, n)
print(encrypted_message)
print(decrypted_message)