import math
import random

class Intersection():
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.element = None
        self.number = 0


        # self.name =

class Dalek():
    def __init__(self, pX, pY,):
        self.posX = pX
        self.posY = pY
        self.state = "D"


class Doctor():
    def __init__(self, pGame):
        self.posX = math.floor(pGame.size/2)
        self.posY = math.floor(pGame.size/2)
        self.zappers = 1 #A augmenter de 1 apres chaque niveau
        self.alive = True

    # def zapper(self, pGame):
    #     self.zapper -= 1
    #     for i in pGame.daleks:
    #         if (pGame.daleks[i].posX == (self.posX + 1) or pGame.daleks[i].posX == (self.posX - 1) and pGame.daleks[i].posY == self.posY)\
    #                 or (pGame.daleks[i].posY == (self.posY + 1) or pGame.daleks[i].posY == (self.posY - 1) and pGame.daleks[i].posX == self.posX):
    #
    #             pGame.daleks[i].alive = False


class Game():
    def __init__(self, pSize):
        self.size = pSize
        self.daleks = []
        self.gameArea = []
        self.doctor = Doctor(self)

        for x in range(self.size):
            for y in range(self.size):
                self.gameArea.append(Intersection(x,y))

    def initializeGame(self, nbDaleks=5):

        for j in range(len(self.gameArea)):
            if (self.gameArea[j].column == self.doctor.posX and self.gameArea[j].row == self.doctor.posY):
                self.gameArea[j].element = self.doctor
                self.gameArea[j].number = 1

        dalek = None
        for i in range(nbDaleks):
            x = random.randrange(self.size)
            y = random.randrange(self.size)

            if(x == self.doctor.posX and y == self.doctor.posY):
                dalek = Dalek(x+1,y+2)

            for j in range(len(self.gameArea)):
                if (self.gameArea[j].column == x and self.gameArea[j].row == y):
                    self.gameArea[j].element = dalek
                    self.gameArea[j].number = 2

            self.daleks.append(dalek)


class View():
    def __init__(self, pControler, pGame):
        self.parent = pControler
        self.game = pGame;



    def displayGame(self, game):
        displayGrid = []
        for i in range(game.size):
            row = []
            for j in range(game.size):
                row.append([i,j])
            displayGrid.append(row)

        for intersection in game.gameArea:
            if(intersection.number == 2):
                displayGrid[intersection.column][intersection.row] = "D"

            elif (intersection.number ==1):
                displayGrid[intersection.column][intersection.row] = "W"

            elif (intersection.number ==3):
                displayGrid[intersection.column][intersection.row] = "F"

            else:
                displayGrid[intersection.column][intersection.row] = " "


        for i in displayGrid:
            print(i)






class Controler():
    def __init__(self):
        self.game = Game(8)
        self.game.initializeGame()
        self.view = View(self, self.game)
        self.view.displayGame(self.game)


if __name__ == "__main__":
     c = Controler()
     value = input("up")
