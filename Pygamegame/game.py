import pygame
import sys
import random
import time
pygame.init()
WIDTH = 500
HEIGHT = 500
background = (0, 255, 0)
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
win.fill(background)
food = [random.randrange(1,500),random.randrange(1,500), 10, 10] 
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]
speed = 5 
cubeX = 250 
cubeY = 250 
cubeSize = 20
run = True
while run:
    pygame.time.delay(10) 
    win.fill(background)
    food_status = True 
    Bfood_status = True
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: 
        if cubeX >= 480: 
            cubeX = 480 
        else: 
            cubeX += speed
    if keys[pygame.K_LEFT]:
        if cubeX <= 0:
            cubeX = 0
        else:
            cubeX -= speed
    if keys[pygame.K_UP]:
        if cubeY <= 0:
            cubeY = 0
        else:
            cubeY -= speed
    if keys[pygame.K_DOWN]:
        if cubeY >= 480:
            cubeY = 480
        else:
            cubeY += speed