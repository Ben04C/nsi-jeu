from typing import Any, Union

import pygame


class Menu():
    def __init__(self, game):
        self.game = game  # lets us access previous info
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.cursor_rect = pygame.Rect(0, 0, 20, 20, )  # x y width and height position for cursor
        self.offset = - 100  # making sure cursor doesnt have to be on top of the text

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.midtop[0], self.cursor_rect.midtop[1])

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()  # resets the keyboard flags


class MainMenu(Menu):  # making sure we can use the variables.

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"  # when game starts main cursor points at start game
        self.startx, self.starty = self.mid_w, self.mid_h + 30  # position of start game text
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70  # position of options text
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 50  # position of credits text
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  # starting position of the cursor

    def display_menu(self):  # displays or doesnt display the menu
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)  # sets background to black
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 20)  # postitioning text
            self.game.draw_text('Start Game', 20, self.startx, self.starty)
            self.game.draw_text('Options', 20, self.optionsx, self.optionsy)
            self.game.draw_text('Credits', 20, self.creditsx, self.creditsy)
            self.game.draw_text('Press enter to continue', 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100)
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

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_imput()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("You have no options, just play the game :)", 20, self.volx, self.voly)
            self.game.draw_text("Press Backspace to go back to the Main Menu", 10, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_imput(self):
        if self.game.BACK_KEY:
            self.game.curr_menu =self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self. controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self. voly)
            elif self.game.START_KEY:
                pass

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.draw_text('Made by:', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 125)
            self.game.draw_text('Benjamin', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 90)
            self.game.draw_text('Michiel', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 55)
            self.game.draw_text('Valentina', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Press Backspace to go back to the Main Menu', 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 15)
            self.blit_screen()