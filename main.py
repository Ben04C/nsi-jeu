import pygame

# Initialisation
pygame.init()

# create the window
screen = pygame.display.set_mode((1280, 720))

#Title and Icon
pygame.display.set_caption("Testing")
icon = pygame.image.load("detective-hat.png")
pygame.display.set_icon(icon)

progress = 0 #Progress is going to be the save state of the game. When a scene is finished there will be progress+=1 and the scene will change with an if progress ==.
#Assets:
#Characters
playerImg = pygame.image.load("detective.png")
playerX = 370
playerY = 480


#Backgrounds
crimeSceneBG = pygame.image.load("crimescene.png")

keys = pygame.key.get_pressed()
def player(x, y):
    screen.blit(playerImg, (playerX, playerY))
    if keys[pygame.K_RIGHT]:
        playerX += 5
    if keys[pygame.K_LEFT]:
        playerY += 5

def cutscene1():
    for i in range(4):
        screen.fill((128, 0, 128))
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.time.wait(2000)
        pygame.display.update()
        pygame.time.wait(2000)





#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    if progress == 0:
        #pregame credits
        # pick a font you have and set its size
        myfont = pg.font.SysFont("Comic Sans MS", 30)
        # apply it to text on a label
        label = myfont.render("Python and Pygame are Fun!", 1, yellow)
        # put the label object on the screen at point x=100, y=100
        screen.blit(label, (100, 100))
        progress+=1

    if progress == 1: #cutscene 1 with the intro
        cutscene1()
        progress += 1

    if progress == 2: #The first interactive screen
        screen.blit(crimeSceneBG, (0, 0))
        player(playerX,playerY)








