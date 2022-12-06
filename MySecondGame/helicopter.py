from utils import randcell
import os

class Helicopter:
    def __init__(self, w, h):
         rc = randcell(w, h)
         rx, ry = rc[0], rc[1]
         self.x = rx
         self.y = ry
         self.h = h
         self.w = w
         self.tank = 0
         self.maxtank = 1
         self.score = 0
         self.lives = 20
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def printStats(self):
        print('🧳', self.tank, '/', self.maxtank, sep = '')
        print('🏆', self.score, end = '|')
        print('💚', self.lives)

    def gameOver(self):
        os.system('cls')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('X                               X')
        print('X                               X')
        print('X   GAME OVER, YOUR SCORE IS', self.score, '  X')
        print('X                               X')
        print('X                               X')
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        exit(0)

    def exportData(self):
        return{'score': self.score,
               'lives': self.lives,
               'x': self.x, 'y': self.y,
               'tank': self.tank, 'maxtank': self.maxtank}


    def importData(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.maxtank = data['maxtank'] or 1
        self.lives = data['lives'] or 20
        self.score = data['score'] or 0


