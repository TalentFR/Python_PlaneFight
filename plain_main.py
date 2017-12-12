import pygame
from plane_sprites import *

class PlaneGame(object):
    """The main class of plane fight game"""

    def __init__(self):
        print("The initialization of the game")
        #1. set the screen of the game
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2. set the clock of the game
        self.clock = pygame.time.Clock()
        #3. creats game sprites
        self.__create_sprites()
        #4. set the timer event: creat enemy plane
        pygame.time.set_timer(CREAT_ENEMY_EVENT, ENEMY_UPDATERATE_MS)
        #5. set the timer event: hero fire
        pygame.time.set_timer(HERO_FIRE_EVENT, HERO_FIRERATE_MS)

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("start the game")
        while True:
            #1. set the update frequency
            self.clock.tick(FRAME_PER_SECOND)
            #2. moniter and handle the events
            self.__event_hadler()
            #3. collision detection
            self.__detect_collision()
            #4. update and draw the game sprties
            self.__update_sprites()
            #5. update the screen
            pygame.display.update()

    def __event_hadler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.game_over()
            elif event.type == CREAT_ENEMY_EVENT:
                enemy1 = Enemy()
                self.enemy_group.add(enemy1)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("move right")

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed_x = 5
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed_x = -5
        else:
            self.hero.speed_x = 0

        if key_pressed[pygame.K_UP]:
            self.hero.speed = -5
        elif key_pressed[pygame.K_DOWN]:
            self.hero.speed = 5
        else:
            self.hero.speed = 0

    def __detect_collision(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            self.game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        pygame.display.update()

    @staticmethod
    def game_over():
        print("game over~")

        pygame.quit()
        exit(0)


if __name__ == '__main__':
    #creat the game object
    game = PlaneGame()

    #start the game
    game.start_game()