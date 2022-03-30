class Controller:
    """
    Κλάση για την επικοινωνία μεταξύ View και Model.
    Διαχειρίζεται την είσοδο από τον παίκτη
    και αναθέτει τις απαραίτητες εργασίες στις άλλες δύο κλάσεις.
    """

    def __init__(self, view, model):
        """Αρχικοποίηση του Controller

        Ανάθεση σε εσωτερικές μεταβλητές τα View, Model
        :param view: Αντικείμενο View για την εμφάνιση της εφαρμογής
        :param model: Αντικείμενο Model για την αποθήκευση/χειρισμό δεδομένων της εφαρμογής
        """
        self.model = model
        self.view = view
        self.view.set_controller(self)

    def hello(self, what):
        print("Hello from", what)



