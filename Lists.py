state1 = 'California'
state2 = "Pennyslvenia"

states = ["Delaware" , "california", "Pennsylnvenia" , "Los Angeles"]
states[2] = "pencilvenia"
print(states[2])
print(states[-1])

states.append("New Jersey")
# print(states[4])
states.extend(["Georgia" , "Joeland" , "TrumpLand"])
# print(states[5])
# print(states[6])
# print(states[7])
# print(states)
states.pop(3)
print(states)
states.remove("california")
print(states)
states.insert(3,"california")
print(states)
