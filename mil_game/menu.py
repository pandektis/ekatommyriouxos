import pygame, os, sys
from pygame.locals import *
from game import *
from button import Button
pygame.init()
class MenuMode(object):
    """
    Κατάσταση παιχνιδιού Μενού.
    Το κυρίως μενού του παιχνιδιού
    """
    def __init__(self, game):
        self.game = game
        self.index = 0
        self. inputTick = 0
        self.menuButtons = pygame.sprite.Group()
        self.background_img = pygame.image.load('mil_game/images/ek_menu.jpg').convert()
        self.menuItems = ['Νέο παιχνίδι', 'Αποτελέσματα', 'Έξοδος']
        font50 = pygame.font.SysFont("Tahoma", 25)
        for item in self.menuItems:
            btn = Button(200,75, pygame.Color(100,100,100),'mil_game/images/btn_bg.png', True)
            btn.add_text(font50, item, (255,0,0))
            btn.add(self.menuButtons)

    # Θέτουμε την κατάσταση για νέο παιχνίδι
    def setPlayMode(self, mode):
        self.playmode = mode

    # Θέτουμε την κατάσταση για εμφάνιση αποτελεσμάτων.
    def setScoreMode(self, mode):
        self.scoremode = mode

    def draw(self, surface):
        surface.blit(pygame.transform.scale(self.background_img, (surface.get_rect().width, surface.get_rect().height)), (0,0))
        for i, btn in enumerate(self.menuButtons):
            btn.rect.x = surface.get_rect().width//2 - btn.rect.width // 2
            btn.rect.y = surface.get_rect().height // 3 + i * 160

            # surface.blit(btn.image,(surface.get_rect().width // 2 - btn.rect.width //2, surface.get_rect().height //3 + i * 160) )
        self.menuButtons.draw(surface)

    def update(self, gameTime):
        click = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        
        if click and self.inputTick == 0:
            self.inputTick = 250
            for btn in self.menuButtons.sprites():
                if btn.rect.collidepoint(pos):
                    if(btn.msg == self.menuItems[0]):
                        self.game.changeMode(self.playmode)
                    elif(btn.msg == self.menuItems[1]):
                        self.game.changeMode(self.scoremode)
                    elif(btn.msg == self.menuItems[2]):
                        self.game.changeMode(None)
        elif(self.inputTick > 0):
            print("minus")
            self.inputTick -= gameTime

        if(self.inputTick < 0):
            self.inputTick = 0