
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
            for i in range((len(self.bingo - 1)), 0, -1):
                if self.bingo[i][i] == "x":
                    temp += 1
            if temp == self.x:
                self.bingoBool = True

    def checkBingo(self):
        retBool = False
        # Checks Horizontal Lines
        temp = self.checkLine(False)
        if temp:
            retBool = True
        else:
            # Checks Vertical Lines
            temp = self.checkLine(True)
            if temp:
                retBool = True

        return retBool
