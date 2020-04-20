import pygame

pygame.init()
#
# pygame.display.set_caption("Game")
#
# win = pygame.display.set_mode((800, 600))

class perses(object):
    def __init__(self, win):
        # self.winWidth = 800
        # self.winWidth = 600
        self.win = win
        self.sprites = [pygame.image.load('img/hendalf.png'), \
                        pygame.image.load('img/32x32_stuent.png'),
                        pygame.image.load('img/fed.png')]

        self.hendWidth, self.hendHeight = 126, 183
        self.studdWidth, self.studHeight = 96, 108

    def drawHend(self, x, y):
        '''
            Draws Hendalf
        '''
        self.win.blit(self.sprites[0], (x - self.hendWidth, \
                      y - self.hendHeight))

    def drawFed(self, x, y):
        '''
            Draws Math guru
        '''
        self.win.blit(self.sprites[2], (x, y))

    def drawStud(self, x, y):
        '''
            Draws Student
        '''
        self.win.blit(self.sprites[1], (x, y - self.studHeight))

class dialogue(object):
    dialogue = [pygame.image.load('img/dLT20x16.png'), \
                pygame.image.load('img/dRT20x16.png'), \
                pygame.image.load('img/dLD20x16.png'), \
                pygame.image.load('img/dRD41x33.png'), \
                pygame.image.load('img/dhor8x5.png'), \
                pygame.image.load('img/dver5x8.png'), \
                pygame.image.load('img/LdRD41x33.png'), \
                pygame.image.load('img/LdLD20x16.png')]

    def __init__(self, win, width, height, x, y, toTheRight = 'True', \
                 textToDraw = ''):
        self.win = win
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.toTheRight = toTheRight
        self.textToDraw = textToDraw
        self.maxSymbolsInLine = int(width / 10) - 3

    def drawText(self):
        '''
            Draws text fitted to dialogue window
        '''
        font = pygame.font.SysFont('Lucida Console', 16)
        splitedText = [self.textToDraw[i:i + self.maxSymbolsInLine] \
        for i in range(0, len(self.textToDraw), self.maxSymbolsInLine)]
        for i in range(len(splitedText)):
            text = font.render(splitedText[i], 1, (255, 255, 255))
            self.win.blit(text, (self.x + 20, self.y + 20 * (i + 1)))

    def drawDialogueWin(self):
        '''
            Draws dialogue window with coordinates
        '''
        for i in range(self.height):
            for j in range(self.width):
                if i == 0:
                    if j == 0:
                        self.win.blit(self.dialogue[0], \
                        (self.x + j, self.y + i))
                    elif j < self.width - 20 and j > 15 and j % 8 == 0:
                        self.win.blit(self.dialogue[-4], \
                        (self.x + j, self.y + i))
                    elif j == self.width - 20:
                        self.win.blit(self.dialogue[1], \
                        (self.x + j, self.y + i))
                elif i > 16 and i < self.height - 17:
                    if  j == 4 or j == + self.width - 5:
                        self.win.blit(self.dialogue[-3], \
                        (self.x + j, self.y + i))
                elif i == self.height - 17:
                    if self.toTheRight:
                        if j < + self.width - 41 and j > + 15 and j % 8 == 0:
                            self.win.blit(self.dialogue[-4], \
                            (self.x + j, self.y + i + 10))
                        if j == 0 :
                            self.win.blit(self.dialogue[2], \
                            (self.x + j, self.y + i))
                        elif j ==  + self.width - 41:
                            self.win.blit(self.dialogue[-5], \
                            (self.x + j, self.y + i + 4))
                    else:
                        if j < + self.width - 17 and j > + 39 and j % 8 == 0:
                            self.win.blit(self.dialogue[-4], \
                            (self.x + j, self.y + i + 10))
                        if j == 0 :
                            self.win.blit(self.dialogue[-2], \
                            (self.x + j, self.y + i))
                        elif j ==  + self.width - 17:
                            self.win.blit(self.dialogue[-1], \
                            (self.x + j, self.y + i + 4))

        self.drawText()

class DialogueWindow(object):

    def __init__(self, win):
        self.win = win
        self.run = True
        self.clock = pygame.time.Clock()
        self.guys = perses(self.win)
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        self.dialogueWindowList1 = [dialogue(self.win, 330, 80, 350, 195, \
        True, 'Hello student! I am Romanyuk. YOU SHALL NOT PASS the test'),
        dialogue(self.win, 330, 60, 100, 290, False, \
        'I dont think so. Lets get it'),dialogue(self.win, 350, 90, 330, 365, \
        True, 'You need your option firstly, sofind reminder of division of your creedit card number by 4')]
        self.dialogueWindowList2 = [dialogue(self.win, 340, 90, 350, 185, \
        True, 'You`ve failed your test. You have one night to learn numbers and to attempt again'),
        dialogue(self.win, 370, 80, 100, 280, False, \
        'But I can`t learn them by myself, how can I do this?!'), \
        dialogue(self.win, 350, 100, 330, 365, True, \
        'Go to the UCU Dungeon and there you`ll meet numbers guru - math analisys professor')]
        self.dialogueWindowList3 = [dialogue(self.win, 350, 80, 100, 165, \
        False, 'Hello, I am student from UCU and I`ve failed my programming exam'),
        dialogue(self.win, 365, 70, 100, 280, False, \
        'Now I have only one night to learn  theese numbers'), \
        dialogue(self.win, 370, 90, 330, 365, True, \
        'Ok, I`ll teach you, let`s begin with even numbers: clear all numbers, which aren`t even')]
        self.dialogueWindowList4 = [dialogue(self.win, 370, 95, 340, 215, \
        True, 'Now you have to clear every second number, then every third and then every seventh'), \
        dialogue(self.win, 390, 60, 310, 365, True, \
        'Thst`s how you create Lucky numbers')]
        self.dialogueWindowList5 = [dialogue(self.win, 370, 75, 340, 315, \
        True, 'Now let`s move to Ulam`s numbers. Just google it and exclude others')]
        self.dialogueWindowList6 = [dialogue(self.win, 350, 80, 100, 300, \
        False, 'I`m ready for my second attempt! Now I`m gonna make it!'),
        dialogue(self.win, 95, 60, 600, 380, True, 'No way.')]
        self.dialogueWindowList7 = [dialogue(self.win, 95, 60, 600, 380, \
        True, 'WOW!!!')]

    def redrawGameWindow1(self, numOfBlock):
        '''
            Draws game window for dialogue 1
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList1[i].drawDialogueWin()
        except:
            self.run = False
        self.guys.drawHend(790, 590)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def redrawGameWindow2(self, numOfBlock):
        '''
            Draws game window for dialogue 2
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList2[i].drawDialogueWin()
        except:
            self.run1 = False
        self.guys.drawHend(790, 590)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def redrawGameWindow3(self, numOfBlock):
        '''
            Draws game window for dialogue 3
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList3[i].drawDialogueWin()
        except:
            self.run3 = False
        self.guys.drawFed(640, 440)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def redrawGameWindow4(self, numOfBlock):
        '''
            Draws game window for dialogue 4
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList4[i].drawDialogueWin()
        except:
            self.run = False
        self.guys.drawFed(640, 440)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def redrawGameWindow5(self, numOfBlock):
        '''
            Draws game window for dialogue 5
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList5[i].drawDialogueWin()
        except:
            self.run = False
        self.guys.drawFed(640, 440)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def redrawGameWindow6(self, numOfBlock):
        '''
            Draws game window for dialogue 6
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList6[i].drawDialogueWin()
        except:
            self.run = False
        self.guys.drawHend(790, 590)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def redrawGameWindow7(self, numOfBlock):
        '''
            Draws game window for dialogue 7
        '''
        try:
            for i in range(0, numOfBlock + 1):
                self.dialogueWindowList7[i].drawDialogueWin()
        except:
            self.run = False
        self.guys.drawHend(790, 590)
        self.guys.drawStud(10, 590)
        font = pygame.font.SysFont('Lucida Console', 13)
        text = font.render('To continue press Space', 1, (255, 255, 255))
        self.win.blit(text, (280, 580))
        pygame.display.update()

    def runDialogue1(self):
        '''
            Runs proccesses for diaolgue 1
        '''
        self.run = True
        self.numOfKeysPressed = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList1):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList1):
                self.run = False

            self.redrawGameWindow1(self.numOfKeysPressed)

    def runDialogue2(self):
        '''
            Runs proccesses for diaolgue 2
        '''
        self.run = True
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList2):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList2):
                self.run = False

            self.redrawGameWindow2(self.numOfKeysPressed)

    def runDialogue3(self):
        '''
            Runs proccesses for diaolgue 3
        '''
        self.run = True
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList3):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList3):
                self.run = False

            self.redrawGameWindow3(self.numOfKeysPressed)

    def runDialogue4(self):
        '''
            Runs proccesses for diaolgue 4
        '''
        self.run = True
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList4):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList4):
                self.run = False

            self.redrawGameWindow4(self.numOfKeysPressed)

    def runDialogue5(self):
        '''
            Runs proccesses for diaolgue 5
        '''
        self.run = True
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList5):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList5):
                self.run = False

            self.redrawGameWindow5(self.numOfKeysPressed)

    def runDialogue6(self):
        '''
            Runs proccesses for diaolgue 6
        '''
        self.run = True
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList6):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList6):
                self.run = False

            self.redrawGameWindow6(self.numOfKeysPressed)

    def runDialogue7(self):
        '''
            Runs proccesses for diaolgue 7
        '''
        self.run = True
        self.numOfKeysPressed = 0
        self.pressKeyLoop = 0
        #main loop
        while self.run:

            self.clock.tick(24)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            if self.pressKeyLoop >= 0:
                self.pressKeyLoop += 1
            if self.pressKeyLoop > 3:
                self.pressKeyLoop = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed < len(self.dialogueWindowList7):
                self.numOfKeysPressed += 1
            if keys[pygame.K_SPACE] and self.pressKeyLoop == 0 and \
                    self.numOfKeysPressed == len(self.dialogueWindowList7):
                self.run = False

            self.redrawGameWindow7(self.numOfKeysPressed)
