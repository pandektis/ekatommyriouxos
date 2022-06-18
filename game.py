import pygame, os, sys
from pygame.locals import *

class BaseMode(object):
    """
    Βασική κλάση κατάστασης, από εδώ κληρονομούν όλες οι κλάσεις κατάστασης του παιχνιδιού
    """

    def __init__(self, game) -> None:
        """
        Αναφορά στο game (τη μηχανή δλδ) για να καλούμε την changeMode()
        και να μεταβαίνουμε από τη μία κατάσταση στην άλλη
        """
        self.game = game

    def onEnter(self, oldMode):
        """
        Μέθοδος για εκτέλεση κατά την είσοδο σε μία κατάσταση
        για εκτέλεση λειτουργιών αρχικοποίησης π.χ.
        """
        pass

    def onExit(self):
        """
        Μέθοδος για εκτέλεση κατά την έξοδο απο μία κατάσταση
        για εκτέλεση λειτουργιών εκκαθάρισης, αποθήκευσης, κ.α."""
        pass

    def update(self, gameTime, event_list):
        """
        Μέθοδος ελέγχου κατάστασης, η λογική της κατάστασης
        """
        pass

    def draw(self, surface):
        """
        Μέθοδος εμφάνισης των γραφικών της κατάστασης
        """
        pass

class MainGame(object):
    """
    Κλάση για την υλοποίηση του κυρίως βρόχου του παιχνιδιού

    Εδώ γίνεται η εμφάνιση / ανανέωση κάθε κατάστασης του παιχνιδιού
    
    """
    def __init__(self, gameName, width, height) -> None:
        """
        Αρχικοποίηση της pygame, ορισμός παραθύρου εφαρμογής και ρολογιού"""
        pygame.init()
        pygame.display.set_caption(gameName)

        self.clock = pygame.time.Clock()
        self.mainscreen = pygame.display.set_mode((width, height))
        self.background = pygame.Color(0, 0, 0)
        self.currentMode = None

    def changeMode(self, newMode):
        """
        Αλλαγή κατάστασης παιχνιδιού (μενού, παιχνίδι, high_scores, κτλ..)
        Αν δεν υπάρχει κατάσταση (περαστεί None), τερματίζουμε το παιχνίδι
        """
        # καλούμε την onExit της κατάστασης που 'φεύγει' (cleanup, reset, κτλ.)
        if(self.currentMode):
            self.currentMode.onExit()

        if(newMode == None):
            pygame.quit()
            sys.exit()

        oldMode = self.currentMode    
        self.currentMode = newMode
        # καλούμε την onEnter της νέας κατάστασης, για εργασίες  που χρειάζεται να κάνει στην αρχή
        newMode.onEnter(oldMode)


    def play(self, startMode):
        """
        Κύριος βρόχος εφαρμογής, εδώ μέσα τρέχει όλο το παιχνίδι
        Είναι η 'μηχανή' του παιχνιδιού
        Τροποποιώντας κατάλληλα την κάθε κατάσταση, έχουμε και διαφορετικό αποτέλεσμα,
        χωρίς να πειράζουμε αυτή την μέθοδο
        
        """
        # ορίζουμε αρχική κατάσταση
        self.changeMode(startMode)
        
        # κύριος βρόχος, εδώ μέσα συμβαίνουν όλες οι λειτουργίες
        while True:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == QUIT:
                    self.changeMode(None)
                    # pygame.quit()
                    # sys.exit()
            
            gameTime = self.clock.get_time()

            # καλούμε την update() της τρέχουσας κατάστασης (κλάσεις GameMode, MenuMode, κτλ)
            # αυτή είναι υπεύθυνη για τις λειτουργίες που χρειάζεται κάθε κατάσταση
            if(self.currentMode):
                self.currentMode.update(gameTime, event_list)

            # self.mainscreen.fill(self.background)

            # καλούμε την draw() της τρέχουσας κατάστασης (κλάσεις GameMode, MenuMode, κτλ)
            # αυτή είναι υπεύθυνη για την εμφάνιση των στοιχείων που έχει κάθε κατάσταση.
            if(self.currentMode):
                self.currentMode.draw(self.mainscreen)
                
            pygame.display.update()
            # ορίζουμε τα frames σε 30 ανά δευτερόλεπτο
            self.clock.tick(30)