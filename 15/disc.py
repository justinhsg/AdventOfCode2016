with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")
part1 = 0
part2 = 0

discs= []
for i in range(len(comm)):
    splitComm = comm[i].split(" ")
    discs.append([int(splitComm[3]), int(splitComm[11][:-1])])


time = 0
while(True):
    canPass = True
    for i in range(len(discs)):
        discPos = (time+discs[i][1]+i+1)%discs[i][0]
        if(discPos!=0):
            canPass = False
            break
    if(canPass):
        break
    else:
        time+=1

part1 = time

time = 0
discs.append([11,0])
while(True):
    canPass = True
    for i in range(len(discs)):
        discPos = (time+discs[i][1]+i+1)%discs[i][0]
        if(discPos!=0):
            canPass = False
            break
    if(canPass):
        break
    else:
        time+=1
part2 = time

print("Part 1: {}\nPart 2: {}".format(part1, part2))