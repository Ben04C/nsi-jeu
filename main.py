import pygame
from pygame.locals import *

# Initialisation
pygame.init()
pygame.mixer.init()

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
dialogueFont = pygame.font.Font("assets/fonts/8-BIT WONDER.TTF", 32)

#Characters
playerImg = pygame.image.load("assets/detective-hat.png").convert_alpha()
playerX = 370
playerY = 480

#PoliceImg = pygame.image.load("police.png")
PoliceX = 400
PoliceY = 480

#Backgrounds
crimeSceneBG = pygame.image.load("assets/backgrounds/First_Scene.png").convert()

#sound
def m_buzzing():
    pygame.mixer.music.load("assets/sound/SFX/Neon_light_Buzzing.wav")
def m_investigation():
    pygame.mixer.music.load("assets/sound/Music/Investigation/[Filename].waw")
def m_explosion():
    pygame.mixer.music.load("assets/sound/SFX/small-explosion.wav")


keys = pygame.key.get_pressed()
def player(x, y):
    screen.blit(playerImg, (x, y))
    if keys[pygame.K_RIGHT]:
        playerX += 5
    if keys[pygame.K_LEFT]:
        playerY += 5


#dialogues:
Dialogue1p=["Good evening Detective ","I am sorry to have you come this late but the matter is urgent !"]


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




#Game loop
running = True
while running:
    for event in pygame.event.get(): #checks if cross is clicked.
        if event.type == pygame.QUIT:
            running = False


    if progress == 0:
        #pregame credits
        # pick a font you have and set its size
        progress+=1

    if progress == 1: #cutscene 1 with the intro
        cutscene1()
        progress += 1

    if progress == 2: #The first interactive screen
        screen.blit(crimeSceneBG,(0,0))
        screen.blit(icon, (0, 0))

        playerImg = pygame.image.load("assets/detective-hat.png")
        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
            pass

        screen.blit(playerImg, (300, 400))
        #player(playerX, playerY)
        m_investigation()
        pygame.mixer.music.load("assets/sound/Music/Investigation/[Filename].waw")




