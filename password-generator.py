import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
L = int(input("How many letters would you like in your password?\n")) 
N = int(input(f"How many numbers would you like?\n"))
S = int(input(f"How many symbols would you like?\n"))

password = []

for char in range(1, L + 1):
    password += random.choice(letters)
for char in range(1, N + 1):
    password += random.choice(numbers)
for char in range(1, S + 1):
    password += random.choice(symbols)

random.shuffle(password)

print("You password is: " + ''.join(password))