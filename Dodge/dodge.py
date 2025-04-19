import pygame
from pygame.locals import *
pygame.init()
timer = pygame.time.Clock()
enemies = []
index = 0
screenwidth = 640
screenheight = 640
window = pygame.display.set_mode( ( screenwidth,screenheight ) )
def produce_enemy(x, y):
    imgEnemy = pygame.image.load("Python/Dodge/content/images/enemy.jpg")
    imgEnemy = pygame.transform.scale(imgEnemy, (100,100))
    enemyproduced = window.blit(imgEnemy, (x, y))
    enemies.append(enemyproduced)
    enemyproduced.x = x
    enemyproduced.y = y
pposx = 0
pposy = 0
bgcolor = pygame.Color(253,56,91)
imgPlayer = pygame.image.load("Python/Dodge/content/images/41822.jpg")
imgPlayer = pygame.transform.scale(imgPlayer, (100, 100))
imgSky = pygame.image.load("Python/Dodge/content/images/pexels-pixabay-53594.jpg")
fps = 30
pygame.display.set_caption( "ProtoPygame" )
done = False
while done == False:
    window.fill(bgcolor)
    window.blit(imgSky, (0, 0))
    window.blit(imgPlayer, (pposx, pposy))
    produce_enemy(100, 100)
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        pposy -= 5
    elif keys[K_DOWN]:
        pposy += 5
    elif keys[K_LEFT]:
        pposx -= 5
    elif keys[K_RIGHT]:
        pposx += 5
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    pygame.display.update()
    timer.tick(fps)