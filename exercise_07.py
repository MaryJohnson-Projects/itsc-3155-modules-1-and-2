x = input("Enter a number or QUIT to quit: ")

myList = []

while not (x == "QUIT"):
    myList.append(int(x))

    x = input("Enter a number or QUIT to quit: ")

evenList = []

for i in myList:
    if (i % 2) == 0:
        evenList.append(i)

print("All Nums: ",myList)
print("Even Nums: ",evenList)