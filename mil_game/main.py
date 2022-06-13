from game import MainGame
from menu import MenuMode  
from splash import SplashMode
from score import ScoreMode
from player import Player
from milgame import GameMode
'''
Το σημείο εισαγωγής στην εφαρμογή

Δημιουργούμε τα κύρια αντικείμενα και ξεκινάμε τον κυρίως βρόχο

'''

# Δείχνουμε τη splash, και μετά τη διώχνουμε
splashscreen = SplashMode(600, 600, "mil_game\images\ek_logo.png", "snd/millionaire_intro.mp3", "LOADING...")
splashscreen.showSplash()
splashscreen = None

# Δημιουγούμε πλαίσιο παιχνιδιού, βάζουμε τίτλο και διαστάσεις. Κύριος βρόχος, μέσα σ' αυτόν τρέχουν
# όλα τα άλλα αντικείμενα / καταστάσεις (menu, play_mode, high_scores, etc) 
mil_game = MainGame("Εκατομμυριούχος", 1280, 720)

# Δημιουργούμε κατάσταση μενού, περνάμε το πλαίσιο παιχνίδιού για να αλλάζουμε καταστάσεις
main_menu = MenuMode(mil_game)

# Δημιουργούμε αντικείμενο αποτελέσματα, περνάμε παιχνίδι, επόμενη κατάσταση, και παίκτες προς εμφάνιση
high_scores = ScoreMode(mil_game,main_menu)

#ορίζουμε την play_mode, η κατάσταση που παίζει όλο το παιχνίδι
#play_mode = GameMode(mil_game, high_scores)

# Ορίζουμε την κατάσταση αποτελέσματα για το αντίστοιχο κουμπί του menu
main_menu.setScoreMode(high_scores)
# main_menu.setPlayMode()
# Ξεκινάμε το παιχνίδι
mil_game.play(main_menu)
