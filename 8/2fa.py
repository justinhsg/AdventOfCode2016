import re
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")


grid = []
for i in range(6):
    trow = []
    for j in range(50):
        trow.append(0)
    grid.append(trow)

def printGrid():
    for i in range(6):
        tString=""
        for j in range(50):
            tString+="X" if grid[i][j]==1 else " "
        print(tString)
def rect(x,y):
    for i in range(x):
        for j in range(y):
            grid[j][i] = 1

def rotCol(x,v):
    tCol = [0]*6
    for i in range(6):
        tCol[i] = grid[i][x]
    for i in range(6):
        grid[(i+v)%6][x] = tCol[i]

def rotRow(y,v):
    tRow = [0]*50
    for i in range(50):
        tRow[i] = grid[y][i]
    for i in range(50):
        grid[y][(i+v)%50] = tRow[i]

for i in range(len(comm)):
    tCommand = comm[i].split(" ")
    if(len(tCommand)<2):
        continue
    if(tCommand[0] == "rect"):
        tparams = tCommand[1].split("x")
        rect(int(tparams[0]),int(tparams[1]))
    else:
        if(tCommand[1] == "row"):
            rotRow(int(tCommand[2][2:]), int(tCommand[4]))
        elif(tCommand[1] == "column"):
            rotCol(int(tCommand[2][2:]), int(tCommand[4]))

part1 = 0
for i in range(6):
    part1 += grid[i].count(1)
print("Part 1: {}\nPart 2: ".format(part1))
printGrid()
