import random
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "&", "*"]

print("welcome to the Python Password Generator!")
a_alphabet = int(input("how many letters would you like in your password?\n"))
a_numbers = int(input("how many numbers would you like in your password?\n"))
a_symbols = int(input("how many symbols would you like in your password?\n"))

##password = ""
##for char in  range(0, a_alphabet):
##    password += random.choice(alphabet)
##
##for char in  range(0, a_numbers):
##    password += str(random.choice(numbers))
##
##for char in  range(0, a_symbols):
##    password += random.choice(symbols)
##
##print(password)

password = []
for char in  range(0, a_alphabet):
    password.append(random.choice(alphabet))

for char in  range(0, a_numbers):
    password.append(random.choice(numbers))

for char in  range(0, a_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)

password1 = ""
for char in password:
    password1 += char

print(password1)



                 
