
class BingoBoard:
    def __init__(self, inNumber, inBoard, inX, inY):
        self.number = inNumber
        self.board = inBoard
        self.bingo = []
        self.x = inX
        self.y = inY
        self.bingoBool = False
        for i in range(self.y):
            temp = []
            for o in range(self.x):
                temp.append("o")
            self.bingo.insert(i, temp)
            
    def getBingo(self):
        print(self.bingo)

    def getBoard(self):
        print(self.board)

    def getNum(self):
        return self.number

    def updateBingo(self, inNum):
        for i in range(self.y):
            for o in range(self.x):
                if self.board[i][o] == inNum:
                    self.bingo[i][o] = "x"
                    break
    
    def checkLine(self, rev):
        for i in range(self.x):
            temp = 0
            for o in range(self.y):   
                if not rev:
                    if self.bingo[i][o] == "x":
                        temp += 1
                else:
                    if self.bingo[o][i] == "x":
                        temp += 1
            if temp == self.x:
                self.bingoBool = True
                break
        return self.bingoBool

    def checkDiagonal(self):
        temp = 0
        for i in range(self.x):
            if self.bingo[i][i] == "x":
                temp += 1
        if temp == self.x:
            self.bingoBool = True
        else:
            temp = 0
            decX = self.y - 1
            for i in range(self.x):
                if self.bingo[decX][i] == "x":
                    temp += 1
                decX -= 1
            if temp == self.x:
                self.bingoBool = True

    def checkBingo(self):
        retBool = False
        # Checks Horizontal Lines
        self.checkLine(False)
        if not self.bingoBool:
            # Checks Vertical Lines
            self.checkLine(True)
            if not self.bingoBool:
                # Checks Diagonal Lines
                self.checkDiagonal()

        return self.bingoBool

    def getTotal(self):
        total = 0
        for i in range(self.x):
            for o in range(self.y):
                if self.bingo[i][o] == "o":
                    total += int(self.board[i][o])
        return total
