class Player:
    """
    Κρατάει τα δεδομένα του παίκτη.

    Διατηρεί κι ενημερώνει τα ζητούμενα δεδομένα του παίκτη.
    """
    def __init__(self, name):
        self.name = name
        self.poso = 0
        self.num_questions = 0
        self.total_time = 0
        self.m_o = 0.0
        self.daep = 0.0

    def __str__(self):
        return f"{self.name}, {self.poso}€, {self.total_time}sec, {self.m_o}sec/q, {self.daep}"

    def _calc_mo(self):
        """ Υπολογισμός Μ.Ο. χρόνου ανά ερώτηση"""
        try:
            self.m_o = self.total_time / self.num_questions
        except ZeroDivisionError as Z:
            self.m_o = 0.0

    def _calc_daep(self):
        """Υπολογισμός Δείκτη Αξιολόγησης Επίδοσης Παίκτη"""
        try:
            self.daep = self.poso / self.total_time
        except ZeroDivisionError as Z:
            self.daep = 0.0
