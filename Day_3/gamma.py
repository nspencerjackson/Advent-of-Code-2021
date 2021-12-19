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

# function to opposite 
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

def recursion(inArray, inDefault, bitLoc):
    outArray = []
    newBitLoc = bitLoc
    leng = len(inArray)
    if leng > 1:
        # go through until only 1 number left
        outArray = commonDigit(inArray, leng, bitLoc, inDefault)
        newBitLoc += 1
        outArray = recursion(outArray, inDefault, newBitLoc)
    else:
        outArray = inArray
    return outArray

def commonDigit(inArray, inRange, bitLoc, inDefault):
    val = []
    countOne = 0
    countZero = 0
    for i in range(inRange):
        tempV = inArray[i]
        if tempV[bitLoc] == "1":
            countOne += 1
        else:
            countZero += 1
    if countOne > countZero:
        val = rating(inArray, inRange, bitLoc, 1)
    elif countOne < countZero:
        val = rating(inArray, inRange, bitLoc, 0)
    else:
        val = rating(inArray, inRange, bitLoc, inDefault)
    return val

def rating(inArray, inRange, bitLoc, inDigit):
    tempArray = []
    tempValue = ""
    for i in range(inRange):
        tempValue = inArray[i]
        if int(tempValue[bitLoc]) == inDigit:
            tempArray.append(tempValue)
    return tempArray


test = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

#for o in range(4):
    # make it so inDigit doesn't exist, it is calulated by seeing what in 'o' is more popular
ar = recursion(test, 1, 0)
print("gamma: ", ar[0])
print(int(ar[0], 2))
