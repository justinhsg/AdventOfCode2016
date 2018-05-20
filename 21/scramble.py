with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")
part1=""
part2=""

s = "abcdefgh"
p = "fbgdceah"
def swapPos(x,y, st):
    tchar = st[x]
    tchar2 = st[y]
    if(y<x):
        t = x
        x = y
        y = t
    st = st[:x]+st[y]+st[x+1:y]+st[x]+st[y+1:]
    return(st)

def swapLet(a,b, st):
    tposa = st.find(a)
    tposb = st.find(b)
    return (swapPos(tposa, tposb, st))

def rotateLR(lr, x, st):
    x = x%len(st)
    if(lr == "left"):
        st = st[x:]+st[:x]
    else:
        st = st[-x:]+st[:-x]
    return(st)

def rotateIndex(x, st):
    tpos = st.find(x)
    rotAmt = 1+tpos
    if(tpos>=4):
        rotAmt += 1
    return (rotateLR("right", rotAmt, st))


def reverse(x,y, st):
    ts = st[x:y+1]
    reversed = ts[::-1]
    st = st[:x] + reversed + st[y+1:]
    return(st)

def move(x,y, st):
    tchar = st[x]
    scopy = st[:x]+ st[x+1:]
    st = scopy[:y]+tchar+scopy[y:]
    return(st)

for i in range(len(comm)):
    splitComm = comm[i].split(" ")
    if (splitComm[0] == "swap"):
        if(splitComm[1] == "position"):
            s = swapPos(int(splitComm[2]), int(splitComm[5]), s)
        else:
            s = swapLet(splitComm[2], splitComm[5], s)
    elif(splitComm[0] == "rotate"):
        if(len(splitComm)== 4):
            s = rotateLR(splitComm[1], int(splitComm[2]), s)
        else:
            s = rotateIndex(splitComm[6], s)
    elif(splitComm[0] == "reverse"):
        s = reverse(int(splitComm[2]), int(splitComm[4]), s)
    elif(splitComm[0]=="move"):
        s = move(int(splitComm[2]), int(splitComm[5]), s)

for i in range(len(comm)-1, -1, -1):
    splitComm = comm[i].split(" ")
    if (splitComm[0] == "swap"):
        if(splitComm[1] == "position"):
            p = swapPos(int(splitComm[2]), int(splitComm[5]), p)
        else:
            p = swapLet(splitComm[2], splitComm[5], p)
    elif(splitComm[0] == "rotate"):
        if(len(splitComm)== 4):
            p = rotateLR("left" if splitComm[1] == "right" else "right", int(splitComm[2]), p)
        else:
            tLoc = p.find(splitComm[6])
            if(tLoc == 0 or tLoc == 1):
                p = rotateLR("left", 1, p)
            elif(tLoc == 2):
                p = rotateLR("right", 2, p)
            elif(tLoc == 3):
                p = rotateLR("left", 2, p)
            elif(tLoc == 4):
                p = rotateLR("right", 1, p)
            elif(tLoc == 5):
                p = rotateLR("left", 3, p)
            elif(tLoc == 7):
                p = rotateLR("left", 4, p)
    elif(splitComm[0] == "reverse"):
        p = reverse(int(splitComm[2]), int(splitComm[4]), p)
    elif(splitComm[0]=="move"):
        p = move(int(splitComm[5]), int(splitComm[2]), p)

part1 = s
part2 = p

print("Part 1: {}\nPart 2: {}".format(part1, part2))