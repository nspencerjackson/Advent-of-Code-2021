from bingoboards import *

ar = []

# have classes for each bingo board

x = BingoBoard(1, [[1,2,3,4],[6,7,8,9],[11,12,13,14],[5,10,15,16]], 4, 4)

x.updateBingo(4)
x.getBingo()
x.updateBingo(8)
x.getBingo()
x.updateBingo(12)
x.getBingo()
x.updateBingo(5)
x.getBingo()

b = x.checkBingo()
print(b)
