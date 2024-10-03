import random
print("Welcome to a Strong Password Generator!")

digits = ['0', '1' ,'2' , '3' , '4' , '5' , '6' , '7', '8', '9']
alphabets = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
              'W', 'X', 'Y', 'Z' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
              'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z']     
symbols = ['@','#','$','&','*','!']

total_digits = int(input("How many digits do yo want in your password?\n"))
total_alphabets = int(input("How many alphabets do yu want in your password?\n"))
total_symbols = int(input("How many symbols do you want in your password?\n"))

Number_of_characters = total_alphabets+total_digits+total_symbols
print("The total numbers of charaters in your password : " ,Number_of_characters)
# password = ""

# for digit in range(0,total_digits):
#     password += random.choice(digits)

# for alphabtet in range(0,total_alphabets):
#     password += random.choice(alphabets)

# for symbol in range(0,total_symbols):
#     password += random.choice(symbols)


password_List = []

for digit in range(0,total_digits):
    password_List.append(random.choice(digits))

for alphabtet in range(0,total_alphabets):
    password_List.append(random.choice(alphabets))

for symbol in range(0,total_symbols):
    password_List.append(random.choice(symbols))

# password = random.sample(password_List,Number_of_characters)

# for char in password:
#     print(char,end='')

print(password_List)

random.shuffle(password_List)
print(password_List)

for char in password_List:
    print(char,end='')