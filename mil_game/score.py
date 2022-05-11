import pygame, os, sys
import pickle
from pygame.locals import *
from game import *
from button import Button
from player import Player

class ScoreMode:


    def __init__(self, game, nextMode, players):
        self.game = game
        self.players = players
        self.nextMode = nextMode
        self.bgImage = pygame.image.load('mil_game/images/ek_set.jpg').convert()
        font50 = pygame.font.SysFont("Tahoma", 25)
        self.menu_btn =Button(200,75, pygame.Color(100,100,100),'mil_game/images/btn_bg.png', True)
        self.menu_btn.add_text(font50, "MENOY", (255,0,0))
        self.menu_btn.rect.bottom = self.game.mainscreen.get_rect().bottom - 20
        self.buttons = [Button(700,30,pygame.Color(100,100,100)) for _ in range(10)]
        self.groupb = pygame.sprite.Group()
        self.inputTick = 0
        h = 10
        
        for btn, pl in zip(self.buttons, self.players):
            print(btn, len(self.buttons))
            print(pl, len(self.players))
            btn.add_text(font50, str(pl), (255,0,0))
            btn.rect.y = h
            h += btn.rect.height + 5
            btn.add(self.groupb)

    def update(self, gameTime):
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




