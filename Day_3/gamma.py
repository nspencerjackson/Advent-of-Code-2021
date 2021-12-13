l = []
gamma = ""
ep = ""
leng = 0
countOne = 0
countZero = 0
g = 0
e = 0

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
#print("Gamma = ", gamma, ", and Ep= ", ep)

g = int(gamma, 2)
e = int(ep, 2)
total = g * e

print("total = ", total)

#### PART 2 ####

def commonDigit(inArray, inDigit, inRange, bitLoc):
    tempArray = []
    tempValue = ""
    for i in range(inRange):
        tempValue = inArray[i]
        if int(tempValue[bitLoc]) == inDigit:
            tempArray.append(tempValue)
    return tempArray

def rating(inArray, inRange, bitLoc):
    tempArray = []
    tempValue = ""
    for i in range(inRange):
        tempValue = inArray[i]


test = ["11110", "10110", "10111", "10101", "11100", "10000", "11001", "01101", "00000", "00110", "01001"]

for o in range(4):
    # make it so inDigit doesn't exist, it is calulated by seeing what in 'o' is more popular
    ar = commonDigit(test, 1, 11, o)
    print(ar)
