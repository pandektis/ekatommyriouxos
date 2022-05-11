import pygame, os, sys
from pygame.locals import *

from player import *
from button import Button
from question import QuestionModel

class GameMode:

    def __init__(self, game, gameOverMode):
        self.game = game
        self.gameOverMode = gameOverMode
        self.qmodel = QuestionModel()
        self.controllers = None
        self.views = None
        self.time_allowed = 60