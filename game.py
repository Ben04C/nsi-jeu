import pygame
# CODE FOR THE PRE GAME MENU
from menu import MainMenu


class Game():
    def __init__(self):        #defining all the properties of the game menu
        pygame.init()
        self.running, self.playing = True, False        #check if game is being run and if user is playing
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, = False, False, False, False     #defining all the keys used in the menu
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720      #setting the dimensions of the menu
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))         #giving dimensions a name
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))       #choosing to display dimensions
        self.font_name = pygame.font.get_default_font()     #Choosing the font
        self.BLACK, self.WHITE = (0, 0, 0,), (255, 255, 255)        #defining the colours black and white
        self.curr_menu = MainMenu(self)

    def game_loop(self):        #defining the loop that displays the menu
        while self.playing:
            self.check_events()     #check if keys are pressed
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)  # set background to black
            self.draw_text("thanks for playing", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)       #display text in centre of screen
            self.window.blit(self.display, (0, 0))      #helps locate the rectangle on the screen
            pygame.display.update()  # physically moves the image on the computer screen
            self.reset_keys()       #checks if the player is still holding down the key


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #checks whether to end program or not
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # check if player has pressed the enter key
                    self.START_KEY = True
            if event.type == pygame.K_BACKSPACE:  # check if player has pressed the backspace key
                self.BACK_KEY = True
            if event.type == pygame.K_DOWN:  # check if player has pressed the down key
                self.DOWN_KEY = True
            if event.type == pygame.K_UP:  # check if player has pressed the up key
                self.UP_KEY = True


    def reset_keys(self):
        self.START_KEY, self.BACK_KEY, self.DOWN_KEY, self.UP_KEY = False, False, False, False


    def draw_text(self, text, size, x, y):      #message, font, size, coordinates
        font = pygame.font.Font(self.font_name, size)     #choose font
        text_surface = font.render(text, True, self.WHITE)      #choose colour
        text_rect = text_surface.get_rect()     #create rectangle
        text_rect.center = (x,y)        #centre rectangle
        self.display.blit(text_surface, text_rect)       #display rectangle with text
