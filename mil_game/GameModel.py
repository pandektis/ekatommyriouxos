from player import Player

class Model:
    """
    Κλάση για την αποθήκευση/χειρισμό δεδομένων της εφαρμογής.

    Περιέχει όλες τις παραμέτρους του παιχνιδιού.
    Φορτώνει τις ερωταπαντήσεις από το αρχείο.
    Κρατάει αντικείμενο Player ως τρέχων παίκτη.
    Ορίζει το χρόνο που δίνουμε για την κάθε ερώτηση.
    Δίνει τη σωστή απάντηση για κάθε ερώτηση.
    Αποθηκεύει / διαβάζει High scores
    """

    def __init__(self, name) -> None:
        ''' Αρχικοποίηση κλάσης, ορισμός μεταβλητών'''
        self.player = Player(name)
        self.time_sec = 60
        self.used = set() # Χρησιμοποιημένες ερωτήσεις.
        self.num_played_questions = 0 # Πόσες ερωτήσεις έχουμε παίξει.
        self.cur_difficulty = 1 # Επίπεδο δυσκολίας, για να επιλέγουμε ερωτήσεις.
        self.kerdi = [] # Τα ποσά που θα κερδίζει κάθε ερώτηση. Καρφωτά ή από αρχείο;
        self.cur_question = None # Τρέχουσα ερώτηση
        self.high_scores = [] # Λίστα με Player objects, για να κρατάει τα σκορ. Διαβάζεται από / σώζεται σε αρχείο (pickle)
    
    def _set_difficulty(self):
        """Μέθοδος για να θέτουμε τη δυσκολία ανάλογα με τον αριθμο ερωτήσεων"""
        pass

    
    def get_question(self):
        """ 
        Μέθοδος που επιστρέφει σετ ερώτησης / απαντήσεων (ή σκέτη ερώτηση)
        
        """
        pass

    def get_correct_answer(self):
        """
        Μέθοδος που επιστρέφει τη σωστή απάντηση.
        """
        pass

    def get_time(self):
        """ Μέθοδος που επιστρέφει το διαθέσιμο χρόνο """
        return self.time_sec

    def update_player(self, time_spent, poso):
        """ 
            Μέθοδος που ενημερώνει τα στοιχεία του τρέχοντος παίκτη
            (self.p) μετά από κάθε ερώτηση
        """
        self.p.poso = poso
        self.p.total_time += time_spent
        self.p.num_questions = self.num_played_questions
        self.p.update_stats() # Καλεί μέθοδο του p (Player) για υπολογισμό στατιστικών
        
    
    def get_HighScores(self):
        """
        Μέθοδος που θα επιστρέφει λίστα με τα High Scores
        για να τη δείξουμε στο View
        Να επιστρέφει strings? Μάλλον.TODO
        """
        pass
    
    def save_HighScores(self):
        """
        Μέθοδος για την αποθήκευση των High scores
        """
        pass


    # Για να τρέχει ξεχωριστά το αρχείο, για testing
    if __name__ == "__main__":
        pass