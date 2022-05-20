import pygame, os, sys
from pygame.locals import *

class Player:
    """
    Κρατάει τα δεδομένα του παίκτη.

    Διατηρεί κι ενημερώνει τα ζητούμενα δεδομένα του παίκτη.
    """
    def __init__(self, name = "Player"):
        self.name = name #
        self.lives = 3 # Αριθμός 'ζωών', δλδ πόσα λάθη μπορεί να κάνει.
        self.poso = 0
        self.num_questions = 0
        self.total_time = 0.0
        self.m_o = 0.0
        self.daep = 0.0

    def __str__(self):
        return f"{self.name:^12}|{self.poso:>10}€|{self.total_time:>7} sec|{self.m_o:>7} sec/q|{self.daep:>7}"

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

    def update_stats(self):
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

    def update_name(self):
        self.name_surf = self.view_font.render(self.player.model.name, True, (0,255,0), (255,0,0))
    
    def draw(self, surface):
        surface.blit(self.name_surf, (50,50))
        





    # Για να τρέχει ξεχωριστά το αρχείο, για testing
    if __name__ == "__main__":
        pass