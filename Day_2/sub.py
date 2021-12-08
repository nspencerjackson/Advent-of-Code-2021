forward = 0
down = 0
l = []
command = ""
length = 0
aim = 0

def cont(inCommand, inLength, inPos):
    temp = inPos
    if inCommand == "forward":
        temp += inLength
    elif inCommand == "down":
        temp += inLength
    elif inCommand == "up":
        temp -= inLength
    elif inCommand == "aim":
        temp *= inLength
    return temp

with open("controls.txt") as f:
    l = f.readlines()

num = len(l)
tempList = []

for i in range(num):
    tempList = l[i].split(" ")
    #commandList.append(temp[0])
    #lengthList.append(int(temp[1]))
    command = tempList[0]
    length = int(tempList[1])
    if (command == "forward"):
        forward = cont(command, length, forward)
    else:
        down = cont(command, length, down)

print(down, "m down, ", forward, "m forward")

t = down * forward

forward = 0
down = 0
aim = 0

print("Part 1: ", t)

for i in range(num):
    tempList = l[i].split(" ")
    command = tempList[0]
    length = int(tempList[1])
    if command == "forward":
        forward = cont(command, length, forward)
        aim = cont("aim", length, aim)
        down = cont("down", length, aim)
    else:
        aim = cont(command, length, aim)
    print("Aim: ",aim)

second = forward * down

print("Second Part = ", second)

f = open("answer.txt", "w")
f.write(str(second))
f.close()
