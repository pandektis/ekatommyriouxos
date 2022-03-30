import tkinter as tk
from tkinter import ttk


class View:
    """
    Κλάση για την εμφάνιση της εφαρμογής.

    Υπεύθυνη να εμφανίζει τα δεδομένα στον παίκτη και να
    δέχεται είσοδο από τον παίκτη, την οποία περνάει στον Controller.

    """

    def __init__(self):
        self.c = None

    def set_controller(self, controller):
        """
        Σύνδεση με τον Controller

        Ορίζουμε ως attribute της κλάσης τον Controller
        ώστε να καλούμε μεθόδους σ' αυτόν και να του περνάμε
        την είσοδο του παίκτη.
        """
        self.c = controller
        # Προς αφαίρεση 2 γραμμές, δοκιμή σύνδεσης View με Controller
        print(self.c)
        self.c.hello("view")



