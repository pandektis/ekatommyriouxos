import tkinter as tk
from tkinter import ttk
import random

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



class Game:
    """Κάθε παιχνίδι είναι ένα αντικείμενο Game. Το αντικείμενο Game θα μπορουσε να  διαχειρίζεται ποιος παίζει ,
       το συνολικό χρόνο του τρέχοντος παιχνιδιού,οπως το εχω φτιάξει διαχειρίζεται  ποιες ερωτήσεις  μπαίνουν."""

    def __init__(self):
        self.questions = read_questions()
        self.questions_asked = 0
        self.mistakes = 0

    def get_question(self):
        """Παίρνει μια τυχαία ερώτηση από το τρέχον επίπεδο, επιστρέφει την ερώτηση με της απαντήσεις που θα χρησιμοποιήσουμε"""
        #Εδω γινεται ο έλενχος της δυσκολιας των ερώτησεων που θα τραβηχτούν απο το λεξικό
        if self.questions_asked < 5:
            level = "A"
        elif self.questions_asked < 10:
            level = "B"
        else:
            level = "C"
        #τραβηγμα τυχαίας ερώτησης
        question_number = random.randint(0, len(self.questions[level]))
        #διαγραφη της ερώτησης με την pop
        question = self.questions[level].pop(question_number)

        print(question)
        return question


class Graphic:
    def __init__(self):
        self.root = tk.Tk()
        self.root["bg"] = "white"
        self.root.geometry("700x500")
        #Κλείδωμα μεγέθους frame
        self.root.resizable(width=False, height=False)
        self.init_question_frame()
        self.game = Game()
        self.ask_question()
        self.root.mainloop()

    def init_question_frame(self):
        """Χτίζουμε το frame των ερωτήσεων
        Κάθε ερώτηση εχει ενα καινούργιο frame.Το frame των ερωτήσεων ειναι αντιγραφή απο ένα quiz frame"""

        self.question_frame = tk.Frame(self.root, bg='black')
        self.question_frame.pack()
        self.info_lbl = tk.Label(self.question_frame, bg="black", fg="white")
        self.info_lbl.pack()
        self.question_lbl = tk.Label(self.question_frame)
        self.question_lbl.pack()
        self.answer_buttons = list()
        for i in range(4):
            button = tk.Button(self.question_frame)

            button.bind('<Button-1>', self.get_lambda(i))
            button.pack()

            self.answer_buttons.append(button)
        #Δημιουργία κουμπιού next question και bind την επόμενη ερώτηση
        self.next_btn = tk.Button(self.question_frame, text="Next question", bg="white")
        self.next_btn.bind('<Button-1>', lambda event: self.ask_question())

    def ask_question(self):
        """Εδώ γινεται η δουλειά εμφάνισης της ερώτησης στο γραφικό"""
        #παίρνουμε την ερώτηση απο την get_question της κλασης game
        question = self.game.get_question()
        #εμφανιση της ερώτησης στο γραφικο
        self.question_lbl["text"] = question.question
        #χροματισμός κουμπιών και εμφανιση απαντήσεων της ερώτησης
        for i in range(4):
            self.answer_buttons[i]["bg"] = "gray"
            #παίρνουμε τις απαντήσεις που ειναι οι question.answers[i] για τις 4 απαντήσεις
            self.answer_buttons[i]["text"] = question.answers[i]
        #Ορισμος σωστης απάντησης,την απάντηση την παιρνουμε απο την κλαση question συνάρτηση data με το question.correct_answer
        self.correct_button_number = question.correct_answer
        print(question.correct_answer)


    def answer_clicked(self, clicked_button_number):
        """Η συνάρτηση καλείται όταν ο παίκτης επιλέγει μια απάντηση και εμφανίζει αν η απάντηση ειναι σωστή η όχι"""
        #Η correct ειναι bool μεταβλητή για το αν ειναι σωστή η απάντηση η όχι True or False
        correct = clicked_button_number == self.correct_button_number
        #χρωματίζουμε τη σωστή η τη λάθος απάντηση
        self.answer_buttons[self.correct_button_number]["bg"] = "green"
        if not correct:
            self.answer_buttons[clicked_button_number]["bg"] = "red"

        #εισαγωγη του κουμπιού της επόμενης ερώτησης
        self.next_btn.pack(side="left")


    def get_lambda(self, i):
        """Βηθητική συνάρτηση γιατί το προγραμμα κόλαγε στο for που δημιουργούσε τα κουμπιά στην init_question_frame
        https://stackoverflow.com/questions/14259072/tkinter-bind-function-with-variable-in-a-loop"""

        return lambda event: self.answer_clicked(i)


def read_questions():
    """Ανάγνωση του αρχείου txt με ερωτήσεις
    Επιστρέφει  λεξικό των ερωτήσεων
     {"A" : κατάλογος ερωτήσεων Α, "B" : κατάλογος ερωτήσεων Β...}"""

    questions = {"A": list(), "B": list(), "C": list()}
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
                questions[question.level].append(question)

                i += 5

    return questions


def main():
	game = Graphic()
if __name__ == '__main__':
	main()

