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
        if inGamma[i] == "0":
            o += "1"
        else:
            o += "0"
    return o

print("opposite of 1100 is: ", opposite("1100"))

with open("binary.txt") as f:
    l = f.readlines()

leng = len(l[0])

for x in range(leng-1):
    print("x is equal to ", x)
    for y in l:
        if y[x] == "0":
            countZero += 1
        else:
            countOne += 1
    if countZero > countOne:
        gamma += "0"
    else:
        gamma += "1"
    countZero = 0
    countOne = 0

ep = opposite(gamma)
print("length of gamma: ", len(gamma))
print("Gamma = ", gamma, ", and Ep= ", ep)
