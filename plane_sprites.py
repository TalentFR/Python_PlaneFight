import random
import pygame

# The size of game screen
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# The update rate of the game screen
FRAME_PER_SECOND = 60
# The id of creat a new enemy event
CREAT_ENEMY_EVENT = pygame.USEREVENT
# The enemy update rate in ms
ENEMY_UPDATERATE_MS = 1000
# The id of hero fire event
HERO_FIRE_EVENT = pygame.USEREVENT + 1
# The hero fire rate in ms
HERO_FIRERATE_MS = 300
# The height of bullet
BULLET_HEIGHT = 20

class GameSprite(pygame.sprite.Sprite):
    """飞机大战精灵，继承pygame自带精灵类"""

    def __init__(self, image_name, speed = 1):
        #调用父类初始化方法
        super().__init__()

        #定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):
    """The backgroud class of the game"""
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")

        if is_alt == True:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    """The Enemy plane class of the game"""

    def __init__(self):
        #1.  call the init function of the parent class
        super().__init__("./images/enemy1.png")

        #2. set the speed of the enemy plane
        self.speed = random.randint(1, 4)

        #3. set the initial position of the enemy plane
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width-self.rect.width)

    def update(self):
        #1. call the update function of the parent class
        super().update()
        #2. check if the enemy is out of the screen
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    
    def __del__(self):
        pass
    
class Hero(GameSprite):
    """The hero plane class in the game"""
    def __init__(self, speedx = 0):
        super().__init__("./images/me1.png", 0)
        # The initial position of the hero position
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.speed_x = speedx

        # Create the bullets sprites group
        self.bullets = pygame.sprite.Group()

    def update(self):
        if self.rect.right+self.speed_x > SCREEN_RECT.right \
                or self.rect.left+self.speed_x < SCREEN_RECT.left:
            pass
        else:
            self.rect.x += self.speed_x
        if self.rect.top+self.speed < SCREEN_RECT.top \
                or self.rect.bottom+self.speed > SCREEN_RECT.bottom:
            pass
        else:
            self.rect.y += self.speed

    def fire(self):
        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.top - i*BULLET_HEIGHT
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)

class Bullet(GameSprite):
    """The bullet class in the game"""
    def __init__(self):
        super().__init__("./images/bullet1.png", -5)


    def update(self):
        super().update()

        if self.rect.bottom < SCREEN_RECT.top:
            self.kill()

    def __del__(self):
        pass