import pygame
from pygame import KEYDOWN, K_ESCAPE

from code.const import WIN_WIDTH, WIN_HEIGHT, C_PURPLE


class Result:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def show(self, isVictory):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            result_text = 'VOCÊ PERDEU. TRÊS ZUMBIS INVADIRAM A TORRE!' if not isVictory else 'VOCÊ GANHOU, PROTEGEU A PRINCESA DOS ZUMBIS'
            self.result_text(result_text, 25, (WIN_WIDTH / 2 , WIN_HEIGHT / 2), C_PURPLE)
            self.result_text('PRESSIONE ESC PARA VOLTAR', 20, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 100), C_PURPLE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()

    def result_text(self, text, text_size, text_pos, text_color):
        text_font = pygame.font.SysFont(name="helvetica", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)
