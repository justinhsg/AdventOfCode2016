from collections import deque
with open("input.txt", "r") as infile:
    comm = int(infile.read())

wallMem = []
visited = []
dist = []
for i in range(75):
    wallMem.append([])
    visited.append([])
    for j in range(75):
        wallMem[i].append(-1)
        visited[i].append(-1)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def isWall(x,y):
    if(wallMem[x][y]!=-1):
        return True if wallMem[x][y] == 1 else False
    tVal = x*x + 3*x + 2*x*y + y + y*y + comm
    nOnes = bin(tVal).count('1')
    if(nOnes%2==0):
        wallMem[x][y] = 0
        return False
    else:
        wallMem[x][y] = 1
        return True

queue = deque()
queue.append([1,1,0])

part1 = -1
visited[1][1] = 0
part2=1
while(not len(queue) == 0):
    curPos = queue.popleft()
    curX = curPos[0]
    curY = curPos[1]
    curDist = curPos[2]
    for i in range(4):
        newX = curX+dx[i]
        newY = curY+dy[i]
        if(newX >= 0 and newY >= 0):
            if(not isWall(newX,newY)):
                if(visited[newX][newY] == -1):
                    visited[newX][newY] = curDist+1
                    if(curDist+1 <= 50):
                        part2+=1
                    if(newX == 31 and newY == 39):
                        part1 = curDist+1
                        break
                    else:
                        queue.append([newX,newY,curDist+1])
print("Part 1: {}\nPart 2: {}".format(part1, part2))