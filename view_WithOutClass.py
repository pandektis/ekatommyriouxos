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
import midb


pygame.init()

SIZE = WIDTH, HEIGHT = 1431, 797
BACKGROUND_COLOR = pygame.Color('black')
FPS = 80

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
timeP = pygame.time


qdata = str("--------------------------")
font = pygame.font.Font(None, 80)
text = 'Fonty'
size = font.size(text)

fg = 250, 250, 250
bg = 5, 5, 5

question_sys_font = pygame.font.SysFont("Tahoma", 25)
answers_sys_font = pygame.font.SysFont ("Tahoma",20)
bank_sys_font = pygame.font.SysFont ("Arial",30)
font50_sys_font = pygame.font.SysFont(None, 50)
cd_sys_font = pygame.font.SysFont(None, 100)


background_image = pygame.image.load("img/lobby-2.png").convert()
background_image_blank = pygame.image.load("img/millionaire_logo_full.png").convert()
icon = pygame.image.load('img/millionaire_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Millionaire")
pygame.mixer.init()
pygame.mixer.music.load("snd/millionaire_intro.mp3")
pygame.mixer.music.play(0, 0.0)
pygame.mixer.music.set_volume(0.2)



def countdown():
    counter = 60
    text = cd_sys_font.render(str(counter), True, (0, 128, 0))

    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == timer_event:
                counter -= 1
                text = cd_sys_font.render(str(counter), True, (0, 128, 0))
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)

        screen.fill((255, 255, 255))
        text_rect = text.get_rect(center=screen.get_rect().center)
        screen.blit(text, text_rect)
        #pygame.display.flip()


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

def askName():
    global inputname

    screen.blit(background_image_blank, [0, 0])
    pygame.display.update()
    inputname = simpledialog.askstring(title="Millionaire",
                                      prompt="Καλώς ήρθες , εισήγαγε το όνομα σου για να συνεχίσεις :")
    name = inputname
    main()

def viewQ():
    global correct_answer , ansAdata , ansBdata , ansCdata , ansDdata , ansEdata , q , qdata
    qnum = int(random.random() * 10)
    q = midb.get_question(0, qnum)
    qdata = (q[0])
    ansAdata = (q[1])
    ansBdata = (q[2])
    ansCdata = (q[3])
    ansDdata = (q[4])
    draw_question(qdata)
    draw_ansA(ansAdata)
    draw_ansB(ansBdata)
    draw_ansC(ansCdata)
    draw_ansD(ansDdata)
    correct_answer = q[5]
    print(correct_answer)



def check_answer(lvl,answer):
    balance = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]



    if (correct_answer == answer):

        if (lvl == 14):
            print("EFTASES TIS 15 EROTISIS BRAVO")
        else:
            print("\nΣωστή απάντηση  %s τώρα έχεις $%s πάμε στην ερώτηση νούμερο #%s!  " % (inputname, balance[lvl + 1], lvl + 2))

            #viewQ()
            #check_answer(answer,lvl + 1)

    else:
        print("\n lathos h sosti einai  %s." % correct_answer)
        main()

#------------------------------------------------------MainProgram-------------------------------------------------
def main():



    pygame.display.update()



    running = True
    screen.blit(background_image, [0, 0])
    viewQ()



    while (running):


        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("PRESS A")
                    answer = ansAdata
                    check_answer(0,answer)
                if event.key == pygame.K_b:
                    print("PRESS B")
                    answer = ansBdata
                    check_answer(0,answer)
                if event.key == pygame.K_c:
                    print("PRESS C")
                    answer = ansCdata
                    check_answer(0,answer)
                if event.key == pygame.K_d:
                    print("PRESS D")
                    answer = ansDdata
                    check_answer(0, answer)
                if event.key == pygame.K_5:
                    print("PRESS 5")
                if event.key == pygame.K_SPACE:
                    running = False
                    main()
                if event.type == pygame.K_q:
                    print("PRESS Q")
                    pygame.quit();
                    #sys.exit();



        pygame.display.update()









if __name__ == '__main__':
    askName()





