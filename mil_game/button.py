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
        self.text_image = self.button_image.copy()
        self.text_image.set_colorkey((0,0,0))
        if clickable:
            self.clicked_image = self.button_image.copy()
            self.hover_image = self.button_image.copy()
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

            images.append(font.render(text[:i], True, textColor,(0,0,0)))
            text = text[i:]
            
        for image in images:
            self.text_image.blit(image, (self.rect.centerx - image.get_rect().width // 2, y))
            y += fontHeight + linespacing

class QAButton(pygame.sprite.Sprite):


    def __init__(self,group, aRect):
        super().__init__(group)
        self.rect = aRect
        self.text_surf = pygame.Surface(self.rect.size)
        self.text_surf.set_colorkey((0,0,0))
        self.base_image = self.text_surf.copy()
        self.button_image = self.text_surf.copy()
        self.hover_image = self.text_surf.copy()
        self.clicked_image = self.text_surf.copy()
        self.setup()


    def setup(self):
        self.text_surf.fill((0,0,0))
        self.button_image.fill((0,0,0))
        self.hover_image.fill((96, 96, 96))
        pygame.draw.rect(self.hover_image, (196, 196, 196), self.hover_image.get_rect(), 3)
        self.clicked_image.fill((96, 196, 96))
        self.image = self.button_image
        self.msg = ""
        self.clicked = False
        self.chosen = False

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
        # y = self.rect.centery - fontHeight // 2
        y = self.text_surf.get_rect().height // 2 - fontHeight // 2
        while text:
            i = 1
            while font.size(text[:i])[0] < self.rect.width and i < len(text):
                i += 1

            if i < len(text):
                i = text.rfind(" ", 0, i) + 1
                y -= fontHeight // 2 - linespacing

            images.append(font.render(text[:i], True, textColor,(0,0,0)))
            text = text[i:]
            
        for image in images:
            image.set_colorkey((0,0,0))
            self.text_surf.blit(image, (self.text_surf.get_rect().centerx - image.get_rect().width // 2, y))
            y += fontHeight + linespacing

        self.button_image.blit(self.text_surf, (0,0))
        self.hover_image.blit(self.text_surf, (0,0))
        self.clicked_image.blit(self.text_surf, (0,0))

    def setRadioButtons(self, buttons):
        self.buttons = buttons

    def update(self, event_list, pos):
        hover = self.rect.collidepoint(pos)
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover and event.button == 1:
                    if self.clicked:
                        self.chosen = True
                    else:    
                        for rb in self.buttons:
                            rb.clicked = False
                        self.clicked = True
                       

        self.image = self.button_image
        if self.clicked:
            self.image = self.clicked_image
        elif hover:
            self.image = self.hover_image

