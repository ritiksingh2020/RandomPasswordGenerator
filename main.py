#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password=[]
for q in range(nr_letters):
    temp=random.randrange(len(letters))
    password.append(letters[temp])
for q in range(nr_symbols):
    temp=random.randrange(len(symbols))
    password.append(symbols[temp])
for q in range(nr_numbers):
    temp=random.randrange(len(numbers))
    password.append(numbers[temp])
#print("".join(password))
for q in range(len(password)):
    temp=random.randrange(len(password))
    password[q],password[temp]=password[temp],password[q]
print("".join(password))