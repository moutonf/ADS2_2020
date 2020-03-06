
import random 
import string  # Importing ASCII letters

# The string module will store all alphabet letters in the given variable
# We clarify that we only need upper case letters
alphabet = string.ascii_uppercase


def cypher_explain():
    """Short explanation of Caeser Cypher"""

    print("Caeser Cypher is a form of encryption that involves 'rotating' each letter of a given\n",
          "string by a certain number of places. 'Rotating' is shifting through the letters of the alphabet.\n",
          "In order to encode a word - program rotates each letter of the word by the same amount - key.\n")


def encoder():
    """Function that encodes given message with a randomly generated key"""

    message = "Version control system is fun"
    print("Original message is: \n", message)
    key = random.randint(0, 26)                          # Randomly generated key
    print("We encode the original message by ", key)

    message = message.upper()   # first convert all letters of the message into Uppercase letters
    encrypted_message = ""      # empty string for a new encrypted message

    for char in message:        # check if a letter in the message is in the alphabet
        if char in alphabet:
            # we find the new position of each character by first locating it in the alphabet
            # and then shifting with the key
            # use modulo operation to escape an error if the new position is larger than alphabet length
            char_position = (alphabet.find(char) + key) % len(alphabet)
            encrypted_message += alphabet[char_position]
        else:
            encrypted_message += char
    print("The encoded result:\n", encrypted_message)


if __name__ == '__main__':
    cypher_explain()
    encoder()

