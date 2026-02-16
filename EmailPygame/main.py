import pygame
from pygame.locals import *
pygame.init()
timer = pygame.time.Clock()
font = pygame.font.Font(None, 30)
text_surface = font.render("Kmail", True, (0, 0, 0))
done = False
currentplace = 0
mcurrentplace = 0
inboxcurrentplace = 0
page = 0
inputed2 = ''
x = -1000
y = -1000
menuicons = ['Inbox','Sent','Trash','Settings','Log Out']
inputed = ''
currentpage = 'home'
screenwidth = 500
screenheight = 500
window = pygame.display.set_mode((screenwidth,screenheight ) )
username = pygame.surface.Surface((250, 50))
password = pygame.surface.Surface((250, 50))
selected = pygame.surface.Surface((260, 60), pygame.SRCALPHA)
selectedm = pygame.surface.Surface((460, 60))
selectedinbox = pygame.surface.Surface((460, 60), pygame.SRCALPHA)
selectedinbox.fill((0,0,0,0))
pygame.draw.rect(selectedinbox, (0,0,0), selectedinbox.get_rect(), 5)
currentwin = 0
winselect  = pygame.surface.Surface((10, 10))
selected_email = 0
def blitmenu():
    for i in range(5):
        block = pygame.surface.Surface((450, 50))
        block.fill((255,255,255))
        window.blit(block, (25, 100+(i*75)))
        font = pygame.font.Font(None, 30)
        text_surface = font.render(menuicons[i], True, (0, 0, 0))
        window.blit(text_surface, (50, 115+(i*75)))
window.blit(username, (100, 100))
pygame.display.set_caption( "Kmail" )
fps = 30
background = pygame.image.load(r"\Users\user\OneDrive\Desktop\Personal\Productivity\Projects\Python\Dodge\content\images\pexels-pixabay-53594.jpg").convert()
yv = 1
xv = 1
name = inputed.partition('@')[0]
def renderlogin():
    global x, y, xv, yv, inputed2, inputed, done, currentplace, page, name
    window.blit(background, (0, 0))
    username.fill((255,255,255))
    password.fill((255,255,255))
    username_pos = (125, 200)
    password_pos = (125, 300)
    font = pygame.font.Font(None, 30)
    text_surface = font.render("Kmail   Log-in", True, (0, 0, 0))
    window.blit(text_surface, (10, 10))
    font = pygame.font.Font(None, 50)
    text_surface = font.render("Log-in", True, (0, 0, 0))
    window.blit(text_surface, (185, 100))
    font = pygame.font.Font(None, 30)
    text_surface = font.render("Email:", True, (0, 0, 0))
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
                    if inputed == '' or inputed2 == '':
                        pass
                    else:
                        page = 1
numimessagees = 4
imessagenames = ["Welcome to Kmail!", "Send an Email", "Deleting an email", 'How to use the trash folder']
imessagemessage = ['Hello! Thanks for choosing Kmail!\nHope you enjoy it!\nSincerely,\nThe developer of Kmail', 'To send an email, perform the following steps:\n1. Go to the "sent" folder\n2. Navigate to "draft"\n3. Compose and send!', 'To delete an email, do the following steps:\n1. Go to the "inbox" folder\n2. Select the email you want to delete\n3. Press the delete key!\nSimple and easy!','Here is how to use the trash folder:\nEnter any email in the trash folder\nPress the following to:\n1. Delete permanently: Press the delete key\n2. Restore email: Press the tab key\n3. Go back to inbox: Press space']
def renderimessage(chosenemail):
    global x, y, xv, yv, done, currentpage, inboxcurrentplace, page
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 50)
    text_surface = font.render(imessagenames[chosenemail], True, (0, 0, 0))
    window.blit(text_surface, (25, 25))
    block = pygame.surface.Surface((450, 350))
    block.fill((255,255,255))
    window.blit(block, (25, 75))
    font = pygame.font.Font(None, 30)
    lines = imessagemessage[chosenemail].split('\n')
    y_offset = 80
    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        window.blit(text_surface, (30, y_offset))
        y_offset += 35
    font = pygame.font.Font(None, 30)
    text_surface = font.render("Press SPACE to go back", True, (0, 0, 0))
    window.blit(text_surface, (125, 450))
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                currentpage = 'inbox'
                inboxcurrentplace = 0
                page = 1
def renderinbox():
    global x, y, xv, yv, done, currentpage, mcurrentplace, page, inboxcurrentplace, selected_email
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 50)
    text_surface = font.render("Inbox", True, (0, 0, 0))
    window.blit(text_surface, (25, 25))
    sel_x = 20
    sel_y = 100 + (inboxcurrentplace * 60) - 5
    window.blit(selectedinbox, (sel_x, sel_y))
    for i in range(numimessagees):
        block = pygame.surface.Surface((450, 50))
        block.fill((255,255,255))
        window.blit(block, (25, 100+(i*60)))
        font = pygame.font.Font(None, 30)
        text_surface = font.render(imessagenames[i], True, (0, 0, 0))
        window.blit(text_surface, (45, 115+(i*60)))
    font = pygame.font.Font(None, 30)
    text_surface = font.render("Press SPACE to go back", True, (0, 0, 0))
    window.blit(text_surface, (125, 450))
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                currentpage = 'home'
                mcurrentplace = 0
            if event.key == pygame.K_TAB:
                inboxcurrentplace += 1
                if inboxcurrentplace >= nummessagees:
                    inboxcurrentplace = 0
            if event.key == pygame.K_RETURN:
                selected_email = inboxcurrentplace
                page = 2
def rendersent():
    pass
def rendertrash():
    pass
def rendersettings():
    pass
def renderhome():
    global x, y, xv, yv, text_surface, done, name, mcurrentplace, page, inputed, currentwin, inputed2, currentpage
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 50)
    name = inputed.partition('@')[0]
    text_surface = font.render("Welcome, " + name, True, (0, 0, 0))
    sel_x = 20
    sel_y = 95 + (mcurrentplace * 75)
    window.blit(selectedm, (sel_x, sel_y))
    blitmenu()
    sel_x = 450
    sel_y = 115 + (currentwin * 75)
    window.blit(winselect, (sel_x, sel_y))
    window.blit(text_surface, (25, 25))
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                mcurrentplace += 1
                if mcurrentplace > 4:
                    mcurrentplace = 0
            if event.key == pygame.K_RETURN:
                currentwin = mcurrentplace
                if menuicons[currentwin] == 'Log Out':
                    page = 0
                    inputed = ''
                    inputed2 = ''
                elif menuicons[currentwin] == 'Settings':
                    currentpage = 'settings'
                elif menuicons[currentwin] == 'Inbox':
                    currentpage = 'inbox'
                elif menuicons[currentwin] == 'Sent':
                    currentpage = 'sent'
                elif menuicons[currentwin] == 'Trash':
                    currentpage = 'trash'
while not done:
    if page == 0:
        renderlogin()
    elif page == 1:
        if currentpage == 'home':
            renderhome()
        elif currentpage == 'inbox':
            renderinbox()
        elif currentpage == 'sent':
            rendersent()
        elif currentpage == 'trash':
            rendertrash()
        elif currentpage == 'settings':
            rendersettings()
    elif page == 2:
        renderimessage(selected_email)
    pygame.display.update()
    timer.tick(fps)
pygame.quit()
print('Program executed successfully. Pygame.quit() called.')
print("Email: " + inputed)
print("Password: " + inputed2)