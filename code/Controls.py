import sys

import pygame
from pygame import KEYDOWN, K_ESCAPE

from code.const import CONTROLS, WIN_WIDTH, C_RED, C_BLACK

class Controls:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def show(self):
        while True:
            self.window.blit(self.surf, self.rect)
            self.control_text('CONTROLS', 35, (WIN_WIDTH / 2, 60), C_RED)

            for i in range(len(CONTROLS)):
                self.control_text(CONTROLS[i], 20, (WIN_WIDTH / 2, 120 + 50 * i), C_BLACK)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def control_text(self, text, text_size, text_pos, text_color):
        text_font = pygame.font.SysFont(name="helvetica", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
