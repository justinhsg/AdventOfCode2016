with open("input.txt", "r") as infile:
    raw = infile.read().split("\n")

pretty = []
for i in raw:
    checksum = i[-6:-1]
    wordsval = i[:-7].split("-")
    letters = "".join(sorted("".join(wordsval[:-1])))
    value = int(wordsval[-1])
    pretty.append([letters, checksum, value])
part1 = 0
for i in pretty:
    store = []
    p = 0
    while(p<len(i[0])):
        val = i[0].count(i[0][p])
        store.append([val, i[0][p]])
        p+=val
    store = sorted(store, key = lambda k: -k[0])
    if("".join([store[j][1] for j in range(5)]) == i[1]):
        part1 += i[2]



pretty = []
for i in raw:
    checksum = i[-6:-1]
    wordsval = i[:-7].split("-")
    letters = wordsval[:-1]
    value = int(wordsval[-1])%26
    pretty.append([letters, checksum, value])


def offset(c, v):
    return chr((ord(c)-ord('a')+v)%26+ord('a'))
part2 = 0
for i in pretty:
    llist = i[0]
    offsets = i[2]
    sentence = []
    for k in range(3):
        word = "".join([offset(c,offsets) for c in llist[k]])
        sentence.append(word)
    if("northpole" in sentence):
        part2 = (raw[pretty.index(i)].split("-")[-1].split("[")[0])
        break
print("Part 1: {}\nPart 2: {}".format(part1, part2))