lines = []
temp = 0
count = 0
first = 0

with open("sweep.txt") as f:
    lines = f.readlines()

for x in lines:
    xInt = int(x)
    if xInt > temp:
        if first == 0:
            first += 1
        else:
            count += 1
        temp = xInt
    elif xInt == temp:
        temp = xInt
    else:
        temp = xInt

print("The count is: ", count)

lines = []
a = 0
b = 0
c = 0
xCount = 1
aTotal = 0
combinedList = []

with open("sweep.txt") as f:
    lines = f.readlines()

for x in lines:
    xInt = int(x)
    if xCount == 3:
        c = xInt
        aTotal = a + b + c
        combinedList.append(aTotal)
    elif xCount == 1:
        a = xInt
    elif xCount == 2:
        b = xInt
    else:
        a = b
        b = c
        c = xInt
        aTotal = a + b + c
        combinedList.append(aTotal) 
    xCount += 1

temp = 0
count = 0
first = 0

print("length = ", len(combinedList))

for y in combinedList:
    if y > temp:
        if first == 0:
            first += 1
        else:
            count += 1
        temp = y
    elif y == temp:
        temp = y
    else:
        temp = y

print("Combined count is: ", count)
