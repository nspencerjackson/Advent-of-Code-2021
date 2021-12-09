forward = 0
down = 0
l = []
command = ""
length = 0
aim = 0

# function to add or multiply values based on command
def cont(inCommand, inLength, inPos):
    temp = inPos
    # forward command increases distance forward
    if inCommand == "forward":
        temp += inLength
    # down command submerges downward
    elif inCommand == "down":
        temp += inLength
    # increases depth upward
    elif inCommand == "up":
        temp -= inLength
    # multiplies aim by inLength
    elif inCommand == "aim":
        temp *= inLength
    # returns the temp variable which is the inPos variable 
    return temp

# opens and reads the file
with open("controls.txt") as f:
    l = f.readlines()

# length of l list
num = len(l)
tempList = []

# for loop to read all the values in l and split into seperate lists
for i in range(num):
    # splits l list
    tempList = l[i].split(" ")
    # gets the command
    command = tempList[0]
    # gets the lenght
    length = int(tempList[1])
    # if statement to check if command is to go forward
    if (command == "forward"):
        forward = cont(command, length, forward)
    # else submerging / rising
    else:
        down = cont(command, length, down)

print(down, "m down, ", forward, "m forward")

# answer
t = down * forward
print("Part 1: ", t)

# resets all values for 2nd part
forward = 0
down = 0
aim = 0
tempDown = 0


# for list read all values in l
for i in range(num):
    # splits l into command and length
    tempList = l[i].split(" ")
    # gets the command
    command = tempList[0]
    # gets length
    length = int(tempList[1])
    # checks if forward
    if command == "forward":
        # increases forward position
        forward = cont(command, length, forward)
        # decreases depth
        tempDown = cont("aim", length, aim)
        down = cont("down", tempDown, down)
    # else adjusts aim
    else:
        aim = cont(command, length, aim)
    # prints test values
    if i < 12:
        print("forward: ", forward, ", aim: ", aim, ", depth:", down)

second = forward * down

print("Second Part = ", second)

f = open("answer.txt", "w")
f.write(str(second))
f.close()
