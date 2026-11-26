import pygame.image

from code.Entity import Entity


class Tower:

    def __init__(self, window, position):
        self.window = window
        self.surf = pygame.image.load('./assets/images/Tower.svg')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])