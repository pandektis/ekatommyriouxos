import pygame, os, sys
from pygame.locals import *

from View_ import RadioButton

class Question:
    """Κλάση που διαχειρίζεται την εμφάνιση συμπεριλαμβανομένου του επιπέδου και ενός ακέραιου αριθμού 0-3
    που υποδεικνύει ποια  είναι η σωστή απάντηση"""

    def __init__(self, question, answers):
        #Σκοπός της rstrip(";\n") ειναι να εμφανίζονται η δυσκολία και η σωστή απάντηση δίπλα στην ερώτηση και όχι απο κάτω
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
        # ξέρουμε οτι αυτή ειναι η σωστή απάντηση,επισης κρατάμε και το counter
        for i, ans in enumerate(self.answers):
            if "(*)" in ans:
                #εισαγωγη σωστής απάντησης
                self.correct_answer = i
                #βγαζουμε το *
                ans = ans.split("(*)")
                self.answers[i] = ans[0]
                #Απομονωση δυσκολίας
                ans = ans[1]
                #Εδω ουσιαστικά μέσω τις λίστας απομονόνουμε την δυσκολία και μέτα ψάχνοντας με τη find
                #μολις βρούμε το νούμερο το ονοματίζουμε A B η C
                for level in range(1, 4):
                    if ans.find(str(level)) > 0:
                        self.level = "ABC"[level - 1]




class QuestionModel:

    def __init__(self):
        self.questions = {"A": list(), "B": list(), "C": list()}
        self.currentq = None


    def read_questions(self):
        """Ανάγνωση του αρχείου txt με ερωτήσεις
            Επιστρέφει  λεξικό των ερωτήσεων
            {"A" : κατάλογος ερωτήσεων Α, "B" : κατάλογος ερωτήσεων Β...}"""

    
        with open("Questions.txt", "r", encoding="UTF-8") as file:
            #Διαβάζουμε το αρχείο των ερωτήσεων και το γυρνάμε σαν λίστα
            lines = file.readlines()

            # Διατρέχουμε τη λίστα
            for i in range(len(lines)):

                line = lines[i]
                #Όλες οι ερωτήσεις τελειώνουν με ; οπότε με τη line.rstrip().endswith(";") παίρνουμε μόνο τις ερωτήσεις
                if line.rstrip().endswith(";"):
                #Αν η συνθήκη ειναι true τότε στέλνουμε ως ορίσματα τις ερωτήσεις και τις αντίστοιχες απαντήσεις
                    question = Question(line, [lines[j].rstrip() for j in range(i + 1, i + 5)] )
                    #print(question)

                    #Προσθέτω τη δυσκολία στο τέλος της ερώτησης
                    self.questions[question.level].append(question)

                    i += 5
        
                                    
class QuestionController:
    pass


class QuestionView:
    pass

    def __init__(self):
        pass

    def draw(self, surface):
        pass