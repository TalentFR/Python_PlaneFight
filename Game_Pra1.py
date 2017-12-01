import pygame
from plane_sprites import *

pygame.init()

#创建图形窗口
screen = pygame.display.set_mode((480, 700))

#绘制背景图像
#>1 加载背景图像
background = pygame.image.load("./images/background.png")
#>2 在游戏窗口中绘制背景图像
screen.blit(background, (0,0))
#>3 更新游戏窗口
# pygame.display.update()

#绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (300, 600))
hero_pos = pygame.Rect(300, 600, 102, 126)

pygame.display.update()

#创建敌机
enemy1 = GameSprite("./images/enemy1.png")
enemy2 = GameSprite("./images/enemy1.png",2)

enemy_group = pygame.sprite.Group(enemy1, enemy2)

#创建时钟对象
clock = pygame.time.Clock()

while True:
    clock.tick(60)
#捕获事件
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    hero_pos.y -= 1

    if hero_pos.bottom == 0:
        hero_pos.y = 700


    screen.blit(background, (0,0))
    screen.blit(hero, hero_pos)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()