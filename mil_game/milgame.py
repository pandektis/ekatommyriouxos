import pygame, os, sys
from pygame.locals import *

from player import *
from button import Button
from question import QuestionModel

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
        self.qmodel = QuestionModel()
        self.controllers = None
        self.views = None
        self.time_allowed = 60



    def update(self, gameTime, event_list):
        pass

    def draw(self, surface):
        pass