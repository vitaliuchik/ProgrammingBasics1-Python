import pygame

win_size = (800, 600)
walkRight = [pygame.image.load('sprites/R0.png'), pygame.image.load('sprites/R1.png'),
                  pygame.image.load('sprites/R2.png'), pygame.image.load('sprites/R3.png'),
                  pygame.image.load('sprites/R4.png'), pygame.image.load('sprites/R5.png')]
walkLeft = [pygame.image.load('sprites/L0.png'), pygame.image.load('sprites/L1.png'),
                 pygame.image.load('sprites/L2.png'), pygame.image.load('sprites/L3.png'),
                 pygame.image.load('sprites/L4.png'), pygame.image.load('sprites/L5.png')]
cube = pygame.image.load('sprites/cube.png')
bull = pygame.image.load('sprites/bullet.png')
health = pygame.image.load('sprites/hp.png')
bg = pygame.image.load('sprites/bg.png')


class player(object):
    '''
    Creates main hero, (x, y) - top left coordinates of hero sprites
    '''

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

        self.left = False
        self.right = False
        self.walkCount = 0

        self.standing = True

    def draw(self, win):
        '''
        Draw main hero
        '''
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//4], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//4], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x,self.y))
            elif self.right:
                win.blit(walkRight[0], (self.x,self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))


class projectile(object):
    """
    Creates projectile, (x, y) - top left coordinates of projectile
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 20

    def draw(self, win):
        """
        Draw projectile
        """
        win.blit(bull, (self.x, self.y))


class block(object):
    """
    Creates box with number
    """
    def __init__(self, number, x):
        self.number = number
        self.x = x
        self.y = 55

    def draw(self, win):
        """
        Draw boxe and print number
        """
        win.blit(cube, (self.x, self.y))
        font = pygame.font.Font(None, 40)
        text = font.render(str(self.number), True, [255, 255, 255])
        if self.number < 10:
            win.blit(text, (self.x + 15, self.y + 10))
        else:
            win.blit(text, (self.x + 8, self.y + 10))


class hp(object):
    """
    Creates hp bar
    """
    def __init__(self, x):
        self.x = x
        self.y = 5

    def draw(self, win):
        """
        Draw hp bar
        """
        win.blit(health, (self.x, self.y))


class timer(object):
    """
    Creates timer with time_left seconds left
    """
    def __init__(self, time_left, x, y):
        self.time_left = time_left
        self.x = x
        self.y = y

    def draw(self, win):
        """
        Draw timer
        """
        font = pygame.font.Font(None, 60)
        text = font.render(str(self.time_left), True, [255, 255, 255])
        win.blit(text, (self.x, self.y))


def create_blocks(lst):
    """
    (list) -> list

    Return list of block objects with numbers from lst
    """
    blocks = []
    for i in range(len(lst)):
        blocks.append(block(i + 1, 2 + 50 * i-1))
    return blocks


#mainloop
class minigame(object):
    """
    Main class of minigame
    """
    def __init__(self, win, true_boxes, block_lst, start_time, number_type):
        self.win = win

        self.clock = pygame.time.Clock()

        self.man = player(0, win_size[1] - 50, 32, 32)
        self.bulletLoop = 1  # фіксить те що вилітають декілька пуль одночасно
        self.bullets = []
        self.boxes = create_blocks(block_lst)
        self.hearts = [hp(win_size[0] - 300 + i*40) for i in range(3)]
        self.true_boxes = true_boxes
        self.number_type = number_type
        self.false_boxes_count = 0
        self.timer_count = 0
        self.start_time = start_time
        self.timer_element = timer(self.start_time, 400, 10)
        self.run = True

    def redrawGameWindow(self):
        """
        Redraw window and objects
        """
        self.win.blit(bg, (0, 0))
        self.man.draw(self.win)
        self.timer_element.draw(self.win)
        for heart in self.hearts:
            heart.draw(self.win)
        for box in self.boxes:
            if box:
                box.draw(self.win)
        for bullet in self.bullets:
            bullet.draw(self.win)
        font = pygame.font.Font(None, 50)
        text = font.render(self.number_type + ' numbers', True, [255, 255, 255])
        self.win.blit(text, (50, 10))
        pygame.display.update()




    def run_game(self):
        """
        Runs minigame
        """
        while self.run:
            self.clock.tick(24)

            if self.bulletLoop > 0:
                self.bulletLoop += 1
            if self.bulletLoop > 3:
                self.bulletLoop = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    return 'quit'

            # пули летят
            for bullet in self.bullets:
                # полет пули
                if bullet.y > 100:
                    bullet.y -= bullet.vel
                else:
                    # проверка попадания в правильный квадрат
                    if self.boxes[(bullet.x + 12)//50]:
                        if self.boxes[(bullet.x + 12)//50].number in self.true_boxes:
                            self.hearts.pop(-1)
                            if len(self.hearts) == 0:
                                self.run = False
                                return 'hp'
                        else:
                            self.boxes[(bullet.x + 12)//50] = False
                            self.false_boxes_count += 1
                            if self.false_boxes_count == len(self.boxes) - len(self.true_boxes):
                                self.run = False
                                return 'win'
                    self.bullets.pop(self.bullets.index(bullet))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and self.bulletLoop == 0:
                if len(self.bullets) < 5:
                    self.bullets.append(projectile(self.man.x + 6, self.man.y))
                self.bulletLoop = 1

            if keys[pygame.K_LEFT] and self.man.x > self.man.vel:
                self.man.x -= self.man.vel
                self.man.left = True
                self.man.right = False
                self.man.standing = False
            elif keys[pygame.K_RIGHT] and self.man.x < win_size[0] - self.man.width - self.man.vel:
                self.man.x += self.man.vel
                self.man.right = True
                self.man.left = False
                self.man.standing = False
            else:
                self.man.standing = True
                self.man.walkCount = 0

            # timer
            self.timer_count += 1
            if self.timer_count == 24:
                self.timer_count = 0
                if self.start_time == 0:
                    self.run = False
                    return 'time'
                else:
                    self.start_time -= 1
                    self.timer_element = timer(self.start_time, 400, 10)


            self.redrawGameWindow()
