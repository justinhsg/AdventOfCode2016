import re
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")


def isAbba(inText):
    for i in range(len(inText)-3):
        if(inText[i]==inText[i+3] and inText[i+1]==inText[i+2] and inText[i]!=inText[i+2]):
            return True
    return False




nTLS = 0
nSSL = 0
for i in range(len(comm)):
    tempIP = comm[i]
    phrases = re.split(r'\W', tempIP)
    allowed = []
    banned = []
    babList = []

    for j in range(len(phrases)):
        if(j%2==0):
            allowed.append(phrases[j])
        else:
            banned.append(phrases[j])
    isTLS = False
    isSSL = False

    for j in range(len(allowed)):
        tWord = allowed[j]
        if(isAbba(tWord)):
            isTLS = True
        for l in range(len(tWord)-2):
            if(tWord[l]==tWord[l+2]):
                babList.append(tWord[l+1]+tWord[l]+tWord[l+1])

    for k in range(len(banned)):
        tWord = banned[k]
        if(isAbba(tWord)):
            isTLS = False
        for m in range(len(babList)):
            if babList[m] in tWord:
                isSSL = True
                break
        if isSSL:
            break

    nTLS += 1 if isTLS else 0
    nSSL += 1 if isSSL else 0
print("Part 1: {}\nPart 2: {}".format(nTLS, nSSL))
