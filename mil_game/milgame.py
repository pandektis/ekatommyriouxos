import pygame, os, sys
from pygame.locals import *

from player import *
from button import Button
from question import *
from game_timer import *
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
        self.player_controller = PlayerController("New Player")
        self.question_controller = QuestionController()
        self.time_counter = TimerController(self.time_allowed)
        self.controllers = None
        self.views = None
        
        self.setup()

    def setup(self):
        player_view = PlayerView(self.player_controller)
        question_view = QuestionView(self.question_controller)
        timer_view = TimerView(self.time_counter)
        self.controllers = [self.question_controller, self.player_controller, self.time_counter]
        self.views = [player_view, question_view, timer_view]



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
                    
                if event.key == pygame.K_b:
                    print("PRESS B")
                    print("Response Time :", self.time_counter.model.counter)
                    
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
        

        # Ζητάμε από κάθε View να εμφανίσει αυτά που έχει στην οθόνη
        for painter in self.views:
            painter.draw(self.game.mainscreen)
        