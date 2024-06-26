# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
text = "ATTACKATONCE"
s = 4
# print("Text : " + text)
# print("Shift : " + str(s))
# print("Cipher: " + encrypt(text, s))



# A python program to illustrate Caesar Cipher Brute Force Decryption Technique

message = 'GIEWIVrGMTLIVrHIQS' #encrypted message
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key #%s: %s' % (key, translated))




# Program to illustrate substitution cypher

# Define the substitution dictionary
substitution_dict = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm'
}

# Function to encrypt the message
def encrypt_message(message):
    encrypted_message = ""
    for letter in message.lower():
        if letter in substitution_dict:
            encrypted_message += substitution_dict[letter]
        else:
            encrypted_message += letter
    return encrypted_message

# Function to decrypt the message
def decrypt_message(encrypted_message):
    decrypted_message = ""
    for letter in encrypted_message.lower():
        if letter in substitution_dict.values():
            for key in substitution_dict:
                if substitution_dict[key] == letter:
                    decrypted_message += key
        else:
            decrypted_message += letter
    return decrypted_message


# Encrypt the message
encrypted_message = encrypt_message("hello, world!")
print("Encrypted Message: ", encrypted_message)

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted Message: ", decrypted_message)