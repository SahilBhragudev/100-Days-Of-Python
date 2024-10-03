# def greet():
#     print("Hey ! Good Morning")    
#     print("How do you do ?")    
#     print("Isn't the weather nice today?")

# greet()    

# Function that allows to get input

# def greet_with_name(name):
#     print(f"Hey ! Good Morning {name}")    
#     print(f"How do you do {name}?")    
#     print(f"Isn't the weather nice today , {name}?")    

# greet_with_name("Sahil")    

#  Funcions with more than oe parametres

def greet_with_name(name,location):
    print(f"Hello {name}!")
    print(f"What it's like in {location}")

greet_with_name("sahil","delhi")


def greet_with_name(name,location,age):
    print(f"Hello {name}!")
    print(f"What it's like in {location}")
    print(f"are you {age} years old?")

greet_with_name("sahil","delhi",23)
greet_with_name(location="delhi" , name ="rohit" , age = "23")
