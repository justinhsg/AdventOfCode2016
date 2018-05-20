with open("input.txt", "r") as infile:
    comm = int(infile.read())
elves = []
nRemoved = 0
position = 0
pointer = []

for i in range(comm):
    pointer.append((i+1)%comm)

while(nRemoved<(comm-1)):
    removedElf = pointer[position]
    nextElf = pointer[removedElf]
    pointer[removedElf] = -1
    pointer[position] = nextElf
    position = nextElf
    nRemoved+=1
part1 = position+1


memory = []
memory.append(-1)
memory.append(-1)
memory.append(0)

for i in range(3,comm+1):
    position = 0
    removedPos = i//2
    if(memory[i-1]+1 >= removedPos):
        memory.append((memory[i-1]+2)%i)
    else:
        memory.append((memory[i-1]+1)%i)
for i in range(len(memory)):
    memory[i] = memory[i] + 1
part2 = memory[-1]

print("Part 1: {}\nPart 2: {}".format(part1, part2))