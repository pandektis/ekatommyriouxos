from game import MainGame
from menu import MenuMode
from splash import SplashMode
from score import ScoreMode
from player import Player
'''
Το σημείο εισαγωγής στην εφαρμογή

Δημιουργούμε τα κύρια αντικείμενα και ξεκινάμε τον κυρίως βρόχο

'''

# Δείχνουμε τη splash, και μετά τη διώχνουμε
players = [Player("Player " + str(i)) for i in range(10)] # Προς αφαίρεση, δοκιμαστικό
splashscreen = SplashMode(600, 600, "mil_game\images\ek_logo.png", "snd/millionaire_intro.mp3", "LOADING...")
splashscreen.showSplash()
splashscreen = None

# Δημιουγούμε παιχνίδι, βάζουμε τίτλο και διαστάσεις
mil_game = MainGame("Εκατομμυριούχος", 1024, 600)
# Δημιουργούμε μενού, περνάμε το αντικείμενο παιχνίδι
main_menu = MenuMode(mil_game)
# Δημιουργούμε αντικείμενο αποτελέσματα, περνάμε παιχνίδι, επόμενη κατάσταση, και παίκτες προς εμφάνιση
high_scores = ScoreMode(mil_game,main_menu,players)
# Ορίζουμε την κατάσταση αποτελέσματα για το αντίστοιχο κουμπί του menu
main_menu.setScoreMode(high_scores)

# Ξεκινάμε το παιχνίδι
mil_game.play(main_menu)
