# Mary Johnson
myString = str(input("Enter a string: ")).strip()
lowerCase = ""
upperCase = ""

for x in myString:
    if x.isupper():
        upperCase+=x
    elif x.islower():
        lowerCase+=x

print(lowerCase+upperCase)