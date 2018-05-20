with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")
ranges = []
part1 = 0
part2 = 0
highestRange = 0
for i in range(len(comm)):
    t = comm[i].split("-")
    ranges.append([int(t[0]), int(t[1])])
ranges.sort()
if ranges[0][0] != 0:
    part1 = 0
else:
    for i in range(len(ranges)):


        upperBound = ranges[i][1]
        highestRange = upperBound if highestRange<upperBound else highestRange
        if(i==len(ranges)-1):
            part2 += 4294967295 - highestRange
            break
        if(highestRange+1 < ranges[i+1][0]):
            if(part1==0):
                part1 = highestRange+1
            part2 += ranges[i+1][0]-1-highestRange



print("Part 1: {}\nPart 2: {}".format(part1, part2))