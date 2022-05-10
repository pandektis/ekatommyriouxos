from turtle import bgcolor
import pygame
from pygame.locals import *




class Button(pygame.sprite.Sprite):
    '''
    Κλάση για τη δημιουργία buttons.
    Χρησιμοποιείται για τις απαντήσεις, στο menu, στις βοήθειες
    '''
    def __init__(self, width, height, bgColor, bgImage = None, clickable = False) -> None:
        super().__init__()
        self.SIZE = width, height
        self.button_image = pygame.Surface(self.SIZE)
        if clickable:
            self.clicked_image = pygame.Surface(self.SIZE)
            self.hover_image = pygame.Surface(self.SIZE)
        self.button_image.fill((bgColor))
        self.button_image.set_colorkey(bgColor)
        if(bgImage):
            self.bg_img = pygame.image.load(bgImage).convert_alpha()
            self.button_image.blit(pygame.transform.scale(self.bg_img, self.SIZE),(0,0))
        else:
            self.bg_img = bgImage
        self.image = self.button_image
        self.rect = self.button_image.get_rect()
        self.msg = ""
        

    def add_text(self, font, text, textColor):
        """
        Προσθέτει κείμενο στο button
        Συνεχίζει σε νέα γραμμή απο κάτω αν δεν χωράει.
        """
        self.msg = text
        images = []
        linespacing = 2
        lines = 1
        fontHeight = font.size(text)[1]
        y = self.rect.centery - fontHeight // 2
        while text:
            i = 1
            while font.size(text[:i])[0] < self.rect.width and i < len(text):
                i += 1

            if i < len(text):
                i = text.rfind(" ", 0, i) + 1
                y -= fontHeight // 2 - linespacing

            images.append(font.render(text[:i], True, textColor))
            text = text[i:]
            
        for image in images:
            self.button_image.blit(image, (self.rect.centerx - image.get_rect().width // 2, y))
            y += fontHeight + linespacing