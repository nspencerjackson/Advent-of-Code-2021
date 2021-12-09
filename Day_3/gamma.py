l = []
gamma = []
ep = []
leng = 0
countOne = 0
countZero = 0

#x = int("111111", 2)
#print(x)

with open("binary.txt") as f:
    l = f.readlines()

leng = len(l[0])

for x in l:
    x
