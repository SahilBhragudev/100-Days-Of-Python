import random

random_number = random.randint(0,1)
random_number = random.random() * 100
print(random_number)
if random_number == 0:
    print("heads")
elif random_number == 1:
    print("Tails")
else:
    print("Error Occured !")