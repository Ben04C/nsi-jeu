import time
import pygame

from pygame.locals import *

from game import Game

j=0
g = Game()
animateWalking = False

while g.running: #Executs the menu
    g.curr_menu.display_menu()
    g.game_loop() #opens menu

# Initialisation
pygame.init()
pygame.mixer.init()
i=0
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
#liste contenant les iamges du joueur afin de faire l'animation
playerWalkR = [pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_0.png").convert_alpha(), pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_1.png").convert_alpha(), pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_2.png").convert_alpha(), pygame.image.load("assets\player\sprites\detective_walk\spr_detective_walk_3.png").convert_alpha()]

playerWalkL = [pygame.transform.flip(playerWalkR[0], True, False).convert_alpha(), pygame.transform.flip(playerWalkR[1], True, False).convert_alpha(), pygame.transform.flip(playerWalkR[2], True, False).convert_alpha(), pygame.transform.flip(playerWalkR[3], True, False).convert_alpha()]

#PoliceImg = pygame.image.load("police.png")
PoliceX = 400
PoliceY = 480






#Backgrounds
crimeSceneBG = pygame.image.load("assets/backgrounds/Game_First_Scene_bigger_res.png").convert()


#UI:
textbox = pygame.image.load("assets/UI/textbox_full_res.png").convert_alpha()
inventaire = pygame.image.load("assets/UI/inventory.png").convert()

#Flowers:
flowerPot1=pygame.image.load("assets/backgrounds/flower_pot_1.png").convert_alpha()
flowerPot2=pygame.image.load("assets/backgrounds/flower_pot_2.png").convert_alpha()
flowerPot3=pygame.image.load("assets/backgrounds/flower_pot_3.png").convert_alpha()
flowerPot4=pygame.image.load("assets/backgrounds/flower_pot_4.png").convert_alpha()



#Le son n'est pas implemente pour l'instant.
#sound
#def m_buzzing():
    #pygame.mixer.music.load("assets/sound/SFX/Neon_light_Buzzing.mp3")
#def m_investigation():
    #pygame.mixer.music.load("assets/sound/Music/SFX/Neon_light_Buzzing.mp3")
#def m_explosion():
    #pygame.mixer.music.load("assets/sound/SFX/small-explosion.mp3")






keys = pygame.key.get_pressed()



#Init variables:
bushes= False
tempProgress= True
temProgress=False
temporaryProgress=0
taklingabout= False
showFlowerPot=True
stopsign=False
inventory = False   #par défaut l'inventaire est fermé



#knowledge init variables:
kbushes=False
kstopsign=False


#dialogues:
Dialogue1p=["Policeman ;I am sorry to have warned you  this late but the matter is urgent !", "some other text"]
explanation1= dialogueFont.render("Policeman: Good evening Detective, press any key to continue", True, (255, 255, 255))





def cutscene1():# Nous n'utilisons plus cette partie, nous la gardons seulement au cas où.
    cscene1d=["Flicker", "Flicker", "Flicker", "You're a goner"]
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

def oftenusedD1(): #This is a function that executes the lines of code that are often used in the first dialogue.
    screen.blit(crimeSceneBG, (0, 0))
    screen.blit(playerDialogue, (0, 0))
    screen.blit(textbox, (200, 450))



def checkanykey(): #This function checks if any key is pressed on the keyboard.
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if temProgress==True: #Temp progress servira a intercaler des dialogues quand le jouer discutera sur le sujet d'un objet qu'il a analyse.
                global temporaryProgress
                temporaryProgress += 1
            else:
                global progress
                progress += 1
            print("click")

def boundaries(): #teleports the player back into the game boundaries if he tries to get out
    global playerX
    if playerX <= 0:
        playerX = 1
    if playerX >= 1150:
        playerX = 1149

def walking_function():#verifie si le joueur est en train de marcher et dans quelle dirrection
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

    for event in pygame.event.get(): #Permet de vérifier quelle touche a ete utilisee et donc dans quelle dirrection il faut orienter le joueur.
        if event.type == pygame.KEYDOWN:
            if event.key == K_RIGHT:
                walkingRight = True #Orientation du joueur
            if event.key == K_LEFT:
                walkingRight = False
    screen.blit(flowerPot1, (523, 450))
    screen.blit(crimeSceneBG, (0, 0))


def show_bg():
    screen.blit(crimeSceneBG, (0, 0))


#keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
#if keys[pygame.K_TAB] and inventory == False:
    #inventory = True


#on vérifie si TAB est pressé et si l'inventaire est fermé
#indique que l'inventaire est maintenant ouvert

#Game loop
running = True
while running:
    for event in pygame.event.get(): #checks if cross is clicked.
        if event.type == QUIT:

            running = False#On ferme le jeu en passant la boucle en false
            print("croix")
    clock.tick(30) #FPS

    print(temporaryProgress)
    if event.type == KEYDOWN:
        if inventory == False and event.key == K_TAB:
            print("i'm trying honest")
            inventory = True
            screen.blit(inventaire, (320, 40))
            if inventory == True and event.key == K_TAB:
                inventory = False
            pygame.display.update()


    #if event.type == KEYDOWN:
        #if event.key == K_TAB and inventory == False:  # on vérifie si TAB est pressé et si l'inventaire est fermé
            #inventory = True  # indique que l'inventaire est maintenant ouvert
            #screen.blit(inventaire, (320, 40))  # L'image de l'inventaire s'affiche désormait à l'écran (inventaire est l'image, et inventory est le booléen!)
            #pygame.display.update()
        #if event.key == K_TAB and inventory == True:  # on vérifie si TAB est pressé et si l'inventaire est ouvert
            #inventory = False  # indique que l'inventaire est maintenant fermé
            #screen.blit(crimeSceneBG, (0, 0))
            #pygame.display.update()

        #if inventory == True:
            #screen.blit(inventaire, (320, 40))
            #pygame.display.update()
        #if kbushes == True and event.key == K_TAB:
            #screen.blit(flowerPot1, (409, 365))
            #pygame.display.update()
        
        
    else:
        if progress == 0:
            temProgress = False
            checkAnyKey=True
            oftenusedD1()
            screen.blit(explanation1, (250,500))#ecrit le premier texte visible à l'ecran
            pygame.display.update()
            checkanykey()#appele la fonction checkanykey() qui permet de vérifier si une touche du clavier est cliquee.

            
            
        if progress == 1:
            temProgress = False
            oftenusedD1()
            toprint = dialogueFont.render("Huf... Puff..., Huf..., Puff. Palms sweaty, this case seems", True, (255, 255, 255))#Ceci sont les paramètres du texte a afficher
            screen.blit(toprint, (250,500)) #Ceci affiche le texte
            toprint = dialogueFont.render("to be big. AND Why is it always me that has to be called ", True, (255, 255, 255))#Une autre ligne de dialogue
            screen.blit(toprint, (250, 520))
            toprint = dialogueFont.render("upon at 2am.", True, (255, 255, 255))
            screen.blit(toprint, (250, 540))
            pygame.display.update()
            checkanykey()

        if progress == 2:
            temProgress = False
            oftenusedD1()
            toprint = dialogueFont.render("My name is Richard Bright, homocide detective at the  ", True, (255, 255, 255)) #Et une autre
            screen.blit(toprint, (250,500))
            toprint = dialogueFont.render("local precinct from Taga, Our great leader Mr. Taga himself called me", True, (255, 255, 255)) #Encore une
            screen.blit(toprint, (250, 520))
            toprint = dialogueFont.render("Let me tell you I got a ", True, (255, 255, 255)) #Fin on a compris quoi.
            pygame.display.update()
            checkanykey()

        if progress == 3:
            temProgress = False
            oftenusedD1()
            toprint = dialogueFont.render("Policeman :I am sorry to have warned you  this late", True, (255, 255, 255))
            screen.blit(toprint, (250, 500))
            toprint = dialogueFont.render("but the matter is urgent !", True, (255, 255, 255))
            screen.blit(toprint, (250, 520))
            pygame.display.update()
            checkanykey()

        if progress == 4:
            temProgress = False
            oftenusedD1()
            toprint = dialogueFont.render("Policeman :We have already investigated a bit,", True, (255, 255, 255))
            screen.blit(toprint, (250, 500))
            toprint = dialogueFont.render("BECAUSE WE HAD BUDGET CUTS LETS GET TO THE ", True, (255, 255, 255))
            screen.blit(toprint, (250, 520))
            toprint = dialogueFont.render("INVESTIGATION", True, (255, 255, 255))
            screen.blit(toprint, (250, 540))
            pygame.display.update()
            checkanykey()
            show_walk= True



        
        if progress== 5:#phase d'enquete
            if inventory==True:
                screen.blit(inventaire, (320, 40))

                keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
                if keys[pygame.K_TAB]:  # Si la valeur de la clé K_TAB est vraie:
                    print("TAB.click")
                    inventory = False
                    time.sleep(0.2)  # afin de ne pas prendre en compte un double press

                pygame.display.update()



            else:
                keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
                if keys[pygame.K_TAB]:  # Si la valeur de la clé K_TAB est vraie:
                    print("TAB.click")
                    inventory=True
                    time.sleep(0.2) #afin de ne pas prendre en compte un double press


                if show_walk:
                    walking_function()
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    print(Mouse_x, Mouse_y)
        
                    if animateWalking == True: #On verifie s'il faut animer le joueur else il sera a l'arret.
                        if walkingRight==True: #On verifie dans quel sens il faut s'orrienter.

                            for counter in range(len(playerWalkR)): #Boucle pour afficher chaque frame de l'animation 1 par 1.
                                walkR = playerWalkR[int(counter)]#WalkR est une variable contenant l'image a afficher. PlayerWalkR est une liste contenant toutes les frames de marche
                                counter = counter + 1
                                screen.blit(crimeSceneBG, (0, 0)) #On blit tout ce qu'il faut.
                                if showFlowerPot==True: #On vérifie si le pot de fleur n'a pas été récupéré
                                    screen.blit(flowerPot1, (523, 417))

                                playerX = playerX + 40 #Apres avoir blit la frame on ajoute 40 a la position du joueur
                                boundaries() #On vérifie si le joueur n'essaie pas de sortir.
                                screen.blit(walkR, (playerX, 350)) #On affiche le joueur
                                pygame.display.update() #On rafraichit l'ecran
                                time.sleep(0.2) #On attends 0.2s afin de rendre l'animation realiste.

                        else:
                            for counter in range(len(playerWalkL)): #C'est presque la meme chose qu'au dessus
                                walkL = playerWalkL[int(counter)] #WalkL est une variable contenant l'image a afficher. PlayerWalkL est une liste contenant toutes les frames de marche
                                counter = counter + 1
                                screen.blit(crimeSceneBG, (0, 0)) #On print tout ce qu'il faut.
                                if showFlowerPot==True: #On vérifie si le pot de fleur n'a pas été récupéré
                                    screen.blit(flowerPot1, (523, 417))
                                playerX = playerX - 40 #Apres avoir blit la frame on ajoute 40 a la position du joueur
                                boundaries()
                                screen.blit(walkL, (playerX, 350))
                                pygame.display.update()
                                time.sleep(0.2)


                    else:
                        if walkingRight==False: #On verifie dans quel sens s'orrienter
                            if showFlowerPot == True:  # On vérifie si le pot de fleur n'a pas été récupéré
                                screen.blit(flowerPot1, (523, 417))
                            screen.blit(playerImgL,(playerX, 350))
                
                        else: #Si l'on ne doit pas s'orrienter a droite alors logiquement il faut aller a gauche.
                            if showFlowerPot == True:  # On vérifie si le pot de fleur n'a pas été récupéré
                                screen.blit(flowerPot1, (523, 417))
                            screen.blit(playerImgR, (playerX, 350))

                pressE=False
    
                print("player x=",playerX)
                if playerX<= 670 and playerX>= 517:

                    toprint=dialogueFont.render("press e to inspect", True, (255, 255, 255))
                    pressE=True
                    bushes= True
                    screen.blit(toprint, (523, 417))
                    toprint=dialogueFont.render("press e to inspect", True, (255, 255, 255))
                    pressEprint=True
                    screen.blit(toprint, (523, 417))
                    pygame.display.update()
        
                elif playerX<=210 and playerX>=20:
                    toprint = dialogueFont.render("press e to inspect", True, (255, 255, 255))
                    screen.blit(toprint, (523, 417))
                    stopsign=True
                    pressE = True

                    #Ajouter les différents éléments à inspecter ici.
        
                else:
                    pygame.display.update()
        
                TalkingAbout=False
                if pressE==True:
                    print("can press e")
                    keys = pygame.key.get_pressed()  # on fait un dictionnaire avec les valeurs de pygame.keys.get_pressed()
                    if keys[pygame.K_e]:  # Si la valeur de la clé K_RIGHT est vraie:
                        print("e.click")
                        #playerX = 5
                        TalkingAbout= True
                        if bushes== True: #On vérifie quel dialogue lancer ici le dialogue bushes
                            print("trying to display")
                    
                            temporaryProgress=0
                            show_walk= False
                            taklingabout= True
                    
                
                
            if taklingabout: #Le joueur inspecte le pot de fleurs et un dialoque se lance
                print("hello")
                oftenusedD1()
                temProgress=True
                if bushes == True: #On lance le lialogue bushes la structure ci-dessous est tres similaire a celle au premier dialogue.

                    if temporaryProgress == 0:
                        checkanykey() #on vérifie si une touche est enfoncée
                        oftenusedD1() #On met l'ecran de dialogue
                        toprint=dialogueFont.render("Nice Bushes", True, (255, 255, 255)) #On affiche les dialogue de la meme maniere que dans le reste du jeu.
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 1:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render("This flower pot seems to have a crack, Detective could we analyse these bushes", True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 2:
                        checkanykey()
                        oftenusedD1()
                        toprint = dialogueFont.render("Right away sir", True, (255, 255, 255))
                        screen.blit(toprint, (250, 500))

                    if temporaryProgress == 3:
                        showFlowerPot = False #On arrete d'afficher le pot de fleur car il a ete recupere pour analyse.
                        tempProgress = 0 #On remet tout les parametres requis afin de retourner a la phase d'enquete.
                        taklingabout = False
                        bushes = False
                        kbushes = True
                        progress = 5
                        show_walk= True
                        temProgress = False 