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
        self.bgImage = pygame.image.load('images/ek_set.jpg').convert()
        self.scoreline_bg = pygame.transform.scale(pygame.image.load('images/btn_bg.png').convert_alpha(), (700,50))
        # self.scoreline_bg.set_colorkey(0,0,0)
        self.btn_font = pygame.font.SysFont(None, 25)
        self.menu_btn =Button(200,50, pygame.Color(100,100,100),'images/btn_bg.png', True)
        self.menu_btn.add_text(self.btn_font, "Μενού Επιλογών", (255,128,0))
        self.menu_btn.rect.bottom = self.game.mainscreen.get_rect().bottom - 20
        # self.buttons = [Button(700,50,pygame.Color(100,100,100), 'images/btn_bg.png') for _ in range(10)]
        self.scorelines = []
        self.textlines = []
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
              
        for i in range(10):
            self.scorelines.append(pygame.Rect(290, self.h, 700, 50))
            self.h += 65

    def onEnter(self, oldMode):
        print("Score mode enter", type(self.players))
            
        if self.curr_player:
            self.players.append(self.curr_player)
            self.curr_player = None

        self.players.sort(key = lambda pl : pl.daep, reverse=True)
        
        self.players = self.players[:10]

        for i in range(10):
            self.textlines.append(self.btn_font.render(str(self.players[i]), True,(255,60,30) ))


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
        
        pos = pygame.mouse.get_pos()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.menu_btn.rect.collidepoint(pos):
                        self.game.changeMode(self.nextMode)

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.bgImage, (surface.get_rect().width, surface.get_rect().height)), (0,0))
        # self.groupb.draw(surface)
        for i in range(10):
            surface.blit(self.scoreline_bg, self.scorelines[i])
            # text_line = self.btn_font.render(str(self.players[i]), True, (255,60,30))
            surface.blit(self.textlines[i], self.textlines[i].get_rect(center = self.scorelines[i].center))
        surface.blit(self.menu_btn.image, self.menu_btn.rect)



