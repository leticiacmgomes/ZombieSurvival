from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name, window, position):
        self.name = name
        self.window = window
        self.surf = pygame.image.load(f'./assets/images/{name}.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])

    @abstractmethod
    def move(self):
        pass