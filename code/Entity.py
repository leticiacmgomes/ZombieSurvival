from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name):
        self.name = name
        self.surf = pygame.image.load(f'../assets/images/{name}.png').convert_alpha()

    @abstractmethod
    def move(self):
        pass