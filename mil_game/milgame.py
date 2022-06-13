import pygame, os, sys
from pygame.locals import *

from game import *
from player import *
from button import Button
from question import *
from game_timer import *
from helpers import *

class RoundMsgMode(BaseMode):
    """
    Κλάση για την εμφάνιση μηνύματος στο τέλος κάθε γύρου
    Μεταβαίνουμε σ' αυτή μετά από κάθε γύρο, και επιστρέφουμε στο παιχνίδι (GameMode) μετά
    Εκτός από το τέλος του παιχνιδιού, όπου μετά μεταφερόμαστε στα high scores
    """

    def __init__(self, game, next_mode, msg = "Επόμενη ερώτηση" ) -> None:
        super().__init__(game)
        self.next_mode = next_mode
        self.delay = 3000
        self.msg = msg
        self.base_rect = pygame.Rect(130,35,840,130)
        self.base_surf = pygame.Surface(self.base_rect.size)
        self.base_surf.fill(0)
        self.overlay = pygame.Surface(self.game.mainscreen.get_size())
        self.overlay.set_alpha(150)
        self.overlay.fill((0,0,0))
        msg_font = pygame.font.Font(None, 60)
        self.msg_surf = pygame.font.Font.render(msg_font,msg,True, (255,0,0), (0,0,0))
        self.msg_surf.set_colorkey((0,0,0))
        self.msg_rect = self.msg_surf.get_rect()
        self.msg_rect.midbottom = self.base_rect.midbottom

    def set_msg(self, msg):
        self.msg_surf = pygame.font.Font.render(None,msg,True, (255,0,0), (0,0,0))
        self.msg_surf.set_colorkey((0,0,0))
        

    def update(self, gameTime, event_list):
        if self.delay <= 0:
            self.game.changeMode(self.next_mode)
            self.delay = 3000
        self.delay -= gameTime
        self.msg_rect.bottom -= 1

    def onExit(self):
        self.msg_rect.midbottom = self.base_rect.midbottom



    def draw(self, surface):
        # surface.blit(self.overlay, (0,0))
        surface.blit(self.base_surf, self.base_rect)
        surface.blit(self.msg_surf, self.msg_rect)
        



class GameMode(BaseMode):
    """
    Κατάσταση παιχνιδιού Παιχνίδι.

    Περιέχει τα αντικείμενα που χρειάζονται για να παιχτεί το παιχνίδι
    (player, question, timer, κ.α.)
    Οι μεθόδοι update και draw καλούν κάθε φορά τις αντίστοιχες μεθόδους
    από τα περιεχόμενα αντικείμενα.    
    """
    def __init__(self, game, gameOverMode):
        """
        Αρχικοποίηση μεταβλητών που χρειάζεται η κλάση καθώς και δημιουργία αντικειμένων
        (player, timer, question, κτλ ) που χρειάζεται το παιχνίδι.
        """
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
        self.endRoundMode = RoundMsgMode(self.game, self)
        self.question_view = QuestionView(self.question_controller)
        helpers_view = HelpersView(self.helper_controller)
        timer_view = TimerView(self.time_counter)
        self.controllers = [self.question_controller, self.player_controller, self.time_counter, self.helper_controller]
        self.views = [self.player_view, self.question_view, timer_view, helpers_view]

    def set_name(self, name):
        """
        Μέθοδος για να ορίσουμε το όνομα του παίκτη
        καλείται από την κατάσταση InputMode
        """
        if name:
            self.player_controller.model.name = name
            self.player_view.update_name()

    def reset_all(self):
        """
        Μέθοδος για επαναφορά δεδομένων ερώτησης και βοήθειας
        """
        self.question_controller.reset()
        self.helper_controller.done = False

    def onEnter(self, oldMode):
        """
        Μέθοδος που εκτελείται κατά την είσοδο στην κατάσταση
        Κατεβάζουμε τη σημαία για το τέλος του γύρου
        ελέγχουμε/θέτουμε το επίπεδο ερώτησης
        παίρνουμε νέα ερώτηση
        και επαναφέρουμε το χρονόμετρο
        """
        self.endRound = False
        if self.player_controller.model.amount_pointer == 4:
            self.question_controller.model.curent_level = "B"
        elif self.player_controller.model.amount_pointer == 9:
            self.question_controller.model.curent_level = "C"
        
        self.question_controller.model.set_question()
        print(self.question_controller.model.current_q)
        print("amount pointer ", self.player_controller.model.amount_pointer, "Current level", self.question_controller.model.curent_level)
        self.question_view.add_messages()
        self.time_counter.reset()

    def onExit(self):
        """
        Μέθοδος που εκτελείται κατά την έξοδο από την κατάσταση
        επαναφέρουμε την ερώτηση (σβήνουμε δλδ αυτήν που μόλις έπαιξε)
        """
        self.question_controller.reset()
        


    def update(self, gameTime, event_list):
        """ Γενική συνάρτηση για ενημέρωση όλων των αντικειμένων που αποτελούν το παιχνίδι
        Καλεί τις ξεχωριστές update κάθε αντικειμένου ώστε να ενημερωθεί το καθένα μόνο του
        Ελέγχει αν έχει γίνει κάποια αλλαγή.
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου, μέσα στη run() της 'μηχανής' δηλαδή, 30 φορές το δευτερόλεπτο """

        # Ελέγχουμε αν έχει τεθεί η σημαία για το τέλος του γύρου, και πράττουμε ανάλογα.
        if self.endRound:
            self.game.changeMode(self.endRoundMode)
            self.endRound = False
            # self.question_controller.reset()
            self.reset_all()
            return

        # Ζητάμε από κάθε αντικείμενο που αποτελεί το παρόν mode παιχνιδιού να κάνει τους ελέγχους και τις ενημερώσεις.
        # Καλούμε την update() κάθε αντικειμένου controller (playerController, questionController, κτλ)
        # Κάθε αντικείμενο με τη σειρά του κάνει τους ελέγχους/ενέργειες που χρειάζεται και μεταβάλλει την κατάστασή του
        # (θέτει μεταβλητές, ενημερώνει στοιχεία, κτλ).
        for manager in self.controllers:
            manager.update(gameTime, event_list)
        
        # Μετά το update ρωτάμε τα αντικείμενα για τις συνθήκες που θέλουμε
        # Αυτές τις συνθήκες /ελέγχους βέβαια μπορούμε να τις μοιράσουμε 
        # στα αντικείμενά που θέλουμε να ελέγξουμε
        #
      

        #### ρωτάμε τα αντικείμενα αν έγινε κάτι, και πράττουμε ανάλογα

        # Ξεκινάμε τον timer μόλις εμφανιστούν οι απαντήσεις
        if self.question_controller.show_answers:
            if not self.time_counter.model.is_running:
                self.time_counter.start()

        # Συνθήκη για επιλογή απάντησης: Αν έχει επιλέξει ο χρήστης
        if self.question_controller.chosen != None:
            self.time_counter.stop() # Σταματάμε το χρόνο
            if self.question_controller.check_answer():
                # Αν είναι σωστή, αυξάνουμε το δείκτη του ποσού
                self.player_controller.model.amount_pointer += 1
            else:
                # Αλλιώς μειώνουμε τις 'ζωές'
                self.player_controller.model.lives -= 1
            # Είτε σωστή είτε όχι, αυξάνουμε τον αριθμό των ερωτήσεων, ενημερώνουμε σημαία για τέλος γύρου
            # και ανανεώνουμε στατιστικά και ερωτήσεις
            self.player_controller.model.num_questions += 1
            self.player_controller.model.update_stats(self.time_allowed - self.time_counter.model.counter)
            self.endRound = True
            self.question_controller.reset()

        # Συνθήκη για τέλος χρόνου
        elif self.time_counter.model.is_over:
            #print("time counter isover ", self.time_counter.model.is_over)
            ## Ελέγχουμε αν έχει επιλεγεί κάποια απάντηση και δεν έχει υποβληθεί οπότε την λαμβάνουμε ώς υποβληθείσα
            for btn in self.question_controller.q_view.ans_group.sprites():
                if btn.clicked:
                    self.question_controller.chosen = btn
                    print("btn msg", btn.msg)
                    break

            # if self.question_controller.chosen != None and self.question_controller.check_answer():
            #     self.player_controller.model.amount_pointer += 1
            # Αν δεν υπάρχει κάποια επιλεγμένη, χάσαμε την τρέχουσα ερώτηση. Αν υπάρχει, θα πιαστεί στο 
            # από πάνω if στην επόμενη επανάληψη
            if self.question_controller.chosen == None:
                self.player_controller.model.lives -= 1
                self.player_controller.model.num_questions += 1
                self.player_controller.model.update_stats(self.time_allowed - self.time_counter.model.counter)
                self.endRound = True
        
        # Συνθήκη για επιλογή βοήθειας
        elif self.helper_controller.done and self.helper_controller.current_helper != None:
            self.question_controller.take_help_action(self.helper_controller.current_helper.name)
            self.helper_controller.current_helper = None
        
        # Συνολική συνθήκη για τέλος παιχνιδιού.
        if self.player_controller.model.lives == 0 or self.player_controller.model.amount_pointer == 14:
            if self.player_controller.model.lives == 0:
                # έλεγχος για τα 'μαξιλαράκια'
                if self.player_controller.model.amount_pointer >= 9:
                    self.player_controller.model.amount_pointer = 9
                elif self.player_controller.model.amount_pointer >= 4:
                    self.player_controller.model.amount_pointer = 4
                else:
                    self.player_controller.model.amount_pointer = 0
            # ενημέρωση στατιστικών του παίκτη
            self.player_controller.model.update_stats(0)
            # gameOverMode είναι τα high scores, περνάμε τον τρέχων παίκτη 
            self.gameOverMode.curr_player = self.player_controller.model
            # Δημιουργούμε αντικείμενο για το τέλος του γύρου, με μετάβαση στο gameOverMode
            self.endRoundMode = RoundMsgMode(self.game,self.gameOverMode, "€"+str(self.player_controller.model.poso))



    def draw(self, surface):
        """Συνάρτηση για την εμφάνιση της οθόνης του παιχνιδιού
        Εμφανίζουμε το background και ότι άλλο σταθερό ανήκει στο παιχνίδι
        και μετά καλούμε την draw κάθε υπεύθυνου αντικειμένου για να εμφανίσει κι αυτό τα δικά του και 
        να ολοκληρωθεί η εικόνα (frame)
        Τρέχει σε κάθε επανάληψη του κυρίως βρόχου, μέσα στη run() της 'μηχανής' δηλαδή, 30 φορές το δευτερόλεπτο 
        """
        ### Κώδικας για background και ό,τι άλλο δεν ανήκει σε κάποιο άλλο αντικείμενο
        surface.blit(self.background_img, (0,0))

        # Ζητάμε από κάθε αντικείμενο View (playerView, questionView, κτλ) να εμφανίσει αυτά που έχει στην οθόνη
        for painter in self.views:
            painter.draw(surface)
        