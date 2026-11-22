import pygame
from pip._internal.index import sources

from code.const import WIN_WIDTH, WIN_HEIGHT, C_PURPLE, MENU_OPTION, C_BLACK, C_WHITE, C_PURPLE_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0

        pygame.mixer.music.load('./assets/sounds/Menu.wav')
        pygame.mixer.music.play(-1)
        print('Menu carregado')



        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text('ZOMBIE SURVIVAL', 40, (WIN_WIDTH / 2, 60), C_BLACK)

            for i in range(len(MENU_OPTION)):
                if menu_option == i:
                    self.menu_text(MENU_OPTION[i], 20, (WIN_WIDTH / 2, 150 + 50 * i), C_PURPLE)
                else:
                    self.menu_text(MENU_OPTION[i], 20, (WIN_WIDTH / 2, 150 + 50 * i), C_PURPLE_WHITE)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        print(MENU_OPTION[menu_option])
                        return MENU_OPTION[menu_option]

    def menu_text(self, text, text_size, text_pos, text_color):
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)