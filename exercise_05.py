# Mary Johnson 1/14/2023
# https://www.w3schools.com/python/ref_set_intersection.asp

listA = []
for i in range(5):
    listA.append( int( input("Enter a number for the first list: ") ) )

listB = []
for i in range(5):
    listB.append( int( input("Enter a number for the second list: ") ) )

# Using sets makes this a bit easier, assures no duplicates.  
listC = list(set(listA).intersection(set(listB)))

print("First List: ",listA)
print("Second List: ", listB)
print("Common List: ", listC)
