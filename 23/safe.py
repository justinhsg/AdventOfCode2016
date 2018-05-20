from collections import deque
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

pt = 0
registers = {'a': 7, 'b':0, 'c':0, 'd':0}
toggle = []
for i in range(len(comm)):
    toggle.append(False)

def valueOf(inVal):
    if(inVal in registers):
        return registers[inVal]
    else:
        return int(inVal)

counter = 0
while(pt>=0 and pt<len(comm)):

    splitComm = comm[pt].split(" ")
    if(splitComm[0] == "tgl"):
        if(pt+valueOf(splitComm[1]) >= 0 and pt+valueOf(splitComm[1])<len(comm)):

            toggledComm = comm[pt+valueOf(splitComm[1])].split()
            if(len(toggledComm) == 2):
                if(toggledComm[0] == "inc"):
                    comm[pt+valueOf(splitComm[1])] = "dec"+comm[pt+valueOf(splitComm[1])][3:]
                else:
                    comm[pt+valueOf(splitComm[1])] = "inc"+comm[pt+valueOf(splitComm[1])][3:]
            else:
                if(toggledComm[0] == "jnz"):
                    comm[pt+valueOf(splitComm[1])] = "cpy"+comm[pt+valueOf(splitComm[1])][3:]
                else:
                    comm[pt+valueOf(splitComm[1])] = "jnz"+comm[pt+valueOf(splitComm[1])][3:]
        pt+=1
    elif(splitComm[0] == "cpy"):
        if(splitComm[2] not in registers):
            pt+=1
            print("whoops")
        else:
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
part2 = 1
for i in range(len(comm)):
    splitComm = comm[i].split()
    if(splitComm[1] not in registers):
        if(int(splitComm[1]) > 50):
            part2 *= int(splitComm[1])
fact = 1
for i in range(1,13):
    fact *= i
part2 += fact

print("Part 1: {}\nPart 2: {}".format(part1, part2))

#
#6 -> 7290
#7 -> 11610
#8 -> 46890
#
#