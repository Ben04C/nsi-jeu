import pygame

# Initialisation
pygame.init()

# create the window
screen = pygame.display.set_mode((1280,720))

#creating the clock
message_end_time = 0


#Title and Icon
pygame.display.set_caption("Cyberpunk style game")
icon = pygame.image.load("detective-hat.png")
pygame.display.set_icon(icon)

progress = 0 #Progress is going to be the save state of the game. When a scene is finished there will be progress+=1 and the scene will change with an if progress ==.
#Assets:
dialogueFont = pygame.font.Font("fonts/8-BIT WONDER.TTF", 32)

#Characters
#playerImg = pygame.image.load("detective.png")
playerX = 370
playerY = 480

#PoliceImg = pygame.image.load("police.png")
PoliceX = 400
PoliceY = 480

#Backgrounds
crimeSceneBG = pygame.image.load("backgrounds/First_Scene.png")



keys = pygame.key.get_pressed()
def player(x, y):
    screen.blit(playerImg, (x, y))
    if keys[pygame.K_RIGHT]:
        playerX += 5
    if keys[pygame.K_LEFT]:
        playerY += 5



def cutscene1():
    for i in range(4):
        screen.fill((128, 0, 128))
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.time.delay(1 * 3000)
        pygame.display.update()
        dialogue = dialogueFont.render("Testing some text", True, (255, 255, 255))
        screen.blit(dialogue, (0, 0))
        pygame.time.delay(1 * 3000)





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

        playerImg = pygame.image.load("detective.png")
        screen.blit(playerImg, (300, 400))
        player(playerX, playerY)
        print("hello")



