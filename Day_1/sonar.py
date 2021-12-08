lines = []
temp = 0

with open(sweep.txt) as f:
    lines = f.readlines()

for x in lines:
    xInt = int(x)
    if x > temp:

