import pygame as pg
from pygame.locals import *
class SplashMode(object):
    def __init__(self, width, height, bgPath, sndPath, msg) -> None:
        pg.init()
        self.s = pg.display.set_mode((width, height), pg.NOFRAME)
        self.background = pg.transform.scale(pg.image.load(bgPath).convert_alpha(), (width, height))
        font = pg.font.SysFont(None, 60, bold=True)
        self.text = font.render(msg, True, pg.Color('cyan4'))
        self.text_size = font.size(msg)
        self.text_coords = self.text.get_rect(center = (width//2, self.text_size[1]))
        pg.mixer.music.load(sndPath)
       
    def draw(self, surface, alpha):
        surface.fill((0,0,0))
        self.background.set_alpha(alpha)
        surface.blit(self.background, (0, 0))
        # surface.blit(self.text, self.text_coords)

    def showSplash(self):
        a = 0
        self.s.fill((0,0,0))
        self.draw(self.s,a)
        clock = pg.time.Clock()
        pg.display.update()
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play()    
        while pg.mixer.music.get_busy():
            pg.event.pump()
            self.draw(self.s, a)
            if a < 255:
                self.s.blit(self.text, self.text_coords)
                a += 1
            
            pg.display.flip()
            clock.tick(30)
        
        pg.display.quit()





if __name__ == "__main__":

    splash = SplashMode(600, 600, "mil_game\images\ek_logo.png", "snd/millionaire_intro.mp3", "LOADING...")
    splash.showSplash()
    
            
        
        