# words = input("Enter the message: ")

# print(type(words), words)
# print(len(words))
import random
import string

message = input("Enter your message: ")
n=3
random_chars_f = ''.join(random.choices(string.ascii_letters, k=n))
random_chars_b = ''.join(random.choices(string.ascii_letters, k=n))

action = int(input("What would you like to do?\nPress 0 for Encryption and 1 for Decryption: "))

def encrypt(message):
    words = message.split()
    encrypted_code = []

    for word in words:    
        if len(word) >=3 and random_chars_f != random_chars_b:
            res = word[1:] + word[0]
            coded = random_chars_f + res + random_chars_b
            encrypted_code.append(coded)

        else:
            # elif len(words)<3:
                coded = word[::-1]
                encrypted_code.append(coded)

    return ' '.join(encrypted_code)    


def decrypt(message):
    words = message.split()
    decrypted_code = []

    for word in words:
        if len(word)>=3:
            res = word[3:-3]
            decoded = res[-1] + res[:-1]
            decrypted_code.append(decoded)
        else:
            decoded = word[::-1]
            decrypted_code.append(decoded)
    
    return ' '.join(decrypted_code)

if action == 0:
    print(encrypt(message))
else:
    print(decrypt(message))