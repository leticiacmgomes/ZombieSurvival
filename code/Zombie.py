from code.Entity import Entity
from code.const import WIN_WIDTH


class Zombie(Entity):
    def __init__(self, name, window, position):
        super().__init__(name, window, position)
        self.speed = 2
        if self.rect.centerx < WIN_WIDTH / 2:
            self.side = 'left'
        else:
            self.side = 'right'

    def move(self, tower):
        self.rect.centery -= self.speed

        if self.side == 'left':
            if self.rect.centerx < tower.rect.left:

                if self.rect.centerx < WIN_WIDTH / 4:
                    self.rect.centerx += self.speed

                elif self.rect.centery <= 350:
                    self.rect.centerx += self.speed

        elif self.side == 'right':
            if self.rect.centerx > tower.rect.right:

                if self.rect.centerx > WIN_WIDTH / 4 * 3:
                    self.rect.centerx -= self.speed

                elif self.rect.centery <= 350:
                    self.rect.centerx -= self.speed