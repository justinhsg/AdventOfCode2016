with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

floors = []
floors2 = []
for i in range(len(comm)):
    floors.append(comm[i].count("generator") + comm[i].count("microchip"))
    floors2.append(comm[i].count("generator") + comm[i].count("microchip"))
floors2[0] += 4
part1 = 0
for i in range(len(floors)-1):
    part1 += 2*floors[i] - 3
    tVal = floors[i]
    floors[i+1] += tVal
part2 = 0
for i in range(len(floors2)-1):
    part2 += 2*floors2[i] - 3
    tVal = floors2[i]
    floors2[i+1] += tVal
print("Part 1: {}\nPart 2: {}".format(part1, part2))