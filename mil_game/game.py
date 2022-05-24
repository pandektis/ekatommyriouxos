import pygame, os, sys
from pygame.locals import *

class BaseMode(object):


    def __init__(self, game) -> None:
        self.game = game

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def update(self, gameTime, event_list):
        pass

    def draw(self, surface):
        pass

class MainGame(object):
    """
    Κλάση για την υλοποίηση του κυρίως βρόχου του παιχνιδιού

    Εδώ γίνεται η εμφάνιση / ανανέωση κάθε κατάστασης του παιχνιδιού

    Αυτή η κλάση είναι έτοιμη
    """
    def __init__(self, gameName, width, height) -> None:
        pygame.init()
        pygame.display.set_caption(gameName)

        self.clock = pygame.time.Clock()
        self.mainscreen = pygame.display.set_mode((width, height))
        self.background = pygame.Color(0, 0, 0)
        self.currentMode = None

    def changeMode(self, newMode):
        """
        Αλλάζουμε κατάσταση παιχνιδιού.
        Αν δεν υπάρχει κατάσταση, τερματίζουμε το παιχνίδι
        """

        if(self.currentMode):
            self.currentMode.onExit()

        if(newMode == None):
            pygame.quit()
            sys.exit()
            
        self.currentMode = newMode
        newMode.onEnter()


    def play(self, startMode):
        """
        Τρέχουμε το παιχνίδι
        """
        self.changeMode(startMode)
        # print(self.currentMode)
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            gameTime = self.clock.get_time()

            if(self.currentMode):
                self.currentMode.update(gameTime, event_list)

            # self.mainscreen.fill(self.background)
            if(self.currentMode):
                self.currentMode.draw(self.mainscreen)
                
            pygame.display.update()
            self.clock.tick(30)