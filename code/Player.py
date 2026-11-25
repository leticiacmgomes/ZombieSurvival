import pygame.key

from code.Entity import Entity
from code.const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Player(Entity):
    def __init__(self, name, window, position):
        super().__init__(name, window, position)
        self.speed = ENTITY_SPEED[self.name]

    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_w] and self.rect.top > 0:
            self.rect.centery -= self.speed

        if pressed[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += self.speed

        if pressed[pygame.K_a] and self.rect.left > 0:
            self.rect.centerx -= self.speed

        if pressed[pygame.K_d] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += self.speed

