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
    def __init__(self, time_total,):
        self.model = TimerModel(time_total)
        
    def update(self, gameTime,  event_list):
        """ Ενημερώνουμε τον timer, είτε με USEREVENT είτε μετρώντας χειροκίνητα χρόνο.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου.
        Όταν γίνει 0 ενημερώνουμε τη μεταβλητή του isover και την ελέγχει απ' έξω το παιχνίδι."""
        if self.model.counter > 0:
            self.model.counter -= 1
        elif self.model.counter == 0:
            self.model.isover = True
            self.model.counter = 60



class TimerView:

    def __init__(self, timer):
        self.timer = timer
        self.offset = (pi * 2) / self.timer.model.counter
        self.rect = pygame.Rect(pygame.display.get_surface().get_rect().width // 2 - 100, pygame.display.get_surface().get_rect().height // 2 - 100,200,200 )
        self.timer_surf = pygame.Surface(self.rect.size)
        print(self.timer_surf.get_rect())
        print(self.rect)

    def draw(self, surface):
        """
        Συνάρτηση για να εμφανίζει τον κύκλο και το νούμερο με τα δευτερόλεπτα.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου.
        Θέλει συμπλήρωση"""
        cur_offset = self.offset * self.timer.model.counter
        self.timer_surf.fill((0,0,255))
        
        pygame.draw.arc(self.timer_surf, (255,0,0), self.timer_surf.get_rect(),  pi /2, pi / 2 + cur_offset )
        
        surface.blit(self.timer_surf, self.rect)


#### Τεστ, to be deleted
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    # model = TimerModel(60)
    cntrler = TimerController(60)
    timer_view = TimerView(cntrler)
    fps = pygame.time.Clock()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.quit()
        cntrler.update(None, None)
        timer_view.draw(screen)
        pygame.display.update()
        fps.tick(1) # έχω βάλει 1 εδώ για επίδειξη μόνο, κανονικά ελέγχουμε το χρόνο με το event, ή μέσα στην update()
