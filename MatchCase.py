a = int(input("enter the value of a : "))
match a:
  case 0:
    print(" a is zero")
  case 1:
    print("a is one")
  case 2:
    print("a is two")
  case 3:
    print("a is three")
  case _ if a != 70:
    print(a, " is not seventy")
  case _ if a != 80:
    print(a)
  case _ if a != 90:
    print(a)
