l = []
gamma = ""
ep = ""
leng = 0
countOne = 0
countZero = 0

#x = int("111111", 2)
#print(x)

def opposite(inGamma):
    o = ""
    for i in range(len(inGamma)):
        if

with open("binary.txt") as f:
    l = f.readlines()

leng = len(l[0])

for x in range(leng):
    for y in l:
        if y[x] == "0":
            countZero += 1
        else:
            countOne += 1
    if countZero > countOne:
        gamma += str(countZero)
    else:
        gamma += str(countOne)

ep = opposite(gamma)
