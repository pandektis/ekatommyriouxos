from Player import Player
import sqlite3
from sqlite3 import Error

class Model:
    """
    Κλάση για την αποθήκευση/χειρισμό δεδομένων της εφαρμογής.

    Περιέχει όλες τις παραμέτρους του παιχνιδιού.
    Φορτώνει τις ερωταπαντήσεις από τη ΒΔ.
    Κρατάει αντικείμενο Player ως τρέχον παίκτη.
    Ορίζει το χρόνο που δίνουμε για την κάθε ερώτηση.
    Δίνει τη σωστή απάντηση για κάθε ερώτηση.

    """
    def __init__(self, name) -> None:
        ''' Αρχικοποίηση κλάσης, ορισμός μεταβλητών'''
        self.p = Player(name)
        self.time_sec = 60
        self.used = set() # Χρησιμοποιημένες ερωτήσεις.
        self.num_played_questions = 0 # Πόσες ερωτήσεις έχουμε παίξει.
        self.cur_difficulty = 1 # Επίπεδο δυσκολίας, για να επιλέγουμε ερωτήσεις.
        self.kerdi = [] # Τα ποσά που θα κερδίζει κάθε ερώτηση. Καρφωτά ή από αρχείο;
        self.cur_question = None # Τρέχουσα ερώτηση
    
    def _set_difficulty(self):
        """Μέθοδος για να θέτουμε τη δυσκολία ανάλογα με τον αριθμο ερωτήσεων"""
        pass

    def _load_question(self, dif):
        """ 
        Βοηθητική μέθοδος που φορτώνει την ερώτηση στη
        μεταβλητή self.cur_question
        Τη χρησιμοποιεί η get_question
        """
        pass
    def get_question(self):
        """ 
        Μέθοδος που επιστρέφει σετ ερώτησης / απαντήσεων (ή σκέτη ερώτηση)
        Χρησιμοποιεί τη _load_question
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
        self.p.update_stats()
        
    def get_correct_answer(self):
        """
        Μέθοδος που επιστρέφει τη σωστή απάντηση.
        """
        pass

    def get_HighScores(self):
        """
        Μέθοδος που θα επιστρέφει λίστα με τα High Scores
        Αφού έχουμε φτιάξει ΒΔ, επιλέγουμε * από τον πίνακα 
        Statistika, ταξινομημένος κατά ΔΑΕΠ, και θα παίρνουμε
        τα χ πρώτα στοιχεία (5;10)"""
        pass
    
    def save_Player(self):
        """
        Μέθοδος για την αποθήκευση του παίκτη στη ΒΔ
        όταν τελειώνει το παιχνίδι
        """
        pass