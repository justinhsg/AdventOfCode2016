from collections import deque
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

# Credit to Reddit for explaining this
# Essentially prints the reverse of binary of (answer + the product of the numeric arguments in line 1 and 2 (start counting from 0))

tProduct = int(comm[1].split(" ")[1])*int(comm[2].split(" ")[1])
acc = 1
part1 = 0
while(True):
    tClockNumber = int("10"*acc, 2)
    if(tClockNumber > tProduct):
        part1 = tClockNumber - tProduct
        break
    else:
        acc+=1
print("Answer: {}".format(part1))
