import random
import pygame, os, sys
from pygame.locals import *
from button import *

# from View_ import RadioButton

class Question:
    
    """ Κλάση που αντιπροσωπεύει μία ερώτηση με τις απαντήσεις τις.
        Επισημαίνει και τη σωστή απάντηση.
        Τη θέλουμε μόνο για τα δεδομένα της."""
    
    
    # """Κλάση που διαχειρίζεται την εμφάνιση συμπεριλαμβανομένου του επιπέδου και ενός ακέραιου αριθμού 0-3
    # που υποδεικνύει ποια  είναι η σωστή απάντηση"""

    def __init__(self, question, answers):
        #Σκοπός της rstrip(";\n") ειναι να το κλεισιμο του κενού κάτω απο τιν ερώτηση στα γραφικά
        self.question = question.rstrip(";\n")
        self.answers = answers
        self.data()
    #Μέθοδος εμφάνισης και  σύμπτυξης ερωτήσεων απαντήσεων σωστής απάντησης και δυσκολίας
    def __str__(self):
        text = (self.question + self.level +
                str(self.correct_answer) +
                "\n" + "\n".join(self.answers))

        return (text)

    def data(self):
        """Βρίσκει τη σωστή απάντηση και εξάγει το επίπεδο της ερώτησης."""
        #Με την  enumerate ψάχνουμε  το * στις απαντήσεις οταν το βρούμε
        # ξέρουμε οτι αυτή ειναι η σωστή απάντηση,επισης κρατάμε  counter
        for i, ans in enumerate(self.answers):
            #αν βρεθεί το * στις απαντήσεις
            if "(*)" in ans:
                #εισαγωγη αριθμού σωστής απάντησης
                self.correct_answer = i
                #βγαζουμε το * παιρνουμε καθάρη την απάντηση κάνοντας split την απάντηση απο το επίπεδο δυσκολιας
                ans = ans.split("(*)")
                #το ans[0] είναι η σωστή απάντηση και το ans[1] η δυσκολία
                #εισαγουμε την απάντηση καθαρή έχοντας πια αφαιρέσει το  (*) και το επίπεδο
                self.answers[i] = ans[0]
                #Απομονωση δυσκολίας
                ans = ans[1]
                #Εδω ουσιαστικά πέρνουμε τη δυσκολία και  ψάχνοντας με τη find
                #μολις βρούμε το νούμερο το ονοματίζουμε A B η C και το γυρνάμε στην read_questions
                for level in range(1, 4):
                    if ans.find(str(level)) > 0:
                        self.level = "ABC"[level - 1]



class QuestionModel:

    """ Κλάση που κρατάει λεξικό με όλες τις ερωτήσεις, ανά δυσκολία.
    Η ιδιότητα self.current_q κρατάει την τρέχουσα ερώτηση κάθε φορά.
    """

    def __init__(self):
        """Ανάγνωση του αρχείου txt με ερωτήσεις
        Επιστρέφει  λεξικό που αποτελείτε απο λίστες των ερωτήσεων.
        {"A" : κατάλογος ερωτήσεων Α δυσκολίας, "B" : κατάλογος ερωτήσεων Β δυσκολίας...}"""
        #αρχικοποίηση λεξικού
        self.questions = {"A": list(), "B": list(), "C": list()}
        self.curent_level = "A"
        self.current_q = None
        #εισάγουμε το txt
        with open("Questions.txt", "r", encoding="UTF-8") as file:
            #Διαβάζουμε το αρχείο των ερωτήσεων και το γυρνάμε σαν λίστα
            lines = file.readlines()
            # Διατρέχουμε τη λίστα
            for i in range(len(lines)):
                #γραμμή γραμμή
                line = lines[i]
                #Όλες οι ερωτήσεις τελειώνουν με ; οπότε με τη line.rstrip().endswith(";")  ξέρουμε οτι ξεκινάει μια ερώτηση και οι απαντήσεις της.
                if line.rstrip().endswith(";"):
                #Αν η συνθήκη ειναι true τότε στέλνουμε ως ορίσματα στην κλάση question τις ερωτήσεις και τις αντίστοιχες απαντήσεις
                    question = Question(line, [lines[j].rstrip() for j in range(i + 1, i + 5)] )
                    #Προσθέτω στο την ερώτηση στην ανάλογη δυσκολία που παίρνω απο την κλαση question με την questions_level και κάνουμε append
                    #την ερώτηση με τις απαντήσεις στο αντίστοιχο level
                    self.questions[question.level].append(question)
                    #στο επόμενο σετ ερωτήσεων-απαντήσεων
                    i += 5
        w, h = 380, 65
        top_row_y = 465
        bottom_row_y = 545
        left_col_x = 130
        right_col_x = 605
        self.q_rect = pygame.Rect(130,35,840,130)
        self.ansA_rect = pygame.Rect(left_col_x, top_row_y, w, h)
        self.ansB_rect = pygame.Rect(right_col_x, top_row_y, w, h)
        self.ansC_rect = pygame.Rect(left_col_x, bottom_row_y, w, h)
        self.ansD_rect = pygame.Rect(right_col_x, bottom_row_y, w, h)

    def set_question(self):
        if self.questions[self.curent_level]:
            question_number = random.randint(0, len(self.questions[self.curent_level])-1)
            self.current_q = self.questions[self.curent_level].pop(question_number)
        else:
            print("No more questions in list... start new game")
                                    
    def unset_question(self):
        self.current_q = None


class QuestionController:
    """ Κλάση που εκτελέι τους ελέγχους και ενημερώνει την QuestionModel
        Έχει μέθοδο update() που μέσα γίνονται οι έλεγχοι για το κλικ, και αντίστοιχα
        (Η update() τρέχει σε κάθε frame του game loop, είναι σα να είχαμε κώδικα μέσα στο while του gameloop)
    """
    def __init__(self):
        self.model = QuestionModel() # φόρτωμα των ερωτήσεων.
        self.delay = 2500
        self.show_answers = False
        self.chosen = None
    
    def set_view(self, view):
        self.q_view = view


    def reset(self):
        self.delay = 2500
        self.show_answers = False
        self.chosen = None
        self.q_view.remove_messages()
        self.q_view.question_btn.setup()
        for a in self.q_view.ans_group.sprites():
            a.setup()
            a.clicked = False

    def check_answer(self):
        return self.chosen.msg == self.model.current_q.answers[self.model.current_q.correct_answer]

    def take_help_action(self, name):
        if name == 'fifty':
            # λιστα με τα νούμερα των πιθανών απαντήσεων
            ans_list = [ans for ans in self.q_view.ans_group.sprites() if
                        ans != self.model.current_q.answers[self.model.current_q.correct_answer]]

            # ans.remove(εδώ θα μπει το νουμερο της σωστης απάντησης αφου εμφανιστει στο πρόγραμμα)

            ans_list.remove(random.choice(ans_list))
            ans_list.remove(random.choice(ans_list))
            for a in ans_list:
                a.remove(self.q_view.ans_group)

            # Εδώ ελέγχεις τι θες να κάνεις με αυτες που έμειναν
            # η της κάνεις κοκκίνες η .remove

            print("the name is", name)

        elif name == 'computer':
            ans = [0, 1, 2, 3]

            #ans.remove(εδώ θα μπει το νουμερο της σωστης απάντησης αφου εμφανιστει στο πρόγραμμα)

            for i in ans:
            # η της κάνεις κοκκίνες η .remove

            
                print("the name is", name)
        elif name == 'other':

            #απλα ξανακαλεις μια ερώτηση απο όπου την καλείς?
            #και την αφαιρείς απο όπου τις κρατάς να μην επιρεαστεί η κλιμακωτή δυσκολία?


            print("the name is", name)


    def update(self, gameTime, event_list):
        if self.delay > 0:
            self.delay -= gameTime
            return
        self.show_answers = True
        pos = pygame.mouse.get_pos()
        self.q_view.ans_group.update(event_list, pos)
        for ans_btn in self.q_view.ans_group.sprites():
            if ans_btn.chosen:
                self.chosen = ans_btn



class QuestionView:
    """ Κλάση υπεύθυνη για την εμφάνιση της τρέχουσας ερώτησης και απαντήσεων.
        Εδώ μπαίνει όλος ο κώδικας για τη δημιουργία και την εμφάνιση των buttons που εμφανίζουν
        την ερώτηση και τις απαντήσεις. Ο έλεγχος για το"""
    

    def __init__(self, q_controller):
        self.q_controller = q_controller # Ο αντίστοιχος controller, για να παίρνουμε τα στοιχεία και να του δώσουμε αναφορά στα buttons να ελέγχει. 
        # self.rect = pygame.Rect(240, 30, 800, 670)
        self.text_font = pygame.font.Font(None, 30)
        self.ans_group = pygame.sprite.Group()
        self.question_btn = QAButton([], self.q_controller.model.q_rect)
        self.ansA_btn = QAButton(self.ans_group, self.q_controller.model.ansA_rect)
        self.ansB_btn = QAButton(self.ans_group, self.q_controller.model.ansB_rect)
        self.ansC_btn = QAButton(self.ans_group, self.q_controller.model.ansC_rect)
        self.ansD_btn = QAButton(self.ans_group, self.q_controller.model.ansD_rect)

        ans_buttons = self.ans_group.sprites()
        for ans in ans_buttons:
            ans.setRadioButtons(ans_buttons)
        self.q_controller.set_view(self)
        
    def add_messages(self):
        self.question_btn.add_text(pygame.font.Font(None, 40), self.q_controller.model.current_q.question,(60,128,156))
        # Τυχαία σειρά εμφάνισης, για να μην είναι ίδια κάθε φορά.
        answers = random.sample(self.q_controller.model.current_q.answers, 4)
        for i, btn in enumerate(self.ans_group.sprites()):
            btn.add_text(pygame.font.Font(None, 30), answers[i], (60, 28, 156))
    
    def remove_messages(self):
        self.question_btn.setup()
        for btn in self.ans_group.sprites():
            btn.setup()

    def draw(self, surface):
        """ Εμφάνιση της ερώτησης και των απαντήσεων"""
        surface.blit(self.question_btn.image, self.q_controller.model.q_rect)
        if self.q_controller.show_answers:
            self.ans_group.draw(surface)
        
