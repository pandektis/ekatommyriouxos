from milgame import MainGame
from menu import MenuMode
from splash import SplashMode

splashscreen = SplashMode(600, 600, "mil_game\images\ek_logo.png", "snd/millionaire_intro.mp3", "LOADING...")
splashscreen.showSplash()
splashscreen = None

mil_game = MainGame("Εκατομμυριούχος", 1024, 600)
main_menu = MenuMode(mil_game)
print(main_menu)
mil_game.play(main_menu)
