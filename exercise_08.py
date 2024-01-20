# Mary Johnson 1/14/2023
# https://www.w3schools.com/python/ref_list_count.asp

listMult = []
for i in range(10):
    listMult.append( int( input("Enter number "+str(i+1)+": ") ) )

listSing = []
for i in listMult:
    if (listMult.count(i) == 1) and (listSing.count(i) == 0):
        listSing.append(i)
        
print("Original List: ",listMult)
print("Nums that appear once: ",listSing)
