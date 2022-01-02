from bingoboards import *

#s = "4  8 12 5"
#ar = s.split()

# have classes for each bingo board

#x = BingoBoard(1, [[1,2,3,4],[6,7,8,9],[11,12,13,14],[5,10,15,16]], 4, 4)

#for i in range(4):
    #print(ar[i])
    #x.updateBingo(int(ar[i]))
    #x.getBingo()

#b = x.checkBingo()
#print(b)

# opens file
with open("boards.txt") as f:
    ar = f.readlines()

# Gets length of ar array
leng = len(ar)

#for i in range(leng):
    #print(ar[i])

bingoNum = ar[0].split("\n")
temp = bingoNum[0]
bingoNum = temp.split(",")
#print("Bingo numbers: ", bingoNum)

brd = []
totalBoards = 0
board = []
tempBoard = []
boardCount = 0
for i in range(leng):
    if i != 0:
        temp = ar[i]
        if temp == "\n":
            boardCount = 0
            board = []
        else:
            boardCount += 1
            #print("Board: ", boardCount)
            tempBoard = temp.split("\n")
            temp = tempBoard[0]
            board.append(temp.split())
            if boardCount == 4:
                totalBoards += 1
                brd.append(BingoBoard(totalBoards, board, 5, 5))
            #print(board)

leng = len(bingoNum)

for i in range(leng):
    for o in range(len(brd)):
        brd[o].updateBingo(bingoNum[i])
        x = brd[o].checkBingo() 
        if x:
            print("BINGO: ", x, ", on board: ", brd[o].getNum())
            num = bingoNum[i]
            total = brd[o].getTotal()

            break
    if x:
        multi = int(num) * int(total)
        print("num: ", num, ", for total of: ", total)
        print("Combined: ", multi)
        break

amountOfBoards = len(brd)
bingoedBoards = 0
brk = False
num = 0
total = 0
# second part of puzzle
for i in range(leng):
    for o in range(len(brd)):
        brd[o].updateBingo(bingoNum[i])
        x = brd[o].checkBingo() 
        if x:
            bingoedBoards += 1
            print("BINGO: ", x, ", on board: ", brd[o].getNum())
            #print("BingoBoards: ", bingoedBoards, " = ", amountOfBoards)
            x = False
            if bingoedBoards == amountOfBoards:
                num = bingoNum[i]
                total = brd[o].getTotal()
                print("num: ", num, ", for total of: ", total)

multi = int(num) * int(total)
print("Combined: ", multi)

