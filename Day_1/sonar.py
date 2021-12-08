lines = []
temp = 0
count = 0

with open(sweep.txt) as f:
    lines = f.readlines()

for x in lines:
    xInt = int(x)
    if xInt > temp:
        count += 1
        temp = x
    else:
        temp = x

print("The count is: ", count)
