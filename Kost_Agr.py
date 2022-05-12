import tkinter as tk
from tkinter import ttk
import random

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
        #τραβηγμα τυχαίας ερώτησης.Χωρίς το -1 το προγραμμα βγαίνει out of range
        question_number = random.randint(0, len(self.questions[level])-1)
        #διαγραφη της ερώτησης με την pop 
        question = self.questions[level].pop(question_number)
        #κρατάμε τον αριθμό των ερωτήσεων
        self.questions_asked+=1



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

        #Αρχικοποίηση κουμπιού 50-50
        self.fifty50_btn = tk.Button(self.question_frame, text="50-50")
        # Αρχικοποίηση κουμπιού Προτασης βοήθειας
        self.suggestion_btn = tk.Button(self.question_frame, text="Πρόταση")
        # Αρχικοποίηση κουμπιού Αντικατάστασης
        self.replace_btn = tk.Button(self.question_frame, text="Αντικατάσταση")

        #Δημιουργία κουμπιών και τοποθέτηση
        self.fifty50_btn.pack(pady=10, side="left", expand="true")
        self.suggestion_btn.pack(side="left", expand="true")
        self.replace_btn.pack(side="left", expand="true")

        #Εισαγωγη μεθόδου στο κάθε κουμπί
        self.fifty50_btn.bind('<Button-1>', lambda event: self.fifty50())
        self.suggestion_btn.bind('<Button-1>', lambda event: self.suggestion())
        self.replace_btn.bind('<Button-1>', lambda event: self.replace())

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



    def answer_clicked(self, clicked_button_number):
        """Η συνάρτηση καλείται όταν ο παίκτης επιλέγει μια απάντηση και εμφανίζει αν η απάντηση ειναι σωστή η όχι"""
        #Η correct ειναι bool μεταβλητή για το αν ειναι σωστή η απάντηση η όχι True or False
        correct = clicked_button_number == self.correct_button_number
        #χρωματίζουμε τη σωστή η τη λάθος απάντηση
        self.answer_buttons[self.correct_button_number]["bg"] = "green"
        if not correct:
            self.answer_buttons[clicked_button_number]["bg"] = "red"

            # μετρητής λάθος απαντήσεων
            self.game.mistakes += 1
            # αν γίνουν 3 λάθη καλούμε την game over και τέλος παιχνιδιου
            if self.game.mistakes == 3:
                self.game_over()




        #εισαγωγη του κουμπιού της επόμενης ερώτησης
        self.next_btn.pack(side="left")

    def fifty50(self):
        """Όταν κάνουμε κλικ στη βοήθεια 50 50. Επισημαίνει δύο λανθασμένες απαντήσεις με κόκκινο χρώμα"""
        #λιστα με τα νούμερα των πιθανών απαντήσεων
        ans = [0, 1, 2, 3]
        #αφαίρεση απο τη λίστα του νούμερου της σωστής απάντησης
        ans.remove(self.correct_button_number)
        #αφαίρεση μιας ακόμας random απάντησης εκτός της σωστης που έχει αφαιρεθεί
        ans.remove(random.choice(ans))
        #κάνουμε κόκκινα 2 κουμπιά απαντήσεων
        for i in ans:
            self.answer_buttons[i]["bg"] = "red"
        #αφαίρεση κουμπιού όταν πατηθεί
        self.fifty50_btn.forget()


    def suggestion(self):
        """Όταν κάνουμε κλικ στη βοήθεια προτασης. Επισημαίνει όλες τις λανθασμένες απαντήσεις με κόκκινο χρώμα"""
        #με την ίδια λογική όπως με το 50 50
        ans = [0, 1, 2, 3]
        #αφαιρούμε τη σωστή απάντηση
        ans.remove(self.correct_button_number)
        #κάνουμε κοκκινές όλες τις λανθασμένες
        for i in ans:
            self.answer_buttons[i]["bg"] = "red"
        self.suggestion_btn.forget()


    def replace(self):
        """Όταν κάνουμε κλικ στη βοήθεια αντικατάστασης."""
        #απλά καλούμε την ask question και ρωτάμε μια καινούργια ερώτηση
        self.ask_question()
        #αφαιρούμε μια ερώτηση απο τον αριθμό ερωτήσεων
        self.game.questions_asked -= 1
        #print(self.questions_asked)

        self.replace_btn.forget()

    def game_over(self):
        """Καλείται στο τέλος του παιχνιδιού"""
        self.question_frame.forget()

        tk.Label(text="GAME OVER", bg="black", fg="white").pack()
        tk.Label(text="Αριθμός ερωτήσεων", bg="black", fg="white").pack()
        tk.Label(text=self.game.questions_asked, bg="black", fg="white").pack()



    def get_lambda(self, i):
        """Βηθητική συνάρτηση γιατί το προγραμμα κόλαγε στο for που δημιουργούσε τα κουμπιά στην init_question_frame
        https://stackoverflow.com/questions/14259072/tkinter-bind-function-with-variable-in-a-loop"""

        return lambda event: self.answer_clicked(i)


def read_questions():
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


def main():
	game = Graphic()
if __name__ == '__main__':
	main()

