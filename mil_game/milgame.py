import pygame, os, sys
from pygame.locals import *

from player import *
from button import Button
from question import *

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
        self.player_controller = PlayerController("New Player")
        self.question_controller = QuestionController()
        self.controllers = None
        self.views = None
        self.time_allowed = 60
        self.setup()

    def setup(self):
        player_view = PlayerScoreView(self.player_controller)
        question_view = QuestionView(self.question_controller)



    def update(self, gameTime, event_list):
        # Ζητάμε από κάθε αντικείμενο που αποτελεί το παρόν mode παιχνιδιού να κάνει τους ελέγχους και τις ενημερώσεις.
        for manager in self.controllers:
            manager.update(gameTime, event_list)
        
        # Μετά το update ρωτάμε τα αντικείμενα για τις συνθήκες που θέλουμε



        if(self.player_controller.model.lives == 0):
            pass #game over

        # Ζητάμε από κάθε View να εμφανίσει αυτά που έχει στην οθόνη
        for painter in self.views:
            painter.draw(self.game.mainscreen)
        

    def draw(self, surface):
        pass