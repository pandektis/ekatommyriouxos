from cmath import pi
import os
import pygame
import tkinter as tk
from tkinter import simpledialog
import time
import sys
import math
from pygame.locals import *
import random
from numpy.random import choice
import numpy as np
#import midb
from tkinter import ttk

from pyparsing import White


class View:
    """
    Κλάση για την εμφάνιση της εφαρμογής.

    Υπεύθυνη να εμφανίζει τα δεδομένα στον παίκτη και να
    δέχεται είσοδο από τον παίκτη, την οποία περνάει στον Controller.

    """

    def __init__(self, width, height):
        self._SIZE = width, height
        self._BG_COLOR = pygame.Color('black')
        self._FPS = 1
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        #self.timeP = pygame.time
        self.background_image = pygame.image.load("img/lobby-2.png").convert()
        self.background_image_blank = pygame.image.load("img/millionaire_logo_full.png").convert()
        self.c = None
        self.arect = Rect(self._SIZE[0] / 2 - 25, self._SIZE[1]/2 -25,50,50 ) 
        self.subs = self.screen.subsurface(self.arect)

    def set_controller(self, controller):
        """
        Σύνδεση με τον Controller

        Ορίζουμε ως attribute της κλάσης τον Controller
        ώστε να καλούμε μεθόδους σ' αυτόν και να του περνάμε
        την είσοδο του παίκτη.
        """
        self.c = controller
        
    def askName(self):
#        self.screen.blit(self.background_image_blank, [0, 0])
        
        name = simpledialog.askstring(title="Millionaire",
                                        prompt="Καλώς ήρθες , εισήγαγε το όνομα σου για να συνεχίσεις :")
       
        self.screen = pygame.display.set_mode((800,600))
        self._SIZE = self.screen.get_size()
        self.screen.blit(pygame.transform.scale(self.background_image_blank, self._SIZE),(0,0))
        
        pygame.display.flip()
        return name

    def draw_start(self):

        splash = pygame.display.set_mode((512, 512), pygame.NOFRAME )
        pygame.mixer.music.load("snd/millionaire_intro.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(0, 0.0)
        
        
        splash.blit(pygame.transform.scale(self.background_image_blank, splash.get_size()),(0,0))
        pygame.display.update()
        while pygame.mixer.music.get_busy():
            
            pass
        pygame.display.quit()
        # print(pygame.display.get_active())
        # print(pygame.display.get_surface())
        # print(pygame.display.get_desktop_sizes())
        
    def arc_draw(self, surface, stop):
        
               
        self.subs.fill((0,0,0))
        pygame.draw.arc(self.subs,(255,255,255), self.subs.get_rect().inflate(-5,-5), 0, stop)

    def draw_qans(self,surface, qans):
        pass
    
       

if __name__ == '__main__':
    v = View(640,480)
    tt = 60
    stop = 2*pi
    pygame.init()
    v.draw_start()
    # while(tt >= 0):
    #     pygame.event.pump()
    #     v.arc_draw(v.subs, stop)
    #     v.update()
    #     stop -= 2*pi/60

    #     tt -= 1
    #     print(stop, tt)
    #     v.clock.tick(1)
    #     print(v.clock.get_time())
        
    # name = v.askName()
    # print(name)
    # name = v.askName()