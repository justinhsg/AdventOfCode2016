with open("input.txt", "r") as infile:
    comm = [list(map(int,i.strip().split())) for i in infile.read().split("\n")]

part1 = 0
for i in comm:
    j = sorted(i)
    if(j[0] + j[1] > j[2]):
        part1 +=1

part2 = 0
for i in range(0,len(comm),3):
    for j in range(3):
        sides = sorted([comm[i][j], comm[i+1][j], comm[i+2][j]])
        if(sides[0] + sides[1] > sides[2]):
            part2 += 1
print("Part 1: {}\nPart 2: {}".format(part1, part2))