with open("input.txt", "r") as infile:
    comm = infile.read().strip().split(", ")


d = [-1, -1, 1, 1]
dist= [0,0]
face = 0
pt = 0
for i in comm:
    if i[0] == "L":
        pt = (pt-1)%4
    elif i[0] == "R":
        pt = (pt+1)%4
    dist[face] += d[pt]*int(i[1:])
part1 = sum(map(abs,dist))

dp = [[-1, 0], [0, 1], [1,0], [0, -1]]
visited = set()
curPos = [0,0]
visited.add((0,0))
found = False
for i in comm:
    if(i[0] == "L"):
        face = (face-1)%4
    elif(i[0] == "R"):
        face = (face+1)%4
    for i in range(int(i[1:])):
        curPos[0] += dp[face][0]
        curPos[1] += dp[face][1]
        tp = (curPos[0], curPos[1])
        if(tp not in visited):
            visited.add(tp)
        else:
            found = True
            part2 = sum(map(abs,tp))
            break
    if(found):
        break

print("Part 1: {}\nPart 2: {}".format(part1, part2))