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
food = [random.randrange(1,500),random.randrange(1,500), 10, 10] 
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]
speed = 5 
cubeX = 250 
cubeY = 250 
cubeSize = 20
run = True
clock = pygame.time.Clock()
def main():
    global food_status, Bfood_status, run, cubeX, cubeY, cubeSize, food, Bfood
    while run:
        clock.tick(60)
        food_status = True 
        Bfood_status = True
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: 
            if cubeX >= 500-cubeSize: 
                cubeX = 500-cubeSize
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
            if cubeY >= 500-cubeSize:
                cubeY = 500-cubeSize
            else:
                cubeY += speed
        win.fill(background)
        cube = pygame.Rect(cubeX,cubeY,cubeSize,cubeSize)
        if cubeSize <= 100:
            pygame.draw.rect(win, (255, 255, 255), cube)
        else:
            pygame.draw.rect(win, (255, 0, 0), cube)
        if food_status:
            pygame.draw.rect(win, (0, 0, 255), food)
        if Bfood_status:
            pygame.draw.rect(win, (255, 255, 0), Bfood)
        if cube.colliderect(food):
            cubeSize += 10
            food_status = False
            food = [random.randrange(1,500),random.randrange(1,500), 10, 10] 
        if cube.colliderect(Bfood):
            cubeSize -= 20
            Bfood_status = False
            Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]
        pygame.display.flip()
main()