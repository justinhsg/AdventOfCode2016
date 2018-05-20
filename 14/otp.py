from hashlib import md5
with open("input.txt", "r") as infile:
    comm = infile.read()
part1 = 0
part2 = 0
hashes = []
stretchHashes = []
index = 0
nKeys = 0
nStretchKeys = 0
def getHash(index):
    if(index < len(hashes)):
        return hashes[index]
    tString = comm+str(index)
    m = md5()
    m.update(tString.encode('utf-8'))
    tString = m.hexdigest()
    hashes.append(tString)
    return hashes[index]

def getStretchHash(index):
    if(index < len(stretchHashes)):
        return stretchHashes[index]
    tString = comm+str(index)
    for i in range(2017):
        m = md5()
        m.update(tString.encode('utf-8'))
        tString = m.hexdigest()
    stretchHashes.append(tString)
    return stretchHashes[index]

while(nKeys<64 or nStretchKeys<64):
    if(nKeys<64):
        tHash = getHash(index)
        triplet = ''
        for i in range(len(tHash)-2):
            if(tHash[i] == tHash[i+1] and tHash[i] == tHash[i+2]):
                triplet = tHash[i]
                break

        if(triplet != ''):
            for j in range(index+1, index+1001):
                nHash = getHash(j)
                if (triplet*5 in nHash):
                    nKeys += 1
                    print("{}%".format(((nKeys+nStretchKeys)*100)//128), end='\r')
                    if(nKeys==64):
                        part1 = index
                    break
    if(nStretchKeys<64):
        tHash = getStretchHash(index)
        triplet = ''
        for i in range(len(tHash)-2):
            if(tHash[i] == tHash[i+1] and tHash[i] == tHash[i+2]):
                triplet = tHash[i]
                break

        if(triplet != ''):
            for j in range(index+1, index+1001):
                nHash = getStretchHash(j)
                if (triplet*5 in nHash):
                    nStretchKeys += 1
                    print("{}%".format(((nKeys+nStretchKeys)*100)//128), end='\r' )
                    if(nStretchKeys==64):
                        part2 = index
                    break
    index += 1



print("Part 1: {}\nPart 2: {}".format(part1, part2))