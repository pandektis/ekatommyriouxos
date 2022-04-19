import os
import pygame
import time
import sys
import math
from pygame.locals import *
import random
from numpy.random import choice
import numpy as np

pygame.init()

SIZE = WIDTH, HEIGHT = 1431, 797
BACKGROUND_COLOR = pygame.Color('black')
FPS = 80

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
timeP = pygame.time

bank = int(1000)
qdata = str("--------------------------")
font = pygame.font.Font(None, 80)
text = 'Fonty'
size = font.size(text)

fg = 250, 250, 250  # font color
bg = 5, 5, 5


question_sys_font = pygame.font.SysFont("Tahoma", 50)
answers_sys_font = pygame.font.SysFont ("Tahoma",30)
bank_sys_font = pygame.font.SysFont ("Arial",30)


background_image = pygame.image.load("img/lobby-2.png").convert()
background_image_blank = pygame.image.load("img/lobby-2.png").convert()
icon = pygame.image.load('img/millionaire_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Millionaire")
pygame.mixer.init()
pygame.mixer.music.load("snd/millionaire_intro.mp3")
pygame.mixer.music.play(0, 0.0)
pygame.mixer.music.set_volume(0.2)







def timerFunc(index):
    index_old = index
    index = index + 1
    return index


def load_images(path):
    """
        Φορτώνει όλες τις εικόνες στον κατάλογο.
    """
    images = []
    images_names = []

    for file_name in os.listdir(path):
        image_name = file_name
        images_names.append(image_name)
    images_names = sorted(images_names)
    print(images_names)

    for file_name in images_names:
        image = pygame.image.load(path + os.sep + file_name).convert()
        images.append(image)
    return images





def draw_player_data(name):
   textSurf = bank_sys_font.render("Ονομα :" + (name), 1, fg)
   textRect = textSurf.get_rect()
   textRect.center = (150, HEIGHT-30)
   screen.blit(textSurf, textRect)




def draw_question(qdata):
    textSurf = question_sys_font.render((qdata), 1, fg)
    textRect = textSurf.get_rect()
    textRect.center = ((WIDTH / 2.4), (HEIGHT / (6.5)))
    screen.blit(textSurf, textRect)

def draw_ansA(ansAdata):
    textSurf = answers_sys_font.render((ansAdata), 1, fg)
    textRect = textSurf.get_rect()
    textRect.center = ((WIDTH / 6.3), (HEIGHT / (1.45)))
    screen.blit(textSurf, textRect)

def draw_ansB(ansBdata):
    textSurf = answers_sys_font.render((ansBdata), 1, fg)
    textRect = textSurf.get_rect()
    textRect.center = ((WIDTH / 1.55), (HEIGHT / (1.45)))
    screen.blit(textSurf, textRect)

def draw_ansC(ansCdata):
    textSurf = answers_sys_font.render((ansCdata), 1, fg)
    textRect = textSurf.get_rect()
    textRect.center = ((WIDTH / 4.8), (HEIGHT / (1.25)))
    screen.blit(textSurf, textRect)

def draw_ansD(ansDdata):
    textSurf = answers_sys_font.render((ansDdata), 1, fg)
    textRect = textSurf.get_rect()
    textRect.center = ((WIDTH / 1.53), (HEIGHT / (1.25)))
    screen.blit(textSurf, textRect)







def main():
    balance = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    running = True
    pygame.display.update()
    global background_image_blank
    global background_image
    name = "KOLOKOTRONIS"
    qdata = "Q11111111111"
    ansAdata = "A111111111"
    ansBdata = "B222222222"
    ansCdata = "C333333333"
    ansDdata = "D444444444"




    while (running):


        screen.blit(background_image_blank, [0, 0])

        draw_question(qdata)
        draw_ansA(ansAdata)
        draw_ansB(ansBdata)
        draw_ansC(ansCdata)
        draw_ansD(ansDdata)

        draw_player_data(name)

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:

                running = False
                pygame.quit()








if __name__ == '__main__':
    main()
