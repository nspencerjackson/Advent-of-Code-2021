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
