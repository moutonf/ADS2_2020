# V1.1 Encoding ADS
# Original author Leon Helgeland

import random  # Import random library

string = "Version control system is fun"  # String to encrypt
shift = random.randint(0, 26)  # Randomly selects an integer between 0 and 26

def uncrypt(x):  # Unencodes the string
    unencoded_string = ""  # Variable that has new shifted letters appended to it to form the complete string
    for i in x:  # Loops through each letter of the string
        unencoded_string += chr(ord(i) - shift)  # Uses the integer we got from random to shift the letters accordingly

    print(f"\nUnencoding string using caesar cipher shifting the letters {shift} times backward.\nString to unencode: {x}\nUnencoded string: {unencoded_string}")


def ceasar_chipher():  # Encodes the string
    encoded_string = ""  # Variable that has new shifted letters appended to it to form the complete string
    for i in string:  # Loops through each letter of the string
        encoded_string += chr(ord(i) + shift)  # Uses the integer we got from random to shift the letters accordingly

    print(f"Encoding string using caesar cipher shifting the letters {shift} times forward.\nString to encode: {string}\nEncoded string: {encoded_string}")
    uncrypt(encoded_string)  # Calls the unencoding function

ceasar_chipher() # Calls the caesar_cipher function

# ~~~~~~~~~~~~~~~~~Andrea's Version~~~~~~~~~~~~~~~~~~~~
import random

def randomInt(): 
   ran = random.randint(1, 26)
   return(ran)

def encrypt(text, num):

   result = ""

   # Loop through text
   for i in range(len(text)):
      char = text[i]
      
      # Encrypt uppercase characters
      if (char.isupper()):
         result += chr((ord(char) + num - 65) % 26 + 65)

      # Encryptlowercase characters
      else:
         result += chr((ord(char) + num - 97) % 26 + 97)

   return result

text = "Version Control System is fun"
num = randomInt()

print "Plain Text : " + text
print "Shift pattern : " + str(num)
print "Cipher: " + encrypt(text, num)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
