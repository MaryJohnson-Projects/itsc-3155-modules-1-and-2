# Mary Johnson 1/14/2023

stringA = input("Enter a string: ").lower()
stringB = input("Enter another string: ").lower()

# Makes stringA the longer string
if len(stringB) > len(stringA):
    temp = stringA
    stringA = stringB
    stringB = temp

substring = stringA[len(stringA)-len(stringB):]

print(stringB == substring)

