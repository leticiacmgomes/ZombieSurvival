import pygame.image

from code.Player import Player
from code.const import WIN_WIDTH


class Play:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/GameBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        clock = pygame.time.Clock()

        pygame.mixer_music.load('./assets/sounds/Game.mp3')
        pygame.mixer_music.play(-1)

        player = Player('Player', self.window, ((WIN_WIDTH - 80) / 2, 30))

        while True:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            player.move()

            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=player.surf, dest=player.rect)

            pygame.display.flip()



