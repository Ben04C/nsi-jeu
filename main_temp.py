import time
import pygame

from pygame.locals import *

from game import Game

j = 0
g = Game()
animateWalking = False

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()  # opens menu

# Initialisation
pygame.init()
pygame.mixer.init()
i = 0
walkingRight = True
# Clock for FPS
clock = pygame.time.Clock()

# create the window

screen = pygame.display.set_mode((1280, 720))

# creating the clock
message_end_time = 0

# Title and Icon
pygame.display.set_caption("Cyberpunk style game")
icon = pygame.image.load("assets/detective-hat.png")
pygame.display.set_icon(icon)

progress = 0  # Progress is going to be the save state of the game. When a scene is finished there will be progress+=1 and the scene will change with an if progress ==.
# Assets:
dialogueFont = pygame.font.Font("assets/fonts/EightBitDragon-anqx.ttf", 15)

# Characters
playerX = 370
playerY = 480
playerDialogue = pygame.image.load(
    "assets\player\half_bodies/Game_Character_Half_Body_OUTSIDE_LIGHTING_big_res.png").convert_alpha()

# Sprites
# Idle
playerImgR = pygame.image.load("assets\player\sprites\detective_idle\spr_detective_idle_0.png").convert_alpha()
playerImgL = pygame.transform.flip(playerImgR, True, False).convert_alpha()
# Walk
# liste contenant les iamges du joueur afin de faire l'animation
playerWalkR = [pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_0.png").convert_alpha(),
               pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_1.png").convert_alpha(),
               pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_2.png").convert_alpha(),
               pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_3.png").convert_alpha()]

playerWalkL = [pygame.transform.flip(playerWalkR[0], True, False).convert_alpha(),
               pygame.transform.flip(playerWalkR[1], True, False).convert_alpha(),
               pygame.transform.flip(playerWalkR[2], True, False).convert_alpha(),
               pygame.transform.flip(playerWalkR[3], True, False).convert_alpha()]

# PoliceImg = pygame.image.load("police.png")
PoliceX = 400
PoliceY = 480

# Backgrounds
crimeSceneBG = pygame.image.load("assets/backgrounds/Game_First_Scene_bigger_res.png").convert()

# UI:
textbox = pygame.image.load("assets/UI/textbox_full_res.png").convert_alpha()
inventaire = pygame.image.load("assets/UI/inventory.png").convert()

# Flowers:
flowerPot1 = pygame.image.load("assets/backgrounds/flower_pot_1.png").convert_alpha()
flowerPot2 = pygame.image.load("assets/backgrounds/flower_pot_2.png").convert_alpha()
flowerPot3 = pygame.image.load("assets/backgrounds/flower_pot_3.png").convert_alpha()
flowerPot4 = pygame.image.load("assets/backgrounds/flower_pot_4.png").convert_alpha()

# sound
# def m_buzzing():
# pygame.mixer.music.load("assets/sound/SFX/Neon_light_Buzzing.mp3")
# def m_investigation():
# pygame.mixer.music.load("assets/sound/Music/SFX/Neon_light_Buzzing.mp3")
# def m_explosion():
# pygame.mixer.music.load("assets/sound/SFX/small-explosion.mp3")


keys = pygame.key.get_pressed()

# Init variables:
bushes = False
tempProgress = True
temProgress = False
temporaryProgress = 0
taklingabout = False
inventory = False

# dialogues:
Dialogue1p = ["Policeman ;I am sorry to have warned you  this late but the matter is urgent !", "some other text"]
explanation1 = dialogueFont.render("Policeman: Good evening Detective, press any key to continue", True,
                                   (255, 255, 255))


def cutscene1():  # This cutscene is finally not used for now. We keep it just in case we have some more time.
    cscene1d = ["Flicker", "Flicker", "Flicker", "You're a goner"]
    pygame.mixer.music.set_volume(0.7)
    for i in range(4):  # Makes the screen blink

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


def oftenusedD1():  # This is a function that executes the lines of code that are often used in the first dialogue.
    screen.blit(crimeSceneBG, (0, 0))
    screen.blit(playerDialogue, (0, 0))
    screen.blit(textbox, (200, 450))


def checkanykey():  # This function checks if any key is pressed on the keyboard.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if temProgress == True:
                global temporaryProgress
                temporaryProgress += 1
            else:
                global progress
                progress += 1
            print("click")


def boundaries():  # teleports the player back into the game boundaries if he tries to get out
    global playerX
    if playerX <= 0:
        playerX = 1
    if playerX >= 1150:
        playerX = 1149


def walking_function():  # vérifie si le joueur est en train de marcher et dans quelle dirrection
    global animateWalking
    global j
    global walkingRight
    animateWalking = False  # permet de dire que l'on de veut pas animer le joueur.

    keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()

    if keys[pygame.K_RIGHT]:  # Si la valeur de la clé K_RIGHT est vraie:

        j += 1
        if j <= 4:
            j = 0
            animateWalking = True

    if keys[pygame.K_LEFT]:

        j += 1  # la variable temporaire j permet de voir si touche est maintenue pendant assez longtemps pour lancer une animation
        if j <= 4:
            j = 0
            animateWalking = True

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                walkingRight = True
            if event.key == K_LEFT:
                walkingRight = False
    screen.blit(flowerPot1, (523, 450))
    screen.blit(crimeSceneBG, (0, 0))


# Game loop
running = True
while running:
    for event in pygame.event.get():  # checks if cross is clicked.
        if event.type == QUIT:
            running = False
            print("croix")
    clock.tick(30)  # FPS

    if progress == 0:
        checkAnyKey = True
        oftenusedD1()
        screen.blit(explanation1, (250, 500))  # écrit le premier texte visible à l'écran
        pygame.display.update()
        checkanykey()  # appele la fonction checkanykey() qui permet de vérifier si une touche du clavier est cliquée.

    if progress == 1:
        oftenusedD1()
        toprint = dialogueFont.render("Huf... Puff..., Huf..., Puff. Palms sweaty, this case seems", True,
                                      (255, 255, 255))  # Ceci sont les paramètres du texte à afficher
        screen.blit(toprint, (250, 500))  # Ceci affiche le texte
        toprint = dialogueFont.render("to be big. AND Why is it always me that has to be called ", True,
                                      (255, 255, 255))  # Une autre ligne
        screen.blit(toprint, (250, 520))
        toprint = dialogueFont.render("upon at 2am.", True, (255, 255, 255))
        screen.blit(toprint, (250, 540))
        pygame.display.update()
        checkanykey()

    if progress == 2:
        oftenusedD1()
        toprint = dialogueFont.render("My name is Richard Bright, homocide detective at the  ", True, (255, 255, 255))
        screen.blit(toprint, (250, 500))
        toprint = dialogueFont.render("local precinct from Taga, Our great leader Mr. Taga himself called me", True,
                                      (255, 255, 255))
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
        show_walk = True

    if progress == 5:  # phase d'enquete
        if show_walk:
            walking_function()
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            print(Mouse_x, Mouse_y)

            if animateWalking == True:
                if walkingRight == True:
                    for counter in range(len(playerWalkR)):
                        walkR = playerWalkR[int(counter)]
                        counter = counter + 1
                        screen.blit(crimeSceneBG, (0, 0))
                        screen.blit(flowerPot1, (523, 450))
                        playerX = playerX + 40
                        boundaries()
                        screen.blit(walkR, (playerX, 350))
                        pygame.display.update()
                        time.sleep(0.2)

                else:
                    for counter in range(len(playerWalkL)):
                        walkL = playerWalkL[int(counter)]
                        counter = counter + 1
                        screen.blit(crimeSceneBG, (0, 0))
                        screen.blit(flowerPot1, (523, 450))
                        playerX = playerX - 40
                        boundaries()
                        screen.blit(walkL, (playerX, 350))
                        pygame.display.update()
                        time.sleep(0.2)


            else:
                if walkingRight == False:
                    screen.blit(flowerPot1, (523, 417))
                    screen.blit(playerImgL, (playerX, 350))

                else:
                    screen.blit(flowerPot1, (523, 417))
                    screen.blit(playerImgR, (playerX, 350))

        pressE = False

        print("player x=", playerX)
        if playerX <= 670 and playerX >= 517:

            toprint = dialogueFont.render("press e to inspect", True, (255, 255, 255))
            pressE = True
            bushes = True
            screen.blit(toprint, (523, 417))
            toprint = dialogueFont.render("press e to inspect", True, (255, 255, 255))
            pressEprint = True
            screen.blit(toprint, (523, 417))
            pygame.display.update()

        elif True == False:
            pass
            # Ajouter les différents éléments à inspecter ici.

        else:
            pygame.display.update()

        TalkingAbout = False
        if pressE == True:
            print("can press e")
            keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
            if keys[pygame.K_e]:  # Si la valeur de la clé K_RIGHT est vraie:
                print("e.click")
                TalkingAbout = True
                if bushes == True:
                    print("trying to display")

                    temporaryProgress = 0
                    show_walk = False
                    taklingabout = True

        if taklingabout:
            checkanykey()
            oftenusedD1()
            toprint = dialogueFont.render("Nice Bushes", True, (255, 255, 255))
            pressEprint = True
            pygame.display.update()

        keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
        if keys[pygame.K_TAB] and inventory == False:
            inventory = True
            screen.blit(inventaire, (0, 0))
            pygame.display.update()
        if keys[pygame.K_TAB] and inventory == True:
            inventory = False
            screen.blit(inventaire, (0, 0))
            pygame.display.update()

        if inventory == True:
            screen.blit(inventaire, (0, 0))
            pygame.display.update()