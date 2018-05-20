with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

pad = [[1,2,3],[4,5,6],[7,8,9]]

curPos = [1,1]
part1 = ""
for i in comm:
    for j in i:
        if(j == "R"):
            curPos[1] = min(curPos[1]+1,2)
        if(j == "D"):
            curPos[0] = min(curPos[0]+1,2)
        if(j == "L"):
            curPos[1] = max(curPos[1]-1,0)
        if(j == "U"):
            curPos[0] = max(curPos[0]-1,0)
    part1 += str(pad[curPos[0]][curPos[1]])


pad2 = [list(i) for i in "0000000\n0001000\n0023400\n0567890\n00ABC00\n000D000\n0000000".split("\n")]
curPos2 = [3,1]
part2 = ""
getloc = lambda a: pad2[a[0]][a[1]]

for i in comm:
    for j in i:
        if(j == "R"):
            newpos = [curPos2[0], curPos2[1]+1]
        if(j == "D"):
            newpos = [curPos2[0]+1, curPos2[1]]
        if(j == "L"):
            newpos = [curPos2[0], curPos2[1]-1]
        if(j == "U"):
            newpos = [curPos2[0]-1, curPos2[1]]
        if(getloc(newpos) != '0'):
            curPos2 = newpos
    part2 += str(getloc(curPos2))

print("Part 1: {}\nPart 2: {}".format(part1, part2))