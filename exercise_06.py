# Mary Johnson 1/14/2023

grid2D = [ [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0] ]

y = int(input("Enter a row num from 1 to 5: "))
x = int(input("Enter a col num from 1 to 5: "))

grid2D[y-1][x-1] = 1

for i in grid2D:
    print(i[0],i[1],i[2],i[3],i[4])

