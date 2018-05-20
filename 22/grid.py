from collections import deque


with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")
part1 = 0
part2 = 0

grid = []
tcol = []
nodes = []
start = []
for i in range(2, len(comm)):
    for j in range(i, len(comm)):
        if(i!=j):
            node1info = comm[i].split()
            node2info = comm[j].split()
            node1use = int(node1info[2][:-1])
            node2use = int(node2info[2][:-1])
            node1avail = int(node1info[3][:-1])
            node2avail = int(node2info[3][:-1])
            if((node1use < node2avail and node1use!=0)or (node2use < node1avail and node2use!=0) ):
                part1+= 1
    nodeinfo = comm[i].split()
    nodeloc = nodeinfo[0].split("-")
    nodex = int(nodeloc[1][1:])
    nodey = int(nodeloc[2][1:])
    if(nodey == 0 and i != 2):
        grid.append(tcol)
        tcol = []
    tcol.append([int(nodeinfo[2][:-1]), int(nodeinfo[1][:-1])])
grid.append(tcol)
for row in range(len(grid[0])):
    trow = ""
    trrow = []
    for col in range(len(grid)):
        node = grid[col][row]
        if(node[0] == 0):
            start = [col, row]
            trow += "."
        elif(node[0] > 200 and node[1] > 200):
            trow += "#"
        else:
            trow += "O"
    nodes.append(trow)

while(True):
    curx = start[0]
    cury = start[1]
    if(nodes[cury-1][curx]=="O"):
        part2+=1
        start[1] -= 1
    else:
        break

while(True):
    curx = start[0]
    cury = start[1]
    if(nodes[cury-1][curx-1]=="#"):
        part2+=1
        start[0] -= 1
    else:
        break

start[0]-=1
part2+=1
part2+=start[1]
start[1] = 0


part2+= len(nodes[0])-2-start[0]
start[1] = len(nodes[0]) -2
part2 += (5*start[1])+1

print("Part 1: {}\nPart 2: {}".format(part1, part2))