from typing import Any, Union

import pygame
from game import *
firstTime = True


insiderprogress=0
print("progress initialised")
keyMultiplier=0

Reminder=0
Reverse=0
Number=0

#Background
crimeSceneBG = pygame.image.load("assets/backgrounds/Game_First_Scene_bigger_res.png")
MenuBackground = pygame.image.load("assets/backgrounds/Menu_Background_Game_First_Scene_bigger_res_.png")
keyMultiplier = 0


def returnFalse():
    if start==True:
        return False
    else:
        return True



def passwordProgress():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP0]:
        global insiderprogress
        global keyMultiplier
        insiderprogress = insiderprogress + 0 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP1]:
        insiderprogress = insiderprogress + 1 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP2]:
        insiderprogress = insiderprogress + 2 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP3]:
        insiderprogress = insiderprogress + 3 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP4]:
        insiderprogress = insiderprogress + 4 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP5]:
        insiderprogress = insiderprogress + 5 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP6]:
        insiderprogress = insiderprogress + 6 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP7]:
        insiderprogress = insiderprogress + 7 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP8]:
        insiderprogress = v + 8 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)
    if keys[pygame.K_KP9]:
        insiderprogress = insiderprogress + 9 * 10 ** keyMultiplier
        keyMultiplier += 1
        time.sleep(0.2)
        print(insiderprogress)

    if keys[pygame.K_TAB]:
        time.sleep(0.2)
        global Reminder
        global Reverse
        global Number
        print(insiderprogress)
        Number=insiderprogress
        while (Number > 0):
            Reminder = Number % 10
            Reverse = (Reverse * 10) + Reminder
            Number = Number // 10
        progress=Reverse
        print(progress)
        global start
        start=True
        #START THE GAME






class Menu():
    def __init__(self, game):
        self.game = game  # lets us access previous info
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20, )  # x y width and height position for cursor
        self.offset = - 100  # making sure cursor doesnt have to be on top of the text

    def draw_cursor(self):
        self.game.draw_text('-->', 25, self.cursor_rect.midtop[0], self.cursor_rect.midtop[1])      #drawing the cursor

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()  # resets the keyboard flags


class MainMenu(Menu):  # making sure we can use the variables.

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"  # when game starts main cursor points at start game
        self.startx, self.starty = self.mid_w, self.mid_h + - 90  # position of start game text
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50  # position of options text
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + -20  # position of credits text
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  # starting position of the cursor

    def display_menu(self):  # displays or doesnt display the menu
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            #self.game.display.fill(self.game.BLACK)  # sets background to black
            self.game.display.blit(MenuBackground,(0, 0))
            #(crimeSceneBG, (0, 0))
            self.game.draw_text('Main Menu', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)  # postitioning text
            self.game.draw_text('Start Game', 30, self.startx, self.starty)     # postitioning text
            self.game.draw_text('Options', 30, self.optionsx, self.optionsy)        # postitioning text
            self.game.draw_text('Credits', 30, self.creditsx, self.creditsy)        # postitioning text
            self.game.draw_text('Press enter to continue', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 200)      # postitioning text
            self.draw_cursor()
            self.check_input()
            self.blit_screen()

    def move_cursor(self):  # function that makes sure the cursor moves correctly (down and up)
        if self.game.DOWN_KEY:  # down
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:  # up
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):      #Checking if enter is being pressed on one of the options if so it will be moved on to the next step
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class OptionsMenu(Menu):        #positioning the text for the options menu
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        

    def display_menu(self):     #displaying the text where it should be
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_imput()
            self.game.display.blit(MenuBackground,(0, 0))       #displaying backgound
            self.game.draw_text('Options', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text("Enter a progress number", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 -50)
            self.game.draw_text("and press enter", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 +0)
            self.game.draw_text("to skip to where you left off", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 +50)
            self.game.draw_text("Press Backspace to go back to the Main Menu", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 +200)
            self.blit_screen()
            #SYTEME DE MOT DE PASSE
            passwordProgress()

                

    def check_imput(self):
        if self.game.BACK_KEY:      #takes you back to Main Menu
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):          #displaying the text where it should be
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:       #takes you back to Main Menu
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            #self.game.display.fill(self.game.BLACK)
            self.game.display.blit(MenuBackground,(0, 0))       #displaying backgound
            self.game.draw_text('Credits', 50, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text('Made by:', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 125)
            self.game.draw_text('Benjamin', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text('Michiel', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 25)
            self.game.draw_text('Valentina', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100)
            self.game.draw_text('Press Backspace to go back to the Main Menu', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 200)
            self.blit_screen()