with open("input.txt", "r") as infile:
    comm = infile.read()
DISCSIZE = 272
DISC2SIZE = 35651584
part1 = ''
part2 = ''

def dragon(inString):
    outString = inString + '0'
    for i in range(len(inString)):
        outString += '0' if inString[len(inString)-1-i] == '1' else '1'
    return outString

def checksum(inString):
    if(len(inString)%2 == 1):
        return inString
    outString = ''
    for i in range(int(len(inString)/2)):
        outString += '1' if inString[2*i] == inString[2*i+1] else '0'
    return outString


fullData = comm
while(len(fullData)<DISCSIZE):
    fullData = dragon(fullData)

disc = fullData[:DISCSIZE]
part1 = checksum(disc)
while(len(part1)%2==0):
    part1 = checksum(part1)

fullData = comm
while(len(fullData)<DISC2SIZE):
    fullData = dragon(fullData)

disc = fullData[:DISC2SIZE]
part2 = checksum(disc)
while(len(part2)%2==0):
    part2 = checksum(part2)

print("Part 1: {}\nPart 2: {}".format(part1, part2))