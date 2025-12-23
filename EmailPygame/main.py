import pygame
from pygame.locals import *
pygame.init()
timer = pygame.time.Clock()
font = pygame.font.Font(None, 30)
text_surface = font.render("Email", True, (0, 0, 0))
done = False
currentplace = 0
inputed2 = ''
x = -1000
y = -1000
inputed = ''
screenwidth = 500
screenheight = 500
window = pygame.display.set_mode( ( screenwidth,screenheight ) )
username = pygame.surface.Surface((250, 50))
password = pygame.surface.Surface((250, 50))
selected = pygame.surface.Surface((260, 60), pygame.SRCALPHA)
window.blit(username, (100, 100))
pygame.display.set_caption( "Email" )
fps = 30
background = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\pexels-pixabay-53594.jpg").convert()
yv = 1
xv = 1
def renderhome():
    global x, y, xv, yv, inputed2
    x += xv
    y += yv
    xv += (0 - x) * 0.001
    yv += (0 - y) * 0.001
    if x > 0 or x < -500:
        xv = -xv
    if y > 0 or y < -500:
        yv = -yv
    window.blit(background, (x, y))
    username.fill((255,255,255))
    password.fill((255,255,255))
    username_pos = (125, 200)
    password_pos = (125, 300)
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
    text_surface = font.render(inputed, True, (0,0,0))
    window.blit(username, (125, 200))
    window.blit(text_surface, (125, 212))
    text_surface = font.render('*'*len(inputed2), True, (0, 0, 0))
    window.blit(password, (125, 300))
    window.blit(text_surface, (125, 320))
    selected.fill((0,0,0,0))
    pygame.draw.rect(selected, (0,0,0), selected.get_rect(), 3)
    sel_x = username_pos[0] - 5
    sel_y = username_pos[1] - 5 if currentplace == 0 else password_pos[1] - 5
    window.blit(selected, (sel_x, sel_y))
while done == False:
    renderhome()
    pygame.display.update()
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key != pygame.K_TAB and event.key != pygame.K_RETURN:
                if currentplace == 0:
                    if event.key == pygame.K_BACKSPACE:
                        inputed = inputed[:-1]
                    else:
                        inputed += event.unicode
                else:
                    if event.key == pygame.K_BACKSPACE:
                        inputed2 = inputed2[:-1]
                    else:
                        inputed2 += event.unicode
            else:
                if event.key == pygame.K_TAB:
                    if currentplace == 0:
                        currentplace = 1
                    else:
                        currentplace = 0
                if event.key == pygame.K_RETURN:
                    done = True
                    pygame.quit()
print(inputed)
print(inputed2)