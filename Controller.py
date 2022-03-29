class Controller:
    """
    Κλάση για την επικοινωνία μεταξύ View και Model.
    Διαχειρίζεται την είσοδο από τον παίκτη
    και αναθέτει τις απαραίτητες εργασίες στις άλλες δύο κλάσεις.
    """

    def __init__(self, view, model):
        """Αρχικοποίηση του Controller

        Ανάθεση σε εσωτερικές μεταβλητές τα View, Model
        :param view:
        :param model:
        """
        self.model = model
        self.view = view



