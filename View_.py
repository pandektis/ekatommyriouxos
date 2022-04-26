import pygame
import math
from tkinter import simpledialog
from Kost_Agr import Game

#######################################################################################################################
class RadioButton(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, font, text):
        super().__init__()
        text_surf = font.render(text, True, (196, 196, 196))
        self.button_image = pygame.Surface((w, h))
        self.button_image.fill((0, 0, 0))
        self.button_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        self.hover_image = pygame.Surface((w, h))
        self.hover_image.fill((96, 96, 96))
        self.hover_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        pygame.draw.rect(self.hover_image, (196, 196, 196), self.hover_image.get_rect(), 3)
        self.clicked_image = pygame.Surface((w, h))
        self.clicked_image.fill((96, 196, 96))
        self.clicked_image.blit(text_surf, text_surf.get_rect(center=(w // 2, h // 2)))
        self.image = self.button_image
        self.rect = pygame.Rect(x, y, w, h)
        self.clicked = False
        self.buttons = None

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list):
        hover = self.rect.collidepoint(pygame.mouse.get_pos())
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover and event.button == 1:
                    for rb in self.buttons:
                        rb.clicked = False
                    self.clicked = True

        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image

#######################################################################################################################
def viewQ():
    global correct_answer , ansAdata , ansBdata , ansCdata , ansDdata , ansEdata , q , qdata

    newGame = Game()
    GetQuestion = newGame.get_question()
    qdata =  GetQuestion.question.split('.')[1].lstrip()


    ansAdata = GetQuestion.answers[0].split('.')[1].lstrip()
    ansBdata = GetQuestion.answers[1].split('.')[1].lstrip()
    ansCdata = GetQuestion.answers[2].split('.')[1].lstrip()
    ansDdata = GetQuestion.answers[3].split('.')[1].lstrip()

    correct_answer = GetQuestion.correct_answer
    if correct_answer == 0:
        correct_answer = ansAdata
    elif correct_answer == 1:
        correct_answer = ansBdata
    elif correct_answer == 2:
        correct_answer = ansCdata
    elif correct_answer == 3:
        correct_answer = ansDdata

    print(correct_answer)

#######################################################################################################################
def check_answer(lvl,answer):
    balance = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    inputname = "BLABLAS"




    if (correct_answer == answer):


        if (lvl == 14):
            print("14")
        else:
            print("\nΣωστή απάντηση  %s τώρα έχεις $%s πάμε στην ερώτηση νούμερο #%s!  " % (inputname, balance[lvl + 1], lvl + 2))
            #correctButton()
            #viewQ()
            check_answer(answer,lvl + 1)

    else:
        print("\n Λαθος η σωστη ειναι  %s." % correct_answer)

        main()



#######################################################################################################################

#######################################################################################################################
def drawArc(surf, color, center, radius, width, end_angle):
    arc_rect = pygame.Rect(0, 0, radius*2, radius*2)
    arc_rect.center = center
    pygame.draw.arc(surf, color, arc_rect, 0, end_angle, width)
#######################################################################################################################


pygame.init()

SIZE = WIDTH, HEIGHT = 1431, 797
BACKGROUND_COLOR = pygame.Color('black')
FPS = 80
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
timer_event = pygame.USEREVENT+1
pygame.time.set_timer(timer_event, 1000)
fg = 250, 250, 250
bg = 5, 5, 5
font50 = pygame.font.SysFont("Tahoma", 25)
fontClock = pygame.font.SysFont(None, 100)
question_sys_font = pygame.font.SysFont("Tahoma", 25)

background_image = pygame.image.load("img/lobby-2.png").convert()
icon = pygame.image.load('img/millionaire_logo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Millionaire")
counter = 60



################################StartUpMixSound#######################################################################

pygame.mixer.init()
pygame.mixer.music.load("snd/millionaire_intro.mp3")
pygame.mixer.music.play(0, 0.0)
pygame.mixer.music.set_volume(0.2)

#####################################################################################################################

def main():

    viewQ()
    counter = 60
    text = question_sys_font.render(str(counter), True, (0, 128, 0))

    radioButtons = [
        ###########(Mikos,Ypsos,Platos,Megethos)####################
        RadioButton(141, 522, 440, 60, font50, ansAdata),
        RadioButton(678, 522, 440, 60, font50, ansBdata),
        RadioButton(141, 615, 440, 60, font50, ansCdata),
        RadioButton(678, 615, 440, 60, font50, ansDdata)
    ]


    for rb in radioButtons:
        rb.setRadioButtons(radioButtons)



    group = pygame.sprite.Group(radioButtons)
    pygame.display.update()


    run = True
    while run:
        clock.tick(60)

        event_list = pygame.event.get()
        for event in event_list:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("PRESS A")
                    print("Response Time :", counter)
                    answer = ansAdata
                    check_answer(0, answer)
                if event.key == pygame.K_b:
                    print("PRESS B")
                    print("Response Time :", counter)
                    answer = ansBdata
                    check_answer(0, answer)
                if event.key == pygame.K_c:
                    print("PRESS C")
                    print("Response Time :", counter)
                    answer = ansCdata
                    check_answer(0, answer)
                if event.key == pygame.K_d:
                    print("PRESS D")
                    print("Response Time :", counter)
                    answer = ansDdata
                    check_answer(0, answer)
                if event.key == pygame.K_5:
                    print("PRESS 5")
                if event.key == pygame.K_SPACE:
                    running = False
                if event.type == pygame.K_q:
                    print("PRESS Q")
                    pygame.quit();

            elif  radioButtons[0].clicked == True:
                print("CLICK A")
                print("Response Time :", counter)
                answer = ansAdata
                check_answer(0, answer)
            elif radioButtons[1].clicked == True:
                print("CLICK B")
                print("Response Time :", counter)
                answer = ansBdata
                check_answer(0, answer)
            elif radioButtons[2].clicked == True:
                print("CLICK C")
                print("Response Time :", counter)
                answer = ansCdata
                check_answer(0, answer)
            elif radioButtons[3].clicked == True:
                print("CLICK D")
                print("Response Time :", counter)
                answer = ansDdata
                check_answer(0, answer)


            elif event.type == timer_event:
                counter -= 1
                text = fontClock.render(str(counter), True, (0, 220, 0))
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)

                    main()





        group.update(event_list)
        screen.blit(background_image, [0, 0])
        #screen.fill(0)

        text_rect = text.get_rect()
        text_rect.center = ((WIDTH / 2.31), (HEIGHT / (2.2)))
        screen.blit(text, text_rect)
        drawArc(screen, (0, 250, 0), (615, 360), 115, 10, 2 * math.pi * counter / 100)

        group.draw(screen)
        textSurf = question_sys_font.render((qdata), 1, fg)
        textRect = textSurf.get_rect()
        textRect.center = ((WIDTH / 2.4), (HEIGHT / (6.5)))
        screen.blit(textSurf, textRect)
        pygame.display.flip()
        #pygame.display.update()


    pygame.quit()
    exit()

if __name__ == '__main__':
    main()