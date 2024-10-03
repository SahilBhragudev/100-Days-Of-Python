print("Welcome to the Love Calculator!")

def calculate_love_score(name1,name2):
    name = (name1+name2).upper()
    count_T = 0
    count_R = 0
    count_U = 0
    count_E = 0
    count_L = 0
    count_O = 0
    count_V = 0
    count_E = 0

    for letter in name:
        if(letter == 'T'): 
            count_T += 1
        elif(letter == 'R'): 
            count_R += 1
        elif(letter == 'U'): 
            count_U += 1
        elif(letter == 'E'): 
            count_E += 1
        elif(letter == 'L'):
            count_L += 1
        elif(letter == 'O'):
            count_O += 1
        elif(letter == 'V'):
            count_V += 1
        elif(letter == 'E'):
            count_E += 1

    sum1 = count_T+count_R+count_U+count_E
    sum2 = count_L+count_O+count_V+count_E
    
    love_score = str(sum1) + str(sum2)
    print(love_score)

calculate_love_score("Angela Yu","Jack Bauer")

