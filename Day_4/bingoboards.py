
class BingoBoard:
    def __init__(self, inNumber, inBoard, inX, inY):
        self.number = inNumber
        self.board = inBoard
        self.bingo = []
        self.x = inX
        self.y = inY
        self.count = []
        for i in range(self.y):
            temp = []
            for o in range(self.x):
                temp.append("o")
            self.bingo.insert(i, temp)
            
    def getBingo(self):
        print(self.bingo)

    def checkBingo(self, i, o):
        if i == 0 and o == 0:


    def updateBingo(self, inNum):
        for i in range(self.y):
            for o in range(self.x):
                if self.board[i][o] == inNum:
                        self.bingo[i][o] = checkBingo(i, o)
                    break

    def checkBingo(self):
        tempX = 0
        tempY = 0
        for i in range(self.y):
            for o in range(self.x):
                if self.bingo[i][o] == "x":
                    if i == 0 and o == 0:
                        
        if self.bingo
