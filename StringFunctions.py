a = "Sahil"
print(len(a))
print(a.upper())
print(a.lower())

str1 = "abdcDERfg"
print(str1.lower())
'''
In Python strings are immutable . When a string is converted from upper to lower or lower to upper, it returns a new string , the original string remains unchanged

'''
str2 = "Silver Spoon  !!!!!! Silver"
print(str2.rstrip("!"))

# It skips the trailing exclamation marks but doesn't skip the leading ones!

str3 = str2.replace("Silver", "Gold")
print(str3)

# It replaces all the occurences of a string

str4 = str2.split()
print(str4)

# It splits a string from the specified character and returns a list

blogHeading = "introduction To Java"
print(blogHeading.capitalize())

#The capitalise method turns only the first character into uppercase and the rest of characters are only converted to lowercase

str5 = "Welcome to Console"
print(len(str5))
str6 = str5.center(50)
print(len(str6))
print(str6)

# The center method aligns the string to the center as per the parameters given by the user

print(str2.count("S"))
print(str2.count("!"))

#Count method returns the number of times the given value has occurred within the given string

print(str5.endswith("ole"))
print(str5.endswith("o"))

# The endswith method checks if the string ends with a given value. If yes then return True, else return False

str7 = print(str5.endswith("to", 4, 10))

print(str5.find("t"))
print(str5.find("c"))
print(str5.find("x"))
print(str5.find("ishh"))
print(str5.find("km"))

# find method searches for the first occurence of the given value and returns the index where it is present. If given value is absent from the string then return -1

str8 = "WelcomeTo9897TheConsole"
str9 = "Welcome To The Console"
print(str8.isalnum())
print(str9.isalnum())

#isalnum method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False

print(str9.isalpha())
str10 = str8.lower()
print(str10.islower())
print(str10.isupper())

str11 = "We wish you a Merry Christmas\n"
str12 = "We wish you a Merry Christmas"
print(str11.isprintable())
print(str12.isprintable())

#printable method returns True if all the values within the given string are printable, if not, then return False

str13 = "         "
print(str13.isspace())

str14 = " This is a title"
str15 = " This Is A Title"
print(str14.istitle())
print(str15.istitle())

print(str11.swapcase())
print(str11.title())
