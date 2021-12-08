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
    return temp

with open("controls.txt") as f:
    l = f.readlines()

num = len(l)

for i in range(num):
    temp = l[i].split(" ")
    #commandList.append(temp[0])
    #lengthList.append(int(temp[1]))
    command = temp[0]
    length = int(temp[1])
    if (command == "forward"):
        forward = cont(command, length, forward)
    else:
        down = cont(command, length, down)

print(down, "m down, ", forward, "m forward")

t = down * forward

print(t)
