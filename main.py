import pygame
from pygame.locals import *

# Initialisation
pygame.init()
pygame.mixer.init()
i=0
progress=0

# create the window

screen = pygame.display.set_mode((1280,720), RESIZABLE)

#creating the clock
message_end_time = 0


#Title and Icon
pygame.display.set_caption("Cyberpunk style game")
icon = pygame.image.load("assets/detective-hat.png")
pygame.display.set_icon(icon)

progress = 0 #Progress is going to be the save state of the game. When a scene is finished there will be progress+=1 and the scene will change with an if progress ==.
#Assets:
dialogueFont = pygame.font.Font("assets/fonts/EightBitDragon-anqx.ttf", 15)





#Characters
playerImg = pygame.image.load("assets\player\half_bodies/Game_Character_Half_Body_OUTSIDE_LIGHTING_big_res.png").convert_alpha()
playerX = 370
playerY = 480
playerDialogue = pygame.image.load("assets\player\half_bodies/Game_Character_Half_Body_OUTSIDE_LIGHTING_big_res.png").convert_alpha()



#PoliceImg = pygame.image.load("police.png")
PoliceX = 400
PoliceY = 480






#Backgrounds
crimeSceneBG = pygame.image.load("assets/backgrounds/Game_First_Scene_bigger_res.png").convert()


#Button:
textbox = pygame.image.load("assets/UI/textbox_full_res.png").convert_alpha()





#sound
#def m_buzzing():
    #pygame.mixer.music.load("assets/sound/SFX/Neon_light_Buzzing.mp3")
#def m_investigation():
    #pygame.mixer.music.load("assets/sound/Music/SFX/Neon_light_Buzzing.mp3")
#def m_explosion():
    #pygame.mixer.music.load("assets/sound/SFX/small-explosion.mp3")






keys = pygame.key.get_pressed()
def player(x, y):
    screen.blit(playerImg, (x, y))
    if keys[pygame.K_RIGHT]:
        global playerX
        playerX += 5
    if keys[pygame.K_LEFT]:
        global playerY
        playerY += 5







#dialogues:
Dialogue1p=["Policeman ;I am sorry to have warned you  this late but the matter is urgent !", "some other text"]
explanation1= dialogueFont.render("Policeman: Good evening Detective, press any key to continue", True, (255, 255, 255))





def cutscene1():
    cscene1d=["Flicker", "Flicker", "Flicker", "You're a goner"]
    m_buzzing()
    pygame.mixer.music.set_volume(0.7)
    for i in range(4): #Makes the screen blink

        pygame.time.delay(1 * 3000)
        screen.fill((128, 0, 128))
        pygame.mixer.music.play()
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.time.delay(1 * 3000)
        pygame.display.update()
        dialogue = dialogueFont.render(cscene1d[i], True, (255, 255, 255))
        screen.blit(dialogue, (0, 0))
    m_explosion()
    pygame.mixer.music.play()
    pygame.time.delay(1 * 5000)

def oftenusedD1():
    screen.blit(crimeSceneBG, (0, 0))
    screen.blit(playerDialogue, (0, 0))
    screen.blit(textbox, (200, 450))



def checkanykey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            global progress
            progress += 1
            print("click")

#Game loop
running = True
while running:
    for event in pygame.event.get(): #checks if cross is clicked.
        if event.type == QUIT:

            running = False
            print("croix")


            
    
    if progress == 0:
        checkAnyKey=True
        oftenusedD1()
        screen.blit(explanation1, (250,500))
        pygame.display.update()
        pressed = pygame.key.get_pressed()
        checkanykey()

            
            
    if progress == 1:
        oftenusedD1()
        toprint = dialogueFont.render("Huf... Puff..., Huf..., Puff. Palms sweaty, this case seems", True, (255, 255, 255))
        screen.blit(toprint, (250,500))
        toprint = dialogueFont.render("to be big. AND Why is it always me that has to be called ", True, (255, 255, 255))
        screen.blit(toprint, (250, 520))
        toprint = dialogueFont.render("upon at 2am.", True, (255, 255, 255))
        screen.blit(toprint, (250, 540))
        pygame.display.update()
        checkanykey()

    if progress == 2:
        oftenusedD1()
        toprint = dialogueFont.render("My name is Richard Bright, homocide detective at the  ", True, (255, 255, 255))
        screen.blit(toprint, (250,500))
        toprint = dialogueFont.render("local precinct from Taga, Mr. Taga himself called me this", True, (255, 255, 255))
        screen.blit(toprint, (250, 520))
        toprint = dialogueFont.render("Let me tell you I got a ", True, (255, 255, 255))
        pygame.display.update()
        checkanykey()

    if progress == 3:
        oftenusedD1()
        toprint = dialogueFont.render("Policeman :I am sorry to have warned you  this late", True, (255, 255, 255))
        screen.blit(toprint, (250, 500))
        toprint = dialogueFont.render("but the matter is urgent !", True, (255, 255, 255))
        screen.blit(toprint, (250, 520))
        pygame.display.update()
        checkanykey()

