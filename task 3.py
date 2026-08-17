import random
import string
length = int(input("Enter Password length: "))
characters= string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for _ in range(length))
print("Generate Password:", password)