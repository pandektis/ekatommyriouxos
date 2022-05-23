import pygame, os, sys
from pygame.locals import *

from player import *
from button import Button
from question import *
from game_timer import *

class RoundMsgMode:


    def __init__(self, game, next_mode) -> None:
        self.game = game
        self.next_mode = next_mode
        self.delay = 2000
        self.msg = ""
        self.overlay = pygame.Surface(self.game.mainscreen.get_size())
        self.overlay.set_alpha(200)
        self.overlay.fill((0,0,0))

    def set_msg(self, msg):
        msg_surf = pygame.font.Font.render(None,msg,True, (255,0,0), (0,0,0))
        msg_surf.set_colorkey((0,0,0))
        self.overlay.blit(msg_surf, msg_surf.get_rect(center = self.overlay.get_rect.center) )

    def update(self, gameTime, event_list):
        if self.delay <= 0:
            self.game.changeMode(self.next_mode)
            self.delay = 2000
        self.delay -= gameTime
        

    def draw(self, surface):
        surface.blit(self.overlay, (0,0))
        pass



class GameMode:
    """
    Κατάσταση παιχνιδιού Παιχνίδι.

    Περιέχει τα αντικείμενα που χρειάζονται για να παιχτεί το παιχνίδι
    (player, question, timer, κ.α.)
    Οι μεθόδοι update και draw καλούν κάθε φορά τις αντίστοιχες μεθόδους
    από τα περιεχόμενα αντικείμενα.    
    """
    def __init__(self, game, gameOverMode):
        self.game = game
        self.gameOverMode = gameOverMode
        self.time_allowed = 60
        self.background_img = pygame.image.load("mil_game/images/set_mil.jpg")
        # self.background_img = pygame.transform.scale(self.background_img, self.game.mainscreen.get_size())
        self.player_controller = PlayerController("Player")
        self.player_view = PlayerView(self.player_controller)
        self.question_controller = QuestionController()
        self.time_counter = TimerController(self.time_allowed)
        self.controllers = None
        self.views = None
        
        self.setup()

    def setup(self):
        question_view = QuestionView(self.question_controller)
        timer_view = TimerView(self.time_counter)
        self.controllers = [self.question_controller, self.player_controller, self.time_counter]
        self.views = [self.player_view, question_view, timer_view]


    def set_name(self, name):
        if name:
            self.player_controller.model.name = name
            self.player_view.update_name()

    def update(self, gameTime, event_list):
        """ Γενική συνάρτηση για ενημέρωση όλων των αντικειμένων που αποτελούν το παιχνίδι
        Καλεί τις ξεχωριστές update κάθε αντικειμένου ώστε να ενημερωθούν το καθένα μόνο του
        αν έχει γίνει κάποια αλλαγή.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου. """
        # Ζητάμε από κάθε αντικείμενο που αποτελεί το παρόν mode παιχνιδιού να κάνει τους ελέγχους και τις ενημερώσεις.

        for manager in self.controllers:
            manager.update(gameTime, event_list)
        
        # Μετά το update ρωτάμε τα αντικείμενα για τις συνθήκες που θέλουμε
        # Παράδειγμα ακολουθεί. Αυτές τις συνθήκες /ελέγχους βέβαια μπορούμε να τις μοιράσουμε 
        # στα αντικείμενά που θέλουμε να ελέγξουμε
        #
        for event in event_list:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("PRESS A")
                    print("Response Time :", self.time_counter.model.counter)
                    self.time_counter.start()
                if event.key == pygame.K_b:
                    print("PRESS B")
                    print("Response Time :", self.time_counter.model.counter)
                    self.time_counter.stop()
                if event.key == pygame.K_c:
                    print("PRESS C")
                    print("Response Time :", self.time_counter.model.counter)
                   
                if event.key == pygame.K_d:
                    print("PRESS D")
                    print("Response Time :", self.time_counter.model.counter)
                    
                if event.key == pygame.K_5:
                    print("PRESS 5")
                
                    
                if event.type == pygame.K_q:
                    print("PRESS Q")
                    pygame.quit();
        

        # εδώ αντί για event, ρωτάμε ένα αντικείμενο αν έγινε κάτι.
        if(self.player_controller.model.lives == 0):
            pass #game over

        
        
        

    def draw(self, surface):
        """Συνάρτηση για την εμφάνιση της οθόνης του παιχνιδιού
        Εμφανίζουμε το background και ότι άλλο σταθερό ανήκει στο παιχνίδι
        και μετά καλούμε την draw κάθε υπεύθυνου αντικειμένου για να εμφανίσει κι αυτό τα δικά του και 
        να ολοκληρωθεί η εικόνα (frame)
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου. 
        """
        ### Κώδικας για background και ό,τι άλλο δεν ανήκει σε κάποιο άλλο αντικείμενο
        surface.blit(self.background_img, (0,0))
        # Ζητάμε από κάθε View να εμφανίσει αυτά που έχει στην οθόνη
        for painter in self.views:
            painter.draw(surface)
        