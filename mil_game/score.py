import pygame, os, sys
import pickle
from pygame.locals import *
from game import *
from button import Button
from milgame import GameMode
from player import Player

class ScoreMode(BaseMode):

    def __init__(self, game, nextMode):
        super().__init__(game)
        self.players = []
        self.nextMode = nextMode
        self.bgImage = pygame.image.load('mil_game/images/ek_set.jpg').convert()
        self.btn_font = pygame.font.SysFont(None, 25)
        self.menu_btn =Button(200,50, pygame.Color(100,100,100),'mil_game/images/btn_bg.png', True)
        self.menu_btn.add_text(self.btn_font, "Μενού Επιλογών", (255,128,0))
        self.menu_btn.rect.bottom = self.game.mainscreen.get_rect().bottom - 20
        self.buttons = [Button(700,50,pygame.Color(100,100,100), 'mil_game/images/btn_bg.png') for _ in range(10)]
        self.groupb = pygame.sprite.Group()
        self.inputTick = 0
        self.curr_player = None
        self.h = 50
        try:
            with open('scores.data', 'rb') as file:
                self.players = pickle.load(file)
        except:
            for i in range(10):
                self.players.append(Player("Player " + str(i+1)))
                # print(self.players[i])

        


    def onEnter(self, oldMode):
        print("Score mode enter", type(self.players))
        print(type(self.players))
        print(self.players == [])
    
        self.players.append(self.curr_player)
        for pl in self.players:
            print(pl)
        self.players.sort(key = lambda pl : pl.daep, reverse=True)
        for i, pl in enumerate(self.players):
            print(i, " -> ",pl)
        self.players = self.players[:10]

        for btn, pl in zip(self.buttons, self.players):
            btn.add_text(self.btn_font, str(pl), (255,60,30))
            btn.rect.x = 290
            btn.rect.y = self.h
            self.h += btn.rect.height + 15
            btn.add(self.groupb)
        


    def onExit(self):
        self.h = 50
        try:
            with open('scores.data', 'wb') as file:
                pickle.dump(self.players, file)
        except:
            print("Πρόβλημα στο άνοιγμα του αρχείου αποτελεσμάτων")

    def update(self, gameTime, event_list):
        """
        Μέθοδος update
        """
        click = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()

        if(click and self.inputTick == 0):
            self.inputTick = 250
            if(self.menu_btn.rect.collidepoint(pos)):
                self.game.changeMode(self.nextMode)
        elif(self.inputTick > 0):
            self.inputTick -= gameTime
        
        if(self.inputTick < 0):
            self.inputTick = 0

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.bgImage, (surface.get_rect().width, surface.get_rect().height)), (0,0))
        self.groupb.draw(surface)
        surface.blit(self.menu_btn.image, self.menu_btn.rect)




