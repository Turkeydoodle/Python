import pygame
from pygame.locals import *
pygame.init()
timer = pygame.time.Clock()
font = pygame.font.Font(None, 30)
text_surface = font.render("Email", True, (0, 0, 0))
done = False
x = -1000
y = -1000
inputed = ''
screenwidth = 500
screenheight = 500
window = pygame.display.set_mode( ( screenwidth,screenheight ) )
username = pygame.surface.Surface((250, 50))
password = pygame.surface.Surface((250, 50))
window.blit(username, (100, 100))
pygame.display.set_caption( "Email" )
fps = 30
background = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\pexels-pixabay-53594.jpg").convert()
yv = 1
xv = 1
def renderhome():
    global x, y, xv, yv
    x += xv
    y += yv
    xv += (0 - x) * 0.001
    yv += (0 - y) * 0.001
    if x > 0 or x < -500:
        xv = -xv
    if y > 0 or y < -500:
        yv = -yv
    window.blit(background, (x, y))
    font = pygame.font.Font(None, 30)
    text_surface = font.render("Email   Log-in", True, (0, 0, 0))
    window.blit(text_surface, (10, 10))
    font = pygame.font.Font(None, 50)
    text_surface = font.render("Log-in", True, (0, 0, 0))
    window.blit(text_surface, (185, 100))
    font = pygame.font.Font(None, 30)
    text_surface = font.render("Username:", True, (0, 0, 0))
    window.blit(text_surface, (125, 175))
    text_surface = font.render("Password:", True, (0, 0, 0))
    window.blit(text_surface, (125, 275))
    text_surface = font.render(inputed, True, (255, 255, 255))
    window.blit(username, (125, 200))
    window.blit(text_surface, (125, 212.5))
    window.blit(password, (125, 300))
while done == False:
    renderhome()
    pygame.display.update()
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                inputed = inputed[:-1]
            else:
                inputed += event.unicode
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True