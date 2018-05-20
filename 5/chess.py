from hashlib import md5
with open("input.txt", "r") as infile:
    input = infile.read()

password = ""
index = 0
found = 0
pass2 = ["" for i in range(8)]

while(found < 8):
    m = md5()
    m.update((input + str(index)).encode())
    hash = m.hexdigest()
    if(hash[:5] == '00000' and len(password) < 8):
        password += hash[5]

    if(hash[:5] == '00000' and hash[5].isnumeric()):
        if(int(hash[5]) < 8):
            if(pass2[int(hash[5])] == ""):
                pass2[int(hash[5])] = hash[6]
                found += 1
                print("{}%".format(found*100//8), end="\r")

    index += 1
print("Part 1: {}\nPart 2: {}".format(password, "".join(pass2)))