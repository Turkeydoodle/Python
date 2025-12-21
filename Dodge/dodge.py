import pygame, random
from pygame.locals import *
pygame.init()
timer = pygame.time.Clock()
enemies = []
bullets = []
index = 0
score = 0
pposx = 955
pposy = 980
screenwidth = 1920
screenheight = 1080
window = pygame.display.set_mode( ( screenwidth,screenheight ) )
pygame.display.set_caption( "Dodge" )
score = 0
font = pygame.font.Font(None, 30)
text_surface = font.render("Score:"+str(score), True, (0, 0, 0))
window.blit(text_surface, (10, 10))
pygame.display.flip()
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\enemy.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\bullet.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
def shoot():
    global pposx
    x = pposx + 45
    y = 980
    bullet = Bullet(x, y)
    bullets.append(bullet)
def produce_enemy():
    x = random.randint(0, screenwidth - 100)
    y = -100 
    enemy = Enemy(x, y)
    enemies.append(enemy)
bgcolor = pygame.Color(253,56,91)
imgPlayer = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\you.jpg").convert_alpha()
imgPlayer = pygame.transform.scale(imgPlayer, (100, 100))
imgSky = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\pexels-pixabay-53594.jpg").convert()
player_rect = imgPlayer.get_rect()
player_rect.topleft = (pposx, pposy)
fps = 30
enemy_spawn_timer = 0
done = False
def collision():
    global done, score
    for i, enemy in enumerate(enemies):
        if player_rect.colliderect(enemy.rect):
            done = True
    for i, bullet in enumerate(bullets):
        for j, enemy in enumerate(enemies):
            if bullet.rect.colliderect(enemy.rect):
                score += 100
                enemies.pop(j)
                bullets.pop(i)
while done == False:
    window.fill(bgcolor)
    window.blit(imgSky, (0, 0))
    window.blit(imgPlayer, (pposx, pposy))
    enemy_spawn_timer += 1
    if enemy_spawn_timer >=fps:
        produce_enemy()
        enemy_spawn_timer = 0
    for enemy in enemies:
        window.blit(enemy.image, enemy.rect)
        enemy.rect.y += 5 
    for b in bullets:
        b.rect.y -= 10
        window.blit(b.image, b.rect)
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        if pposx>=0:
            pposx -= 5
    elif keys[K_RIGHT]:
        if pposx <=1920:
            pposx += 5
    elif keys[K_SPACE]:
        shoot()  
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    collision()
    player_rect.topleft = (pposx, pposy)
    score += 1
    text_surface = font.render("Score:"+str(score), True, (0, 0, 0))
    window.blit(text_surface, (10, 10))
    pygame.display.update()
    timer.tick(fps)
print("Score: "+str(score))