import pygame, os, sys
from pygame.locals import *

from game import *
from player import *
from button import Button
from question import *
from game_timer import *
from helpers import *

class RoundMsgMode(BaseMode):


    def __init__(self, game, next_mode) -> None:
        super().__init__(game)
        self.next_mode = next_mode
        self.delay = 2000
        self.msg = "Επόμενη ερώτηση"
        self.overlay = pygame.Surface(self.game.mainscreen.get_size())
        self.overlay.set_alpha(200)
        self.overlay.fill((0,0,0,200))
        msg_font = pygame.font.Font(None, 30)
        self.msg_surf = pygame.font.Font.render(msg_font,self.msg,True, (255,0,0), (0,0,0))
        self.msg_surf.set_colorkey((0,0,0))

    def set_msg(self, msg):
        self.msg_surf = pygame.font.Font.render(None,msg,True, (255,0,0), (0,0,0))
        self.msg_surf.set_colorkey((0,0,0))
        

    def update(self, gameTime, event_list):
        if self.delay <= 0:
            self.game.changeMode(self.next_mode)
            self.delay = 2000
        self.delay -= gameTime
        

    def draw(self, surface):
        surface.blit(self.msg_surf, (0,0))
        



class GameMode(BaseMode):
    """
    Κατάσταση παιχνιδιού Παιχνίδι.

    Περιέχει τα αντικείμενα που χρειάζονται για να παιχτεί το παιχνίδι
    (player, question, timer, κ.α.)
    Οι μεθόδοι update και draw καλούν κάθε φορά τις αντίστοιχες μεθόδους
    από τα περιεχόμενα αντικείμενα.    
    """
    def __init__(self, game, gameOverMode):
        super().__init__(game)
        self.gameOverMode = gameOverMode
        self.time_allowed = 60
        self.endRound = False
        self.background_img = pygame.image.load("mil_game/images/game_bg.png")
        # self.background_img = pygame.transform.scale(self.background_img, self.game.mainscreen.get_size())
        self.player_controller = PlayerController("Player")
        self.player_view = PlayerView(self.player_controller)
        self.question_controller = QuestionController()
        self.time_counter = TimerController(self.time_allowed)
        self.helper_controller = HelpersController()
        self.controllers = None
        self.views = None
        self.setup()

    def setup(self):
        self.question_view = QuestionView(self.question_controller)
        helpers_view = HelpersView(self.helper_controller)
        timer_view = TimerView(self.time_counter)
        self.controllers = [self.question_controller, self.player_controller, self.time_counter, self.helper_controller]
        self.views = [self.player_view, self.question_view, timer_view, helpers_view]

    def set_name(self, name):
        if name:
            self.player_controller.model.name = name
            self.player_view.update_name()


    def onEnter(self):
        self.endRound = False
        self.question_controller.model.set_question()
        print(self.question_controller.model.current_q)
        print("amount pointer ", self.player_controller.model.amount_pointer)
        self.question_view.add_messages()
        self.time_counter.reset()

    def onExit(self):
        self.question_controller.reset()
        


    def update(self, gameTime, event_list):
        """ Γενική συνάρτηση για ενημέρωση όλων των αντικειμένων που αποτελούν το παιχνίδι
        Καλεί τις ξεχωριστές update κάθε αντικειμένου ώστε να ενημερωθούν το καθένα μόνο του
        αν έχει γίνει κάποια αλλαγή.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου. """
        # Ζητάμε από κάθε αντικείμενο που αποτελεί το παρόν mode παιχνιδιού να κάνει τους ελέγχους και τις ενημερώσεις.
        if self.endRound:
            self.game.changeMode(RoundMsgMode(self.game, self))
            self.endRound = False
            return
        
        for manager in self.controllers:
            manager.update(gameTime, event_list)
        
        # Μετά το update ρωτάμε τα αντικείμενα για τις συνθήκες που θέλουμε
        # Παράδειγμα ακολουθεί. Αυτές τις συνθήκες /ελέγχους βέβαια μπορούμε να τις μοιράσουμε 
        # στα αντικείμενά που θέλουμε να ελέγξουμε
        #
      

        # ρωτάμε τα αντικείμενα αν έγινε κάτι, και πράττουμε ανάλογα
        if self.question_controller.show_answers:
            if not self.time_counter.model.is_running:
                self.time_counter.start()

        if self.question_controller.chosen != None:
            self.time_counter.stop()
            if self.question_controller.check_answer():
                self.player_controller.model.amount_pointer += 1
            else:
                self.player_controller.model.lives -= 1
            self.endRound = True

        elif self.time_counter.model.is_over:
            print("time counter isover ", self.time_counter.model.is_over)
            for btn in self.question_controller.q_view.ans_group.sprites():
                if btn.clicked:
                    self.question_controller.chosen = btn

                    print("btn msg", btn.msg)
                    break
            if self.question_controller.chosen != None and self.question_controller.check_answer():
                self.player_controller.model.amount_pointer += 1
            else:
                self.player_controller.model.lives -= 1
            self.endRound = True
        
        if self.helper_controller.done:
            for helper in self.helper_controller.helpers:
                if helper.is_clicked:
                    print(helper.name)

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
        