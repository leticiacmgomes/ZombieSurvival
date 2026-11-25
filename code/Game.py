import pygame

from code.Controls import Controls
from code.Menu import Menu
from code.Play import Play
from code.const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_option = menu.run()

            if menu_option == 'QUIT':
                pygame.quit()
                quit()
            if menu_option == 'CONTROLS':
                controls = Controls(self.window)
                controls.show()

            if menu_option == 'PLAY':
                play = Play(self.window)
                play.run()