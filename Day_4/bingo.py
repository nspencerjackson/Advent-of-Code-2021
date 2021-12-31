from bingoboards import *

s = "4  8 12 5"
ar = s.split()

# have classes for each bingo board

x = BingoBoard(1, [[1,2,3,4],[6,7,8,9],[11,12,13,14],[5,10,15,16]], 4, 4)

for i in range(4):
    print(ar[i])
    x.updateBingo(int(ar[i]))
    x.getBingo()

e = x.checkBingo()
print(e)
#x.updateBingo(4)
#x.getBingo()
#x.updateBingo(8)
#x.getBingo()
#x.updateBingo(12)
#x.getBingo()
#x.updateBingo(5)
#x.getBingo()

#b = x.checkBingo()
#print(b)
