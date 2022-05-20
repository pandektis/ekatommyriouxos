import pygame, os, sys
from pygame.locals import *
from game import *
from button import Button

class InputMode(object):
    """
    Κλάση για είσοδο του ονόματος
    Αποτελεί μία κατάσταση (mode) του παιχνιδιού
    """

    def __init__(self, game, nextMode):
        self.game = game
        self.nextMode = nextMode
        self.background_img = pygame.image.load('mil_game/images/ek_set.jpg')
        self.font_size = 28
        self.msg_font = pygame.font.Font(None, self.font_size)
        
        self.user_prompt_surf = self.msg_font.render("Δώστε όνομα παίκτη (ENTER για default):", True, (255,0,0))
        self.user_name = ""
        
        width, height = pygame.display.get_window_size()
        self.msg_rect = pygame.Rect(0, 0, self.user_prompt_surf.get_rect().width + 4, self.font_size * 2 + 4)
        self.msg_rect.center = width / 2, height / 2
        self.overlay = pygame.Surface((width, height))
        self.overlay.set_alpha(210)
        self.overlay.fill((0,0,0))


    def update(self, gameTime, event_list):
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.user_name = self.user_name[:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.nextMode.set_name(self.user_name)
                    self.game.changeMode(self.nextMode)
                else:
                    self.user_name += event.unicode
                


    def draw(self, surface):
        surface.blit(self.background_img, (0,0))
        surface.blit(self.overlay, (0,0))
        pygame.draw.rect(surface, (0,0,255), self.msg_rect, 2)
        surface.blit(self.user_prompt_surf, (self.msg_rect.x + 2, self.msg_rect.y ))
        input_surf = self.msg_font.render(self.user_name, True, (0, 255, 0))
        surface.blit(input_surf, self.msg_rect.midleft)


class MenuMode(object):
    """
    Κατάσταση παιχνιδιού Μενού.
    Το κυρίως μενού του παιχνιδιού
    """
    def __init__(self, game):
        self.game = game
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

    def update(self, gameTime, event_list):
        click = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        
        if click and self.inputTick == 0:
            self.inputTick = 250
            for btn in self.menuButtons.sprites():
                if btn.rect.collidepoint(pos):
                    if(btn.msg == self.menuItems[0]):
                        self.game.changeMode(InputMode(self.game, self.playmode))
                        # self.game.changeMode(self.playmode)
                    elif(btn.msg == self.menuItems[1]):
                        self.game.changeMode(self.scoremode)
                    elif(btn.msg == self.menuItems[2]):
                        self.game.changeMode(None)
        elif(self.inputTick > 0):
            print("minus")
            self.inputTick -= gameTime

        if(self.inputTick < 0):
            self.inputTick = 0