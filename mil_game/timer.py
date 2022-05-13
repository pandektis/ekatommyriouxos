import pygame, os, sys
from pygame.locals import *
from math import pi


class TimerModel:


    def __init__(self, seconds):
        self.counter = seconds
        self.isover = False

    

class TimerController:
    """ Κλάση για τον έλεγχο και την ενημέρωση του timer.

        Έχει μέθοδο update() για να ελέγχει τα timerEvents και να κατεβάζει το χρόνο
        όταν γίνει 0, διαμορφώνει το model.isover σε True
        """
    def __init__(self, gameTime, event_list):
        self.model = TimerModel(60)
        
    def update(self, gameTime):
        if self.model.counter > 0:
            self.model.counter -= 1



class TimerView:

    def __init__(self, timer):
        self.timer = timer
        self.offset = (pi * 2) / self.timer.model.counter

    def draw(self, surface):
        cur_offset = self.offset * self.timer.model.counter
        surface.fill((0,0,0))
        rect = pygame.Rect(surface.get_rect().width // 2 - 100, surface.get_rect().height // 2 - 100,200,200 )
        pygame.draw.arc(surface, (255,0,0), rect,  pi /2, pi / 2 + cur_offset )



if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    model = TimerModel(60)
    cntrler = TimerController(None, None)
    timer_view = TimerView(cntrler)
    fps = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
        cntrler.update(None)
        timer_view.draw(screen)
        pygame.display.update()
        fps.tick(1) # έχω βάλει 1 εδώ για επίδειξη μόνο, κανονικά ελέγχουμε το χρόνο με το event, ή μέσα στην update()
