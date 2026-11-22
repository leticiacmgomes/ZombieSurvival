import pygame



class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        print('Menu carregado')
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()