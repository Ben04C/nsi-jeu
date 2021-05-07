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

crimeSceneBG = pygame.image.load("backgrounds/First_Scene.png")

running = True
while running:
    for event in pygame.event.get(): #checks if cross is clicked.
        if event.type == pygame.QUIT:
            running = False
    screen.blit(icon, (500, 400))