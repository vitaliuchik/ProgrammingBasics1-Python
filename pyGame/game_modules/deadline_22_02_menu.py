import pygame
import game_modules.deadline_22_02_dialogue_module as dialogue_module

pygame.init()

win = pygame.display.set_mode((800, 600))

class buttons(object):
    buttons = [pygame.image.load('img/P_Y.png'), pygame.image.load('img/P_N.png'), \
               pygame.image.load('img/E_Y.png'), pygame.image.load('img/E_N.png')]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.playButWidth, self.playButHeight = 114, 40
        self.exitButWidth, self.exitButWidth = 100, 40

    def drawOnPlayButton(self):
        '''
            Draws highlighted play button
        '''
        win.blit(self.buttons[1], (self.x, self.y))
        win.blit(self.buttons[-2], (self.x + 7, \
                 self.y + 1.5 * self.playButHeight))

    def drawButtons(self):
        '''
            Draws buttons
        '''
        win.blit(self.buttons[0], (self.x, self.y))
        win.blit(self.buttons[-2], (self.x + 7, \
                 self.y + 1.5 * self.playButHeight))

    def drawOnExitButton(self):
        '''
        Draws highlighted exit button
        '''
        win.blit(self.buttons[0], (self.x, self.y))
        win.blit(self.buttons[-1], (self.x + 7, \
                 self.y + 1.5 * self.playButHeight))

class background(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprites = [pygame.image.load('img/newton_sprt.png')]
    def drawNewton(self):
        '''
            draws Newtons sprite
        '''
        win.blit(self.sprites[0], (690, 480))

    def drawMenuManual(self):
        '''
            draws menu manual
        '''
        font = pygame.font.SysFont('Lucida Console', 13)
        line = ['Use arrow keys to navigate', \
                'Use Space key instead of Enter']
        for i in range(2):
            text = font.render(line[i], 1, (255, 255, 255))
            win.blit(text, (5, 15 * (i + 1)))

    def drawReservation(self):
        '''
            draws reservatin text
        '''
        font = pygame.font.SysFont('Lucida Console', 13)
        line = ['CoolTeam Game [Version 1.0.0]', \
                '(c) CoolTeam Corp. 2018. All rights reserved']
        for i in range(2):
            text = font.render(line[i], 1, (255, 255, 255))
            win.blit(text, (5, 550 + 15 * (i + 1)))

class dialogue(object):
    dialogue = [pygame.image.load('img/dLT20x16.png'), \
                pygame.image.load('img/dRT20x16.png'), \
                pygame.image.load('img/dLD20x16.png'), \
                pygame.image.load('img/dRD41x33.png'), \
                pygame.image.load('img/dhor8x5.png'), \
                pygame.image.load('img/dver5x8.png')]

    def __init__(self, width, height, x, y, textToDraw = ''):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.textToDraw = textToDraw
        self.maxSymbolsInLine = int(width / 10)

    def drawText(self):
        '''
            Draws text fitted to dialogue window
        '''
        font = pygame.font.SysFont('Lucida Console', 16)
        splitedText = [self.textToDraw[i:i + self.maxSymbolsInLine] \
        for i in range(0, len(self.textToDraw), self.maxSymbolsInLine)]
        for i in range(len(splitedText)):
            text = font.render(splitedText[i], 1, (255, 255, 255))
            win.blit(text, (self.x + 20, self.y + 20 * (i + 1)))

    def drawDialogueWin(self):
        '''
            Draws dialogue window with coordinates
        '''
        for i in range(self.height):
            for j in range(self.width):
                if i == 0:
                    if j == 0:
                        win.blit(self.dialogue[0], (self.x + j, self.y + i))
                    elif j < self.width - 20 and j > 15 and j % 8 == 0:
                        win.blit(self.dialogue[-2], (self.x + j, self.y + i))
                    elif j == self.width - 20:
                        win.blit(self.dialogue[1], (self.x + j, self.y + i))
                elif i > 16 and i < self.height - 17:
                    if  j == 4 or j == + self.width - 5:
                        win.blit(self.dialogue[-1], (self.x + j, self.y + i))
                elif i == self.height - 17:
                    if j < + self.width - 41 and j > + 15 and j % 8 == 0:
                        win.blit(self.dialogue[-2], (self.x + j, self.y + i + 10))
                    elif j == 0 :
                        win.blit(self.dialogue[2], (self.x + j, self.y + i))
                    elif j ==  + self.width - 41:
                        win.blit(self.dialogue[-3], (self.x + j, self.y + i + 4))
        self.drawText()

class mainWindow(object):
    def __init__(self):
        self.button = buttons((800 - 114) / 2, (600 - 40 * 2.5) / 2)
        self.bg = background()
        self.dial = dialogue(200, 100, 520, 390, \
                'Hello wanderer!     To reach math Zen   start the game')
        self.run = True
        self.key_pressed = False
        self.play_or_exit_pressed = True

    def redrawGameWindow(self, is_pressed, p_or_e = True, stop = False):
        '''
            Redraws game window and highlights chosen button
        '''
        if not stop:
            if is_pressed:
                if p_or_e:
                    self.button.drawOnPlayButton()
                else:
                    self.button.drawOnExitButton()
            else:
                self.button.drawButtons()
            self.bg.drawNewton()
            self.bg.drawMenuManual()
            self.bg.drawReservation()
            self.dial.drawDialogueWin()
            #dial.drawText()
            #text = font.render('12345678901234567890123', 1, (255, 255, 255))
        pygame.display.update()

    def showMenu(self):
        '''
            Main function that has main loop in wich other functions are \
            executed
        '''
        #main loop
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            keys = pygame.key.get_pressed()
            if not self.key_pressed:
                self.redrawGameWindow(False)
            if keys[pygame.K_UP]:
                self.key_pressed = True
                self.play_or_exit_pressed = True
                self.redrawGameWindow(True, self.play_or_exit_pressed)
            if keys[pygame.K_DOWN]:
                self.key_pressed = True
                self.play_or_exit_pressed = False
                self.redrawGameWindow(True, self.play_or_exit_pressed)
            if self.key_pressed:
                if not self.play_or_exit_pressed and keys[pygame.K_SPACE]:
                    self.run = False

                elif self.play_or_exit_pressed and keys[pygame.K_SPACE]:
                    return True
                    self.run = False
