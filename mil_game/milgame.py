import pygame, os, sys
from pygame.locals import *

class MainGame(object):
    def __init__(self, gameName, width, height) -> None:
        pygame.init()
        pygame.display.set_caption(gameName)

        self.clock = pygame.time.Clock()
        self.mainscreen = pygame.display.set_mode((width, height))
        self.background = pygame.Color(0, 0, 0)
        self.currentMode = None

    def changeMode(self, newMode):
        if(newMode == None):
            pygame.quit()
            sys.exit()
            
        self.currentMode = newMode


    def play(self, startMode):

        self.changeMode(startMode)
        # print(self.currentMode)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            gameTime = self.clock.get_time()

            if(self.currentMode):
                self.currentMode.update(gameTime)

            # self.mainscreen.fill(self.background)
            if(self.currentMode):
                self.currentMode.draw(self.mainscreen)
                
            pygame.display.update()
            self.clock.tick(30)