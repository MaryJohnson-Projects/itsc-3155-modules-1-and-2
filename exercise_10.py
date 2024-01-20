# Mary Johnson 1/14/2023
# https://www.w3schools.com/python/ref_list_pop.asp

x = list(input("Enter a string: "))
splitList = []

while len(x) > 0:
    tempList = []
    for i in range(3):
        if len(x) > 0:
            tempList.append(x.pop(0))
    splitList.append(tempList)

print(splitList)