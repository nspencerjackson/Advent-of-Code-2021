linesArray = []
temp = []
arr = []
startLine = []
endLine = []

# Opens file and reads file
with open("vents.txt") as f:
    temp = f.readlines()

for i in range(len(temp)):
    tempLine = temp[i].split("\n")
    arr.append(tempLine[0].split(" -> "))

for i in range(len(arr)):
    startLine.append(arr[i][0].split(","))
    endLine.append(arr[i][1].split(","))

#print(arr)
