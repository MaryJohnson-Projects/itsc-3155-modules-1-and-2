# Mary Johnson 1/14/2023

x = int(input("Enter a number: "))

floatyList = []

for i in range(x):
    floatyList.append( float( input("Enter number "+str(i+1)+": ") ) )

print("List: ", floatyList)

sum = 0
for i in floatyList:
    sum += i

avg = sum/x

print("Average: ", avg)



