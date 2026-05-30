import pygame
from pygame.locals import *
pygame.init()
size = [width, height] = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Fish")
clock = pygame.time.Clock()
background = (0, 127, 255)
def main():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
        screen.fill(background)
        pygame.display.update()
main()