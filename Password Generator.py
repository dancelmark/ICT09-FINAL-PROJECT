import random
import string

def password_generator(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated password:", password_generator(12))
