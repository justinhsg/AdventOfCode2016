from collections import deque
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

nBot = 0
nOutputs = 0
for i in range(len(comm)):
    splitComm = comm[i].split(" ")
    if(splitComm[0] == "bot"):
        nBot = int(splitComm[1]) if int(splitComm[1]) > nBot else nBot
    if(len(splitComm)==12):
        if(splitComm[5] == "output"):
            nOutputs = int(splitComm[6]) if int(splitComm[6]) > nOutputs else nOutputs
        if(splitComm[10] == "output"):
            nOutputs = int(splitComm[11]) if int(splitComm[11]) > nOutputs else nOutputs
nBot+=1
nOutputs+=1
bots = []
outputs = []
for i in range(nOutputs):
    outputs.append([])
for i in range(nBot):
    bots.append([[],['', -1],['' , -1]])

for i in range(len(comm)):
    splitComm = comm[i].split(" ")
    if(len(splitComm)==6):
        #value (int) goes to bot (int)
        bots[int(splitComm[5])][0].append(int(splitComm[1]))
    elif(len(splitComm)==12):
        #bot (int) gives low to bot/output (int) and high to bot/output (int)
        bots[int(splitComm[1])][1][0] = splitComm[5]
        bots[int(splitComm[1])][1][1] = int(splitComm[6])
        bots[int(splitComm[1])][2][0] = splitComm[10]
        bots[int(splitComm[1])][2][1] = int(splitComm[11])

queue = deque()
for i in range(nBot):
    if(len(bots[i][0]) == 2 and bots[i][1][1] != -1 and bots[i][2][1] != -1):
        queue.append(i)
part1 = -1
while(not len(queue) == 0):
    curBot = queue.popleft()
    bots[curBot][0].sort()
    lowChip = bots[curBot][0][0]
    lowTo = bots[curBot][1][0]
    lowDest = bots[curBot][1][1]
    highChip = bots[curBot][0][1]
    highTo = bots[curBot][2][0]
    highDest = bots[curBot][2][1]

    if(lowChip == 17 and highChip == 61):
        part1 = curBot
    if(lowTo == "bot"):
        bots[lowDest][0].append(lowChip)
        if(len(bots[lowDest][0]) == 2 and bots[lowDest][1][1] != -1 and bots[lowDest][2][1] != -1):
            queue.append(lowDest)
    elif(lowTo == "output"):
        outputs[lowDest].append(lowChip)
    if(highTo == "bot"):
        bots[highDest][0].append(highChip)
        if(len(bots[highDest][0]) == 2 and bots[highDest][1][1] != -1 and bots[highDest][2][1] != -1):
            queue.append(highDest)
    elif(highTo == "output"):
        outputs[highDest].append(highChip)
    bots[curBot][0] = []
print("Part 1: {}\nPart 2: {}".format(part1, outputs[0][0]*outputs[1][0]*outputs[2][0]))
