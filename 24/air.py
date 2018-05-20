from collections import deque
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

NAMES = ['0', '1', '2', '3','4','5','6','7']
DX = [-1,0,1,0]
DY = [0,-1,0,1]
grid = []
visited = []
nodes = []
bfsq = deque()


dist = []
memory = []

def listBin(inList):
    op = 0
    for i in range(8):
        if(inList[i]):
            op+=2**i
    return op

def binList(num):
    outList = []
    for i in range(8):
        outList.append(False)
    for i in range(7,-1,-1):
        if( (2**i) <= num):
            outList[i] = True
            num -= 2**i
    return outList

def TSP(end, bin):
    if memory[end][bin]!= -1:
        return memory[end][bin]
    curList = binList(bin)
    curList[end] = False
    reqDist = 9999999999999999
    for i in range(len(curList)):
        if(curList[i]):
            newDist = dist[i][end] + TSP(i, listBin(curList))
            reqDist = newDist if newDist<reqDist else reqDist
    memory[end][bin] = reqDist
    return reqDist



def bfs(start, end):
    bfsq.clear()
    visited = []
    bfsq.append([nodes[start], 0])
    visited.append(nodes[start])
    while(len(bfsq)!=0):
        curPos = bfsq.popleft()
        curX = curPos[0][0]
        curY = curPos[0][1]
        curD = curPos[1]
        for i in range(4):
            newX = curX+DX[i]
            newY = curY+DY[i]
            if([newX, newY] not in visited):
                if(grid[newX][newY]!='#'):
                    if(grid[newX][newY] == str(end)):
                        dist[start][end] = curD+1
                        dist[end][start] = curD+1
                        break
                    visited.append([newX, newY])
                    bfsq.append([[newX,newY], curD+1])
        if(dist[start][end]!=0):
            break




for i in range(8):
    trow = []
    for j in range(8):
        trow.append(0)
    dist.append(trow)
    nodes.append([-1,-1])

for i in range(len(comm)):
    row = []
    for j in range(len(comm[i])):
        row.append(comm[i][j])
        if(comm[i][j] in NAMES):
            print(comm[i][j])
            nodes[int(comm[i][j])] = [i, j]
            print(nodes)
    grid.append(row)

for i in range(8):
    for j in range(i+1, 8):
        bfs(i,j)

for i in range(8):
    trow = []
    for j in range(256):
        trow.append(-1)
    memory.append(trow)

for i in range(0,8):
    memory[i][2**i] = dist[0][i]

part1 = 999999999999
part2 = 999999999999
for i in range(1,8):
    tDist = TSP(i,254)
    tDist2 = TSP(i, 254) + dist[i][0]
    part1 = tDist if tDist<part1 else part1
    part2 = tDist2 if tDist2<part2 else part2

print("Part 1: {}\nPart 2: {}".format(part1, part2))
