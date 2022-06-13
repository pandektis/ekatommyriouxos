import pygame, os, sys
from pygame.locals import *
from button import *

class Player:
    """
    Κρατάει τα δεδομένα του παίκτη.

    Διατηρεί κι ενημερώνει τα ζητούμενα δεδομένα του παίκτη.
    """
    def __init__(self, name = "Player"):
        self.name = name #
        self.lives = 3 # Αριθμός 'ζωών', δλδ πόσα λάθη μπορεί να κάνει.
        self.possible_earnings = (100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 25000, 50000, 100000, 250000, 500000, 1000000)
        self.amount_pointer = -1
        self.poso = 0
        self.num_questions = 0
        self.total_time = 0.0
        self.m_o = 0.0
        self.daep = 0.0

    def __str__(self):
        return f"{self.name:^12}|{self.poso:>10}€|{self.total_time:>7.1f} sec|{self.m_o:>7.2f} sec/q|{self.daep:>7.4f}"

    def _calc_mo(self):
        """ Υπολογισμός Μ.Ο. χρόνου ανά ερώτηση"""
        try:
            self.m_o = self.total_time / self.num_questions
        except ZeroDivisionError as Z:
            self.m_o = 0.0

    def _calc_daep(self):
        """Υπολογισμός Δείκτη Αξιολόγησης Επίδοσης Παίκτη"""
        try:
            self.daep = self.poso / self.total_time
        except ZeroDivisionError as Z:
            self.daep = 0.0

    def update_stats(self, time_elapsed):
        if self.amount_pointer >= 0 and self.amount_pointer <= 14:
            self.poso = self.possible_earnings[self.amount_pointer]
        else:
            self.poso = 0
        self.total_time += time_elapsed
        self._calc_mo()
        self._calc_daep()



class PlayerController:
    """ Αυτή η κλάση δεν ξέρω αν χρειάζεται, αφού δεν ελέγχουμε κάτι στον παίκτη
        Θέλουμε μόνο τα δεδομένα του, που τα κρατάμε στην κλάση Player
        Προς διερεύνηση, να δούμε μήπως χρειαστεί."""
    def __init__(self, name):
        self.model = Player(name)

    def update(self, gameTime, event_list):
        pass

class PlayerView:
    """ Κλάση υπεύθυνη για την εμφάνιση των στοιχείων του παίκτη.
    
        Εδώ φτιάχνουμε τη μορφή εμφάνισης του παίκτη (buttons ή όπως αλλιώς)
        Τα στοιχεία τα παίρνει από αντικείμενο Player, που το έχει ως αναφορά
        π.χ. self.player.poso, self.player.name
        Παρόμοιας λογικής με όλες τις υπόλοιοπες view
        
        Περιέχει μέθοδο draw() για την εμφάνιση, η οποία θα καλείται σε κάθε
        frame μέσω του gameMode
        """
    def __init__(self, player_ctrl):
        self.player = player_ctrl
        self.view_font = pygame.font.Font(None, 36)
        self.name_surf = self.view_font.render(self.player.model.name, True, (0,255,0), (255,0,0))
        self.a_left = 1100
        self.a_right = 1245
        self.a_y = 560
        self.a_hor_offset = 10
        self.a_vert_offset = 15
        
        
        
        
    def update_name(self):
        """
        Μέθοδος για ενημέρωση του ονόματος του παίκτη
        """
        self.name_surf = self.view_font.render(self.player.model.name, True, (0,255,0), (0,0,0))
        self.name_surf.set_colorkey((0,0,0,))
    
    def draw(self, surface):
        """
        Μέθοδος εμφάνισης των στοιχείων του παίκτη κατά τη διάρκεια του παιχνιδιού.
        """
        x , z = self.a_left, self.a_right
        a, b = self.a_hor_offset, self.a_vert_offset
        surface.blit(self.name_surf, (150,250))
        for i in range(len(self.player.model.possible_earnings)):
            if i <= self.player.model.amount_pointer:
                y = self.a_y - (2*b + 2) * i
                coords = [(x, y), (x+a, y - b), (z - a, y - b), (z, y), (z - a, y +b), (x + a, y + b),(x,y)]
                pygame.draw.polygon(surface, 'yellow',coords, 1)

   