import random

import pygame.image

from code.Player import Player
from code.Result import Result
from code.Tower import Tower
from code.Zombie import Zombie
from code.const import WIN_WIDTH, WIN_HEIGHT, ZOMBIE_SPAWN_INTERVAL


class Play:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/GameBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.zombies = []
        self.zombies_reached = 0


    def run(self):
        clock = pygame.time.Clock()

        pygame.mixer_music.load('./assets/sounds/Game.mp3')
        pygame.mixer_music.play(-1)

        tower = Tower(self.window, ((WIN_WIDTH - 128) / 2 , 30))
        player = Player('Player', self.window, ((WIN_WIDTH - 80) / 2, 200))

        last_zombie_spawn = pygame.time.get_ticks()

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
            self.window.blit(source=tower.surf, dest=tower.rect)
            self.window.blit(source=player.surf, dest=player.rect)

            if pygame.time.get_ticks() - last_zombie_spawn >= ZOMBIE_SPAWN_INTERVAL:
                self.spawn_zombie()
                last_zombie_spawn = pygame.time.get_ticks()

            for zombie in self.zombies:
                self.window.blit(source=zombie.surf, dest=zombie.rect)
                zombie.move(tower)
                if zombie.rect.colliderect(tower.rect):
                    self.zombies_reached += 1
                    self.zombies.remove(zombie)

            if self.zombies_reached >= 3:
                result = Result(self.window)
                result.show(False)

            pygame.display.flip()

    def spawn_zombie(self):
        zombie_position_x = random.randint(79, WIN_WIDTH)
        zombie = Zombie('Zombie', self.window, (zombie_position_x - 79, WIN_HEIGHT - 90))

        self.zombies.append(zombie)
