from collections import defaultdict
with open("input.txt", "r") as infile:
    raw = infile.read().split("\n")
part1 = ""
part2 = ""
nChar = len(raw[0])
freqs = [defaultdict(lambda: 0) for i in range(nChar)]
for i in raw:
    for j in range(nChar):
        freqs[j][i[j]] += 1

for i in range(nChar):
    unsorted = [(freqs[i][key], key) for key in freqs[i].keys()]
    s = sorted(unsorted)
    part1 += s[-1][1]
    part2 += s[0][1]

print("Part 1: {}\nPart 2: {}".format(part1, part2))
