from bingoboards import *

ar = []

# have classes for each bingo board

x = BingoBoard(1, [[1,2,3,4],[6,7,8,9],[11,12,13,14],[5,10,15,16]], 4, 4)

x.updateBingo(4)
x.getBingo()
x.updateBingo(9)
x.getBingo()
x.updateBingo(14)
x.getBingo()
x.updateBingo(16)
x.getBingo()
