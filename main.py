import time
import pygame

from pygame.locals import *
from game import Game

j = 0
g = Game()
animateWalking = False
keyMultiplier = 0

while g.running:  # Executs the menu
    g.curr_menu.display_menu()
    g.game_loop()  # opens menu

# Initialisation

from csv_dialogue import MainDialogues, FlowerPotDialogue, StopSignDialogue, Policeman_Before_Bush_Dialogue, Policeman_After_Bush_Dialogue



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
pygame.display.set_caption("Investigation on a budget")
icon = pygame.image.load("assets/detective-hat.png")
pygame.display.set_icon(icon)


from menu import progress
print("progress is  ",progress)
#progress = 0  # Progress is going to be the save state of the game. When a scene is finished there will be progress+=1 and the scene will change with an if progress ==.
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

PoliceImg = pygame.image.load("assets\player\sprites\policeman\spr_policeman.png")
PoliceX = 1099
PoliceY = 345

# Backgrounds
crimeSceneBG = pygame.image.load("assets/backgrounds/Game_First_Scene_bigger_res_flowerpot1_missing.png").convert()

# UI:
textbox = pygame.image.load("assets/UI/textbox_full_res.png").convert_alpha()
inventaire = pygame.image.load("assets/UI/inventory.png").convert()

# Flowers:
flowerPot1 = pygame.image.load("assets/backgrounds/flower_pot_1.png").convert_alpha()
flowerPot2 = pygame.image.load("assets/backgrounds/flower_pot_2.png").convert_alpha()
flowerPot3 = pygame.image.load("assets/backgrounds/flower_pot_3.png").convert_alpha()
flowerPot4 = pygame.image.load("assets/backgrounds/flower_pot_4.png").convert_alpha()

#Musique:
pygame.mixer.music.load("assets/sound/Music/Menu Theme.mp3")
pygame.mixer.music.play(loops=-1)

# Le son n'est pas implemente pour l'instant.
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
talkingabout = False
showFlowerPot = True
stopsign = False
policeman_afterbush = False
policeman_beforebush = False
inventory = False   # par défaut l'inventaire est fermé
repeat_flower = True   #tant que le pot de fleur n'a pas été inspecté, repeat_flower = True. Une fois qu'il a été inspecté, la variable devient repeat_flower = False comme ça on ne peux pas inspecter deux fois le pot de fleur.
repeat_stopsign = True
repeat_policeman_afterbush = True
repeat_policeman_beforebush = True

# knowledge init variables:
kbushes = False
kstopsign = False
kpoliceman_afterbush = False
kpoliceman_beforebush = False

# dialogues:
Dialogue1p = ["Policeman ;I am sorry to have warned you  this late but the matter is urgent !", "some other text"]
explanation1 = dialogueFont.render("Policeman: Good evening Detective, press any key to continue", True,
                                   (255, 255, 255))


def cutscene1():  # Nous n'utilisons plus cette partie, nous la gardons seulement au cas où.
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
    screen.blit(PoliceImg, (PoliceX, PoliceY))


def checkanykey():  # This function checks if any key is pressed on the keyboard.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if temProgress == True:  # Temp progress servira a intercaler des dialogues quand le jouer discutera sur le sujet d'un objet qu'il a analyse.
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


def walking_function():  # verifie si le joueur est en train de marcher et dans quelle dirrection
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

    for event in pygame.event.get():  # Permet de vérifier quelle touche a ete utilisee et donc dans quelle dirrection il faut orienter le joueur.
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                walkingRight = True  # Orientation du joueur
            if event.key == K_LEFT:
                walkingRight = False
    if kbushes == False:
        screen.blit(flowerPot1, (523, 450))
    screen.blit(crimeSceneBG, (0, 0))
    screen.blit(PoliceImg, (PoliceX, PoliceY))


def show_bg():
    screen.blit(crimeSceneBG, (0, 0))
    screen.blit(PoliceImg, (PoliceX, PoliceY))


def ToPrint(x):
    return dialogueFont.render(MainDialogues[x], True,
                                          (255, 255, 255))


# keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
# if keys[pygame.K_TAB] and inventory == False:
# inventory = True


# on vérifie si TAB est pressé et si l'inventaire est fermé
# indique que l'inventaire est maintenant ouvert

# Game loop
running = True
while running:
    for event in pygame.event.get():  # checks if cross is clicked.
        if event.type == QUIT:
            running = False  # On ferme le jeu en passant la boucle en false
            print("croix")
    clock.tick(30)  # FPS

    print(temporaryProgress)
    if event.type == KEYDOWN:
        if inventory == False and event.key == K_TAB:
            print("i'm trying honest")
            inventory = True
            screen.blit(inventaire, (320, 40))
            pygame.display.update()

        if inventory == True and event.key == K_TAB:
            inventory = False
            pygame.display.update()
        pygame.display.update()


    else:
        if progress == 0:
            temProgress = False
            checkAnyKey = True
            oftenusedD1()
            screen.blit(ToPrint(0), (250, 500))  # Ceci affiche le texte
            pygame.display.update()
            checkanykey()  # appele la fonction checkanykey() qui permet de vérifier si une touche du clavier est cliquee.

        if progress == 1:
            temProgress = False
            oftenusedD1()
            print("oversised")
            oversisedPrint = dialogueFont.render(MainDialogues[1][:81], True,
                                          (255, 255, 255))
            screen.blit(oversisedPrint, (250, 500))
            oversisedPrint = dialogueFont.render(MainDialogues[1][81:], True,
                                          (255, 255, 255))
            screen.blit(oversisedPrint, (250, 520))
            pygame.display.update()
            checkanykey()

        if progress == 2:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(2), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 3:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(3), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 4:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(4), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 5:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(5), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 6:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(6), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 7:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(7), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 8:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(8), (250, 500))
            pygame.display.update()
            checkanykey()

        if progress == 9:
            temProgress = False
            oftenusedD1()
            screen.blit(ToPrint(9), (250, 500))
            pygame.display.update()
            checkanykey()
            show_walk = True

        if progress == 10:  # phase d'enquete

            #---------------------------------------------------------------------------------------------------------
            #Cette partie du code vérifie si l'inventaire n'est pas déja ouvert, et si il est déja ouvert, il le ferme

            if inventory == True:   #vérifie si l'inventaire n'est pas déja ouvert
                screen.blit(inventaire, (320, 40))  #crée un rendu de l'image de l'inventaire
                if kbushes == True:     #vérifie si on a inspecté le pot de fleur
                    screen.blit(flowerPot1, (409, 365))     #crée un rendu de l'image pot de fleur

                keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
                if keys[pygame.K_TAB]:  # Si la valeur de la clé K_TAB est vraie:
                    print("TAB.click")
                    inventory = False   #la valeur False indique que l'inventaire doit maintenant être fermé
                    time.sleep(0.2)  # afin de ne pas prendre en compte un double press


                pygame.display.update() #affiche les rendus

            # Fin de la première partie du code inventaire
            # ---------------------------------------------------------------------------------------------------------
            # Cette partie est déclenchée quand inventory!=True (quand l'inventaire est fermé), et ouvre l'inventaire avec inventory=True

            else:
                keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
                if keys[pygame.K_TAB]:  # Si la valeur de la clé K_TAB est vraie:
                    print("TAB.click")
                    inventory = True    #la valeur True indique que l'inventaire doit maintenant être ounvert
                    time.sleep(0.2)  # afin de ne pas prendre en compte un double press


            # Fin de la deuxième partie du code inventaire
            # ---------------------------------------------------------------------------------------------------------

                if show_walk:
                    walking_function()
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    print(Mouse_x, Mouse_y)

                    if animateWalking == True:  # On verifie s'il faut animer le joueur else il sera a l'arret.
                        if walkingRight == True:  # On verifie dans quel sens il faut s'orrienter.

                            for counter in range(
                                    len(playerWalkR)):  # Boucle pour afficher chaque frame de l'animation 1 par 1.
                                walkR = playerWalkR[int(
                                    counter)]  # WalkR est une variable contenant l'image a afficher. PlayerWalkR est une liste contenant toutes les frames de marche
                                counter = counter + 1
                                screen.blit(crimeSceneBG, (0, 0))  # On blit tout ce qu'il faut.
                                screen.blit(PoliceImg, (PoliceX, PoliceY))
                                if kbushes == False:  # On vérifie si le pot de fleur n'a pas été récupéré
                                    screen.blit(flowerPot1, (523, 417))

                                playerX = playerX + 40  # Apres avoir blit la frame on ajoute 40 a la position du joueur
                                boundaries()  # On vérifie si le joueur n'essaie pas de sortir.
                                screen.blit(walkR, (playerX, 350))  # On affiche le joueur
                                pygame.display.update()  # On rafraichit l'ecran
                                time.sleep(0.2)  # On attends 0.2s afin de rendre l'animation realiste.

                        else:
                            for counter in range(len(playerWalkL)):  # C'est presque la meme chose qu'au dessus
                                walkL = playerWalkL[int(
                                    counter)]  # WalkL est une variable contenant l'image a afficher. PlayerWalkL est une liste contenant toutes les frames de marche
                                counter = counter + 1
                                screen.blit(crimeSceneBG, (0, 0))  # On print tout ce qu'il faut.
                                screen.blit(PoliceImg, (PoliceX, PoliceY))
                                if kbushes == False:  # On vérifie si le pot de fleur n'a pas été récupéré
                                    screen.blit(flowerPot1, (523, 417))
                                playerX = playerX - 40  # Apres avoir blit la frame on ajoute 40 a la position du joueur
                                boundaries()
                                screen.blit(walkL, (playerX, 350))
                                pygame.display.update()
                                time.sleep(0.2)


                    else:
                        if walkingRight == False:  # On verifie dans quel sens s'orrienter
                            if kbushes == False:  # On vérifie si le pot de fleur n'a pas été récupéré
                                screen.blit(flowerPot1, (523, 417))
                            screen.blit(playerImgL, (playerX, 350))

                        else:  # Si l'on ne doit pas s'orrienter a droite alors logiquement il faut aller a gauche.
                            if kbushes == False:  # On vérifie si le pot de fleur n'a pas été récupéré
                                screen.blit(flowerPot1, (523, 417))
                            screen.blit(playerImgR, (playerX, 350))

                pressE = False

                print("player x=", playerX)
                if playerX <= 670 and playerX >= 517 and repeat_flower == True:   #si le joueur est dans cette zone, et que c'est la première fois qu'on inspecte le pot de fleur, faire:

                    toprint = dialogueFont.render("press e to inspect", True, (255, 255, 255))
                    pressE = True
                    bushes = True
                    screen.blit(toprint, (523, 417))
                    toprint = dialogueFont.render("press e to inspect", True, (255, 255, 255))
                    pressEprint = True
                    screen.blit(toprint, (523, 417))
                    pygame.display.update()

                elif playerX <= 210 and playerX >= 20 and repeat_stopsign == True:   #si le joueur est dans cette zone, et que c'est la première fois qu'on inspecte le panneau, faire:
                    toprint = dialogueFont.render("press e to inspect", True, (255, 255, 255))
                    screen.blit(toprint, (200, 417))
                    stopsign = True
                    pressE = True
                    pygame.display.update()

                elif playerX <= 1149 and playerX >= 1010 and repeat_policeman_beforebush == True:  # si le joueur est dans cette zone, et que c'est la première fois qu'on inspecte le panneau, faire:
                    toprint = dialogueFont.render("press e to talk to policeman", True, (255, 255, 255))
                    screen.blit(toprint, (1010, 417))
                    policeman_beforebush = True
                    pressE = True
                    pygame.display.update()

                elif playerX <= 1149 and playerX >= 1010 and repeat_policeman_afterbush == True and kbushes == True:  # si le joueur est dans cette zone, et que c'est la première fois qu'on inspecte le panneau, faire:
                    toprint = dialogueFont.render("press e to show findings", True, (255, 255, 255))
                    screen.blit(toprint, (1010, 417))
                    policeman_afterbush = True
                    pressE = True
                    pygame.display.update()

                # Ajouter les différents éléments à inspecter ici.

                else:
                    pygame.display.update()

                TalkingAbout = False
                if pressE == True:
                    print("can press e")
                    keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
                    if keys[pygame.K_e] and repeat_stopsign == True:  # Si la valeur de la clé K_RIGHT est vraie:
                        print("e.click")
                        # playerX = 5
                        TalkingAbout = True
                        repeat_stopsign = False
                        if stopsign == True:
                            temporaryProgress = 0
                            show_walk = False
                            talkingabout = True
                    elif keys[pygame.K_e] and repeat_policeman_beforebush == True:  # Si la valeur de la clé K_RIGHT est vraie:
                        print("e.click")
                        # playerX = 5
                        TalkingAbout = True
                        repeat_policeman_beforebush = False
                        if policeman_beforebush == True:
                            temporaryProgress = 0
                            show_walk = False
                            talkingabout = True
                    elif keys[pygame.K_e] and repeat_flower == True:  # Si la valeur de la clé K_RIGHT est vraie:
                        print("e.click")
                        # playerX = 5
                        TalkingAbout = True
                        repeat_flower = False  # une fois qu'on a inspecté le pot de fleur une première fois, repeat_flower = False comme ça on ne peut pas l'inspecter une deuxième fois
                        if bushes == True:  # On vérifie quel dialogue lancer ici le dialogue bushes
                            print("trying to display")
                            temporaryProgress = 0
                            show_walk = False
                            talkingabout = True
                    elif keys[pygame.K_e] and repeat_policeman_afterbush == True and kbushes == True:  # Si la valeur de la clé K_RIGHT est vraie:
                        print("e.click")
                        # playerX = 5
                        TalkingAbout = True
                        repeat_policeman_afterbush = False
                        if policeman_afterbush == True:
                            temporaryProgress = 0
                            show_walk = False
                            talkingabout = True
                    pressE = False


            if talkingabout:  # Le joueur inspecte le pot de fleurs et un dialoque se lance
                print("hello")
                oftenusedD1()
                temProgress = True
                if bushes == True:  # On lance le lialogue bushes la structure ci-dessous est tres similaire a celle au premier dialogue.

                    if temporaryProgress == 0:
                        checkanykey()  # on vérifie si une touche est enfoncée
                        oftenusedD1()  # On met l'ecran de dialogue
                        toprint = dialogueFont.render(FlowerPotDialogue[0], True, (
                        255, 255, 255))  # On affiche les dialogue de la meme maniere que dans le reste du jeu.
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 1:#Pareil qu'au dessus mais juste avec un indice plus grand.
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(
                            FlowerPotDialogue[1], True,
                            (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 2:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(FlowerPotDialogue[2], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                        
                    if temporaryProgress == 3:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(FlowerPotDialogue[3], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                    
                    if temporaryProgress == 4:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(FlowerPotDialogue[4], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                    
                    if temporaryProgress == 5:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(FlowerPotDialogue[5], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                        showFlowerPot = False  # On arrete d'afficher le pot de fleur car il a ete recupere pour analyse.
                        tempProgress = 0  # On remet tout les parametres requis afin de retourner a la phase d'enquete.
                        talkingabout = False
                        bushes = False
                        kbushes = True
                        progress = 5
                        show_walk = True
                        temProgress = False
                        
                elif stopsign == True:
                    #Inspecting the signpost
                    print("inspecting sign")
                    if temporaryProgress == 0:
                        checkanykey()  # on vérifie si une touche est enfoncée
                        oftenusedD1()  # On met l'ecran de dialogue
                        toprint = dialogueFont.render(StopSignDialogue[0], True, (
                        255, 255, 255))  # On affiche les dialogue de la meme maniere que dans le reste du jeu.
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 1:#Pareil qu'au dessus mais juste avec un indice plus grand.
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(
                            StopSignDialogue[1], True,
                            (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                        tempProgress = 0  # On remet tout les parametres requis afin de retourner a la phase d'enquete.
                        talkingabout = False
                        stopsign = False
                        kstopsign = True
                        progress = 5
                        show_walk = True
                        temProgress = False

                elif policeman_beforebush == True:
                    # Talking to policeman
                    print("talking to policeman")
                    if temporaryProgress == 0:
                        checkanykey()  # on vérifie si une touche est enfoncée
                        oftenusedD1()  # On met l'ecran de dialogue
                        toprint = dialogueFont.render(Policeman_Before_Bush_Dialogue[0], True, (
                            255, 255, 255))  # On affiche les dialogue de la meme maniere que dans le reste du jeu.
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 1:  # Pareil qu'au dessus mais juste avec un indice plus grand.
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(
                            Policeman_Before_Bush_Dialogue[1], True,
                            (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 2:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(Policeman_Before_Bush_Dialogue[2], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 3:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(Policeman_Before_Bush_Dialogue[3], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 4:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(Policeman_Before_Bush_Dialogue[4], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                        tempProgress = 0  # On remet tout les parametres requis afin de retourner a la phase d'enquete.
                        talkingabout = False
                        policeman_beforebush = False
                        kpoliceman_beforebush = True
                        progress = 5
                        show_walk = True
                        temProgress = False

                elif policeman_afterbush == True and kbushes == True:
                    # Talking to policeman
                    print("talking to policeman")
                    if temporaryProgress == 0:
                        checkanykey()  # on vérifie si une touche est enfoncée
                        oftenusedD1()  # On met l'ecran de dialogue
                        toprint = dialogueFont.render(Policeman_After_Bush_Dialogue[0], True, (
                            255, 255, 255))  # On affiche les dialogue de la meme maniere que dans le reste du jeu.
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 1:  # Pareil qu'au dessus mais juste avec un indice plus grand.
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(
                            Policeman_After_Bush_Dialogue[1], True,
                            (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 2:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(Policeman_After_Bush_Dialogue[2], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 3:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(Policeman_After_Bush_Dialogue[3], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 4:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render(Policeman_After_Bush_Dialogue[4], True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))
                        tempProgress = 0  # On remet tout les parametres requis afin de retourner a la phase d'enquete.
                        talkingabout = False
                        policeman_afterbush = False
                        kpoliceman_afterbush = True
                        progress = 5
                        show_walk = True
                        temProgress = False


        if progress > 10:
            kbushes= True
            progress=10
            temProgress = False
            show_walk = True
            repeat_flower=False
            repeat_stopsign = False
            repeat_policeman_afterbush = False
            repeat_policeman_beforebush = False
            
            