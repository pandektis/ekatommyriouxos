class Player:
    """
    Κρατάει τα δεδομένα του παίκτη.

    Διατηρεί κι ενημερώνει τα ζητούμενα δεδομένα του παίκτη.
    """
    def __init__(self, name):
        self.name = name
        self.poso = 0
        self.num_questions = 0
        self.total_time = 0.0
        self.m_o = 0.0
        self.daep = 0.0

    def __str__(self):
        return f"{self.name:^12}|{self.poso:>10}€|{self.total_time:>7} sec|{self.m_o:>7} sec/q|{self.daep:>7}"

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

    def update_stats(self):
        self._calc_mo()
        self._calc_daep()



class PlayerController:
    pass
class PlayerScoreView:

    def __init__(self):
        pass







    # Για να τρέχει ξεχωριστά το αρχείο, για testing
    if __name__ == "__main__":
        pass