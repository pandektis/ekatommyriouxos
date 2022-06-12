import pygame, os, sys
from pygame.locals import *
from button import *


class Helper:
    
    def __init__(self, rect, name) -> None:
        self.is_clicked = False
        self.rect = rect
        self.name = name

class HelpersController:

    def __init__(self):
        width = 95
        height = 50
        names = ["fifty", "computer", "other"]
        x = 405
        y = 625
        self.helpers = []
        for i in range(3):
            tmp_rect = pygame.Rect(x + (width * i), y, width, height)
            self.helpers.append(Helper(tmp_rect, names[i]))
        self.done = False
        self.inactive_helpers = []
        self.current_helper = None

    def update(self, gameTime, event_list):
            if self.done or not self.helpers:
                return
            pos = pygame.mouse.get_pos()
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for helper in self.helpers[:]:
                        if helper.rect.collidepoint(pos):
                            self.inactive_helpers.append(helper)
                            self.helpers.remove(helper)
                            self.current_helper = helper
                            # helper.is_clicked = True
                            self.done = True

class HelpersView:

    def __init__(self, helpers_ctrl) -> None:
        self.controller = helpers_ctrl
        self.image = pygame.Surface(self.controller.helpers[0].rect.size)
        self.image.set_colorkey((0,0,0))
        self.image.fill((0,0,0))
        pygame.draw.line(self.image, (255,0,0), self.image.get_rect().topleft, self.image.get_rect().bottomright, 4)

    def draw(self, surface):
        for helper in self.controller.inactive_helpers:
            # if helper.is_clicked:
                
            surface.blit(self.image, helper.rect)
                # pygame.draw.line(surface, (255,0,0), helper.rect.topleft, helper.rect.bottomright, 4)