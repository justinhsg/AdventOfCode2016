import re
with open("input.txt", "r") as infile:
    comm = infile.read()

part1 = 0
i = 0
while (i<len(comm)):
    if(comm[i]=="("):
        openParen = i
        closeParen = i
        for j in range(i, len(comm)):
            if(comm[j]==")"):
                closeParen = j
                break
        params = comm[i+1:j].split("x")
        part1 += int(params[0])*int(params[1])
        i= closeParen+int(params[0])+1
    else:
        i+=1
        part1+=1

def eval(text, times):
    if("(" not in text):
        return len(text)*times
    else:
        openPos = text.find('(')
        closePos = text.find(')')
        params = text[openPos+1:closePos].split("x")
        encasedText = text[closePos+1:closePos+int(params[0])+1]
        if(closePos+int(params[0])+1 == len(text)):
            return (openPos + eval(encasedText, int(params[1])))*times
        else:
            return (openPos + eval(encasedText, int(params[1])) + eval(text[closePos+int(params[0])+1:],1))*times

print("Part 1: {}\nPart 2: {}".format(part1, eval(comm,1)))
