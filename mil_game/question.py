import pygame, os, sys
from pygame.locals import *

from View_ import RadioButton

class Question:
    """Κλάση που διαχειρίζεται την εμφάνιση συμπεριλαμβανομένου του επιπέδου και ενός ακέραιου αριθμού 0-3
    που υποδεικνύει ποια  είναι η σωστή απάντηση"""

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

    """Ανάγνωση του αρχείου txt με ερωτήσεις
    Επιστρέφει  λεξικό που αποτελείτε απο λίστες των ερωτήσεων.
     {"A" : κατάλογος ερωτήσεων Α δυσκολίας, "B" : κατάλογος ερωτήσεων Β δυσκολίας...}"""
    #αρχικοποίηση λεξικού
    questions = {"A": list(), "B": list(), "C": list()}
    #εισάγουμε το txt
    with open("Questions.txt", "r", encoding="UTF-8") as file:
        #Διαβάζουμε το αρχείο των ερωτήσεων και το γυρνάμε σαν λίστα
        lines = file.readlines()
        # Διατρέχουμε τη λίστα
        for i in range(len(lines)):
            #γραμμή γραμμή
            line = lines[i]
            #Όλες οι ερωτήσεις τελειώνουν με ; οπότε με τη line.rstrip().endswith(";")  ξέρουμε οτι ξεκινάει μια ερώτηση και οι απαντήσεις της
            if line.rstrip().endswith(";"):
            #Αν η συνθήκη ειναι true τότε στέλνουμε ως ορίσματα στην κλάση question τις ερωτήσεις και τις αντίστοιχες απαντήσεις
                question = Question(line, [lines[j].rstrip() for j in range(i + 1, i + 5)] )
                #Προσθέτω στο την ερώτηση στην ανάλογη δυσκολία που παίρνω απο την κλαση question με την questions_level και κάνουμε append
                #την ερώτηση με τις απαντήσεις στο αντίστοιχο level
                questions[question.level].append(question)
                #στο επόμενο σετ ερωτήσεων-απαντήσεων
                i += 5


    return questions

        
                                    
class QuestionController:
    pass


class QuestionView:
    pass

    def __init__(self):
        pass

    def draw(self, surface):
        pass
