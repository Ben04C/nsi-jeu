import pygame
from pygame.locals import *

from game import Game

g=0
g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()       #opens menu

# Initialisation
pygame.init()
pygame.mixer.init()
i=0
progress=0
walkingRight=True
#Clock for FPS
clock = pygame.time.Clock()


# create the window

screen = pygame.display.set_mode((1280,720))

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
playerX = 370
playerY = 480
playerDialogue = pygame.image.load("assets\player\half_bodies/Game_Character_Half_Body_OUTSIDE_LIGHTING_big_res.png").convert_alpha()


#Sprites
#Idle
playerImgR = pygame.image.load("assets\player\sprites\detective_idle\spr_detective_idle_0.png").convert_alpha()
playerImgL = pygame.transform.flip(playerImgR, True, False).convert_alpha()
#Walk
playerWalkR = [pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_0.png").convert_alpha(), pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_1.png").convert_alpha(), pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_2.png").convert_alpha(), pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_3.png").convert_alpha()]

playerWalkL = [pygame.transform.flip(playerWalkR[0], True, False).convert_alpha(), pygame.transform.flip(playerWalkR[1], True, False).convert_alpha(), pygame.transform.flip(playerWalkR[2], True, False).convert_alpha(), pygame.transform.flip(playerWalkR[3], True, False).convert_alpha()]




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
    clock.tick(30) #FPS


            
    
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

    if progress == 4:
        oftenusedD1()
        toprint = dialogueFont.render("Policeman :We have already investigated a bit,", True, (255, 255, 255))
        screen.blit(toprint, (250, 500))
        toprint = dialogueFont.render("BECAUSE WE HAD BUDGET CUTS LETS GET TO THE ", True, (255, 255, 255))
        screen.blit(toprint, (250, 520))
        toprint = dialogueFont.render("INVESTIGATION", True, (255, 255, 255))
        screen.blit(toprint, (250, 540))
        pygame.display.update()
        checkanykey()



        
    while progress== 5:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            #for counter in range(len(playerWalkR)):
                #player = pygame.image.load(playerWalkR[int(counter)])
                #counter = counter + 1
                playerX=playerX+1
                walking=True
        if keys[pygame.K_LEFT]:
                playerX=playerX-1
                walking=True
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("hello")
                if event.key == K_RIGHT:
                    walkingRight=True
                if event.key == K_LEFT:
                    walkingRight=False
        screen.blit(crimeSceneBG, (0, 0))
        if playerX<=0:
            playerX = 1
        if playerX>=1150:
            playerX=1149
        if walkingRight == True:
            for counter in range(len(playerWalkR)):
                walkR = playerWalkR[int(counter)]
                counter = counter + 1
                pygame.display.update()
                screen.blit(walkR,(playerX, 350))


        else:
            screen.blit(playerImgL,(playerX, 350))
            pygame.display.update()
        
