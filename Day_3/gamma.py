l = []
gamma = ""
ep = ""
leng = 0
countOne = 0
countZero = 0
g = 0
e = 0

# function to opposite of the inputted bit
def opposite(inGamma):
    o = ""
    # goes through every bit in the inputted bit-array
    for i in range(len(inGamma)):
        if inGamma[i] == "0":
            o += "1"
        else:
            o += "0"
    return o

# Opens file and reads it
with open("binary.txt") as f:
    l = f.readlines()

# Gets the length of l array
leng = len(l[0])

# Loop for the bits in each line
for x in range(leng-1):
    # Loop for every line in l array
    for y in l:
        # checks in bit is 0 
        if y[x] == "0":
            countZero += 1
        # else bit is 1
        else:
            countOne += 1
    # checks if amount of 0's are more than 1's
    if countZero > countOne:
        gamma += "0"
    else:
        gamma += "1"
    # resets counts
    countZero = 0
    countOne = 0

# reverses gamma bit for epsilon
ep = opposite(gamma)

# get integer for gamma bit
g = int(gamma, 2)

# Gets integer for epsilon bit
e = int(ep, 2)
# Gets the total
total = g * e

print("total = ", total)

#### PART 2 ####

def swap(inFirst, inSecond):
    ret = inSecond
    return ret

def recursion(inArray, inDefault, bitLoc, coTwo):
    outArray = []
    newBitLoc = bitLoc
    leng = len(inArray)
    if leng > 1:
        # go through until only 1 number left
        outArray = commonDigit(inArray, leng, bitLoc, inDefault, coTwo)
        newBitLoc += 1
        outArray = recursion(outArray, inDefault, newBitLoc, coTwo)
    else:
        outArray = inArray
    return outArray

def commonDigit(inArray, inRange, bitLoc, inDefault, coTwo):
    val = []
    countOne = 0
    countZero = 0
    for i in range(inRange):
        tempV = inArray[i]
        if tempV[bitLoc] == "1":
            countOne += 1
        else:
            countZero += 1
    if coTwo:
        temp = countOne
        countOne = swap(countOne, countZero)
        countZero = swap(countZero, temp)
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
ar = recursion(test, 1, 0, False)
print("gamma: ", ar[0])
print(int(ar[0], 2))
co = recursion(test, 0, 0, True)
print(int(co[0], 2))

ox = recursion(l, 1, 0, False)
co = recursion(l, 0, 0, True)

res = int(ox[0], 2) * int(co[0], 2)
print("Ox (", ox, ") x Co2 (", co, ") = ", res)
