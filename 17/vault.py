from hashlib import md5
from collections import deque

with open("input.txt", "r") as infile:
    comm = infile.read()

def isOpen(char):
    if(ord(char)>=ord('b') and ord(char)<=ord('f')):
        return True
    else:
        return False


queue = deque()
queue.append([0,0,comm])
finalkey = ''
firstkey = ''
while(len(queue)!=0):
    curLoc = queue.popleft()
    curX = curLoc[0]
    curY = curLoc[1]
    curPath = curLoc[2]
    if(curX == 3 and curY ==3):
        finalkey = curPath
        firstkey = curPath if firstkey == '' else firstkey
        continue
    m = md5()
    m.update(curPath.encode('utf-8'))
    key=m.hexdigest()[:4]

    if(isOpen(key[0]) and curY!=0):
        newY = curY-1
        newPath = curPath+'U'
        queue.append([curX, newY, newPath])

    if(isOpen(key[1]) and curY!=3):
        newY = curY+1
        newPath = curPath+'D'
        queue.append([curX, newY, newPath])
    if(isOpen(key[2]) and curX!=0):
        newX = curX-1
        newPath = curPath+'L'
        queue.append([newX, curY, newPath])
    if(isOpen(key[3]) and curX!=3):
        newX = curX+1
        newPath = curPath+'R'
        queue.append([newX, curY, newPath])

part1 = firstkey[len(comm):]
part2 = len(finalkey)-len(comm)
print("Part 1: {}\nPart 2: {}".format(part1, part2))



