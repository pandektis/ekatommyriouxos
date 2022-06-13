import pygame, os, sys
from pygame.locals import *
from game import *
from milgame import *
from button import Button

class InputMode(BaseMode):
    """
    Κλάση για είσοδο του ονόματος
    Αποτελεί μία κατάσταση (mode) του παιχνιδιού
    """

    def __init__(self, game, nextMode):
        super().__init__(game)
        self.nextMode = nextMode
        width, height = pygame.display.get_window_size()
        self.background_img = pygame.image.load('mil_game/images/ek_menu.jpg')
        self.background_img = pygame.transform.scale(self.background_img, (width, height))
        self.font_size = 28
        self.msg_font = pygame.font.Font(None, self.font_size)
        
        self.user_prompt_surf = self.msg_font.render("Δώστε όνομα παίκτη (ENTER για default):", True, (255,128,0))
        self.user_name = ""
        # self.cursor = pygame.Rect
        
        self.msg_rect = pygame.Rect(0, 0, self.user_prompt_surf.get_rect().width + 4, self.font_size + 10)
        self.input_rect = pygame.Rect.copy(self.msg_rect)
        self.msg_rect.midbottom = width / 2, height / 2
        self.input_rect.midtop = width / 2, height / 2
        self.overlay = pygame.Surface((width, height))
        self.overlay.set_alpha(150)
        self.overlay.fill((0,0,0))


    def update(self, gameTime, event_list):
        """
        Έλεγχος για είσοδο χρήστη και δημιουργία συμβολοσειράς ονόματος.

        """
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # Αν πατηθεί BACKSPACE σβήνουμε από τη συμβολοσειρά το τελευταίο γράμμα
                    self.user_name = self.user_name[:-1]
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # Αν πατηθεί ENTER ή RETURN περνάμε το όνομα στην επόμενη κατάσταση (GameMode) και αλλάζουμε κατάσταση
                    self.nextMode.set_name(self.user_name)
                    self.game.changeMode(self.nextMode)
                else:
                    # Αλλιώς προσθέτουμε στη γραμματοσειρά τον κωδικό unicode του πλήκτρου που πατήθηκε
                    self.user_name += event.unicode
                


    def draw(self, surface):
        """
        Μέθοδος για την εμφάνιση του background, μηνύματος και πλαισίου εισάγωγής
        """
        surface.blit(self.background_img, (0,0))
        surface.blit(self.overlay, (0,0))
        pygame.draw.rect(surface, (0,128,255), self.input_rect, 1)
        surface.blit(self.user_prompt_surf, (self.msg_rect.x + 2, self.msg_rect.y ))
        input_surf = self.msg_font.render(self.user_name, True, (128, 255, 0))
        surface.blit(input_surf, (self.input_rect.left +4, self.input_rect.top +5))


class MenuMode(BaseMode):
    """
    Κατάσταση παιχνιδιού Μενού.
    Το κυρίως μενού του παιχνιδιού
    """

    def __init__(self, game):
        super().__init__(game)
        self.menuButtons = pygame.sprite.Group()
        self.background_img = pygame.image.load('mil_game/images/ek_menu.jpg').convert()
        self.menuItems = ['Νέο παιχνίδι', 'Αποτελέσματα', 'Έξοδος']
        font_size = 25
        btn_font = pygame.font.SysFont(None, font_size)
        for item in self.menuItems:
            btn = Button(200,font_size *2, pygame.Color(100,100,100),'mil_game/images/btn_bg.png', clickable = True)
            btn.add_text(btn_font, item, (255,128,0))
            btn.add(self.menuButtons)

    # Θέτουμε την κατάσταση για νέο παιχνίδι
    def setPlayMode(self):
        self.playmode = GameMode(self.game, self.scoremode)

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
        for sp in self.menuButtons.sprites():
            surface.blit(sp.text_image, sp.rect)

    def onEnter(self, oldMode):
        self.setPlayMode()

    def update(self, gameTime, event_list):
        pos = pygame.mouse.get_pos()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for btn in self.menuButtons.sprites():
                        if btn.rect.collidepoint(pos):
                            if(btn.msg == self.menuItems[0]):
                                self.game.changeMode(InputMode(self.game, self.playmode))
                                # self.game.changeMode(self.playmode)
                            elif(btn.msg == self.menuItems[1]):
                                self.game.changeMode(self.scoremode)
                            elif(btn.msg == self.menuItems[2]):
                                self.game.changeMode(None)
