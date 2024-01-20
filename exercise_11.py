# Mary Johnson
forwardStr = str(input("Enter a string: "))
backwardStr = ""

for i in range(len(forwardStr)):
    backwardStr+=(forwardStr[len(forwardStr)-i-1])

print(backwardStr)