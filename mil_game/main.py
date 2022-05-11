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

mil_game = MainGame("Εκατομμυριούχος", 1024, 600)
main_menu = MenuMode(mil_game)
high_scores = ScoreMode(mil_game,main_menu,players)
main_menu.setScoreMode(high_scores)

mil_game.play(main_menu)
