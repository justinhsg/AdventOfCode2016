

with open("input.txt", "r") as infile:
    comm = infile.read()
grid = []
NROWS = 40
NROWS2 = 400000
grid.append(comm)


def isTrap(pos, row):
    if(pos==-1 or pos == len(comm)):
        return False
    else:
        return True if grid[row][pos] == '^' else False

def willBeTrap(pos,row):
    boolList = [isTrap(pos-1, row-1), isTrap(pos, row-1), isTrap(pos+1, row-1)]
    if(boolList == [True, True, False]):
        return True
    elif(boolList == [True, False, False]):
        return True
    elif(boolList == [False, False, True]):
        return True
    elif(boolList == [False, True, True]):
        return True
    else:
        return False

for i in range(1,NROWS2):
    tRow = ''
    for j in range(len(comm)):
        tRow += '^' if willBeTrap(j,i) else '.'
    grid.append(tRow)
    if(i%1000 == 0):
        print("{}%".format(i*100//NROWS2), end="\r")

part1 = 0
part2 = 0
for i in range(NROWS):
    part1 += grid[i].count('.')
for i in range(NROWS2):
    part2 += grid[i].count('.')

print("Part 1: {}\nPart 2: {}".format(part1, part2))



