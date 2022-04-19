

class Question:
    """Κλάση που διαχειρίζεται την εμφάνιση συμπεριλαμβανομένου του επιπέδου και ενός ακέραιου αριθμού 0-3
    που υποδεικνύει ποια είναι η σωστή απάντηση"""

    def __init__(self, question, answers):
        #Σκοπός της rstrip(";\n") ειναι να εμφανίζονται η δυσκολία και η σωστή απάντηση δίπλα στην ερώτηση και όχι απο κάτω
        self.question = question.rstrip(";\n")
        self.answers = answers
        self.data()
    #Μέθοδος σύμπτυξης ερωτήσεων απαντήσεων σωστής απάντησης και δυσκολίας
    def __str__(self):
        text = (self.question + self.level +
                str(self.correct_answer) +
                "\n" + "\n".join(self.answers))

        return (text)

    def data(self):
        """Βρίσκει τη σωστή απάντηση και εξάγει το επίπεδο της ερώτησης."""
        #me tin enumerate psaxnoyme to * stis apantiseis otan to vroyme kseroyme oti auti einai i swsti apantisi,episeis kratame kai to counter
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
                        return


def read_questions():
    """Ανάγνωση του αρχείου txt με ερωτήσεις
    Επιστρέφει  λίστες των ερωτήσεων
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

                #Προσθέτω τη δυσκολία στο τέλος της ερώτησης
                questions[question.level].append(question)
                print(question)

                i += 5


    return questions
read_questions()

def save_stats(onoma_paixti, kerdismeno_poso, synolikos_xronos, arithmos erwtisewn):
    """Ανακαλεί τα προηγούμενα στατιστικά και προσθέτει το τελευταίο παιχνίδι στα στατιστικά."""

    stats = from_pickle()



    to_pickle(stats)
pass

def to_pickle(stats):
    """Αποθηκεύει στατιστικά στοιχεία σε αρχείο"""
pass

def from_pickle():
    """Διαβάζει το αρχείο στατιστικών στοιχείων σε ένα dict. Δημιουργεί ένα νέα dict αν το αρχείο δεν υπάρχει.
    Στη συνέχεια επιστρέφει το dict"""

    return stats


