from collections import deque
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

pt = 0
registers = {'a': 0, 'b':0, 'c':0, 'd':0}

def valueOf(inVal):
    if(inVal in registers):
        return registers[inVal]
    else:
        return int(inVal)


while(pt>=0 and pt<len(comm)):
    splitComm = comm[pt].split(" ")
    if(splitComm[0] == "cpy"):
        registers[splitComm[2]] = valueOf(splitComm[1])
        pt+=1
    elif(splitComm[0] == "inc"):
        registers[splitComm[1]] += 1
        pt+=1
    elif(splitComm[0] == "dec"):
        registers[splitComm[1]] -= 1
        pt+=1
    elif(splitComm[0] == "jnz"):
        if(valueOf(splitComm[1])!=0):
            pt+=valueOf(splitComm[2])
        else:
            pt+=1
part1 = registers['a']
registers = {'a': 0, 'b':0, 'c':1, 'd':0}
pt = 0
while(pt>=0 and pt<len(comm)):
    splitComm = comm[pt].split(" ")
    if(splitComm[0] == "cpy"):
        registers[splitComm[2]] = valueOf(splitComm[1])
        pt+=1
    elif(splitComm[0] == "inc"):
        registers[splitComm[1]] += 1
        pt+=1
    elif(splitComm[0] == "dec"):
        registers[splitComm[1]] -= 1
        pt+=1
    elif(splitComm[0] == "jnz"):
        if(valueOf(splitComm[1])!=0):
            pt+=valueOf(splitComm[2])
        else:
            pt+=1
part2 = registers['a']
print("Part 1: {}\nPart 2: {}".format(part1, part2))