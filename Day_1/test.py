file1 = open("sweep.txt", 'r')
lines = file1.readlines()
tempArr = [0,0,0]
sumsArray = []
counter = 0
for line in lines:
    curNum = int(line)
    tempArr[counter % 3] = curNum
    counter += 1
    if (counter >= 3):
        sumsArray.append(sum(tempArr))
print("amount: ", len(sumsArray))
counter = 0
lastItem = 0
answer = 0
for i in sumsArray:
    if (counter >= 1):
        if (i > lastItem):
            answer += 1

    lastItem = i
    counter += 1

print(answer)
