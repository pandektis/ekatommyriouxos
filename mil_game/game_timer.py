import pygame, os, sys
from pygame.locals import *
from math import pi


class TimerModel:


    def __init__(self, seconds):
        self.time_allowed = seconds
        self.counter = self.time_allowed
        self.is_over = False
        self.is_running = False

    

class TimerController:
    """ Κλάση για τον έλεγχο και την ενημέρωση του timer.

        Έχει μέθοδο update() για να ελέγχει τα timerEvents και να κατεβάζει το χρόνο
        όταν γίνει 0, διαμορφώνει το model.isover σε True
        """
    def __init__(self, time_total,):
        self.model = TimerModel(time_total)
        self.COUNTDOWN = pygame.USEREVENT + 1
        self.show = False
        
        
    def update(self, gameTime,  event_list):
        """ Ενημερώνουμε τον timer, είτε με USEREVENT είτε μετρώντας χειροκίνητα χρόνο.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου.
        Όταν γίνει 0 ενημερώνουμε τη μεταβλητή του isover και την ελέγχει απ' έξω το παιχνίδι."""
        for event in event_list:
            if event.type == self.COUNTDOWN:
                if self.model.counter > 0:
                    self.model.counter -= 1
                elif self.model.counter == 0:
                    self.stop()
                    self.model.is_over = True
                    self.model.is_running = False
            

    def start(self):
        pygame.time.set_timer(self.COUNTDOWN,1000)
        self.model.is_running = True
        
    def stop(self):
        pygame.time.set_timer(self.COUNTDOWN, 0)
        self.is_running = False

    def reset(self):
        self.model.counter = self.model.time_allowed
        self.model.is_over = False
        self.model.is_running = False



class TimerView:

    def __init__(self, timer):
        self.timer = timer
        self.offset = (pi * 2) / self.timer.model.counter
        # self.rect = pygame.Rect(pygame.display.get_surface().get_rect().width // 2 - 50, pygame.display.get_surface().get_rect().height // 2 - 50,100,100 )
        self.rect = pygame.Rect(437,210,221,221)
        self.timer_surf = pygame.Surface(self.rect.size)
        # print(self.timer_surf.get_rect())
        print("timer  rect ",self.rect)
        print("timer_surf rect", self.timer_surf.get_rect())

    def draw(self, surface):
        """
        Συνάρτηση για να εμφανίζει τον κύκλο και το νούμερο με τα δευτερόλεπτα.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου.
        Θέλει συμπλήρωση"""
        cur_offset = self.offset * self.timer.model.counter
        
        self.timer_surf.fill((0,0,255))
        self.timer_surf.set_colorkey((0,0,255))
        pygame.draw.arc(self.timer_surf, (255,0,0), self.timer_surf.get_rect(),  pi /2, pi / 2 + cur_offset, 28)
        text_surf = pygame.font.Font(None, 30).render(str(self.timer.model.counter),True, (255,0,0))
        # self.timer_surf.blit(text_surf, text_surf.get_rect(center = self.rect.center))
        surface.blit(self.timer_surf, self.rect)
        surface.blit(text_surf, text_surf.get_rect(center = self.rect.center))

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
