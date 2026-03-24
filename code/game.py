import sys

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_WHITE, COLOR_RED
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
            pygame.init()
            self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
            self.last_score = 0

    def show_score(self):
        font_title = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        font_text = pygame.font.SysFont("Lucida Sans Typewriter", 25)
        while True:
            self.window.fill((0, 0, 0))

            title_surf = font_title.render("SCORE", True, (200, 0, 0))
            score_surf = font_text.render(f"Ultimo Score: {self.last_score}", True, COLOR_WHITE)
            back_surf = font_text.render("Pressione ENTER para voltar", True, COLOR_WHITE)

            # centro da tela
            center_x = WIN_WIDTH // 2
            center_y = WIN_HEIGHT // 2

            # posições organizadas
            self.window.blit(title_surf, title_surf.get_rect(center=(center_x, center_y - 60)))
            self.window.blit(score_surf, score_surf.get_rect(center=(center_x, center_y)))
            self.window.blit(back_surf, back_surf.get_rect(center=(center_x, center_y + 60)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

    def show_game_over(self):
        font_title = pygame.font.SysFont("Lucida Sans Typewriter", 42)
        font_text = pygame.font.SysFont("Lucida Sans Typewriter", 24)

        bg = pygame.image.load('./asset/GameOver.png').convert()
        bg = pygame.transform.scale(bg, (WIN_WIDTH, WIN_HEIGHT))

        while True:
            self.window.blit(bg, (0, 0))

            title_surf = font_title.render("GAME OVER", True, COLOR_RED)
            score_surf = font_text.render(f"Score: {self.last_score}", True, COLOR_WHITE)
            retry_surf = font_text.render("ENTER = jogar novamente", True, COLOR_WHITE)
            menu_surf = font_text.render("ESC = voltar ao menu", True, COLOR_WHITE)

            center_x = WIN_WIDTH // 2
            center_y = WIN_HEIGHT // 2

            self.window.blit(title_surf, title_surf.get_rect(center=(center_x, center_y - 90)))
            self.window.blit(score_surf, score_surf.get_rect(center=(center_x, center_y - 20)))
            self.window.blit(retry_surf, retry_surf.get_rect(center=(center_x, center_y + 50)))
            self.window.blit(menu_surf, menu_surf.get_rect(center=(center_x, center_y + 90)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "RETRY"
                    if event.key == pygame.K_ESCAPE:
                        return "MENU"

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]: # NEW GAME
                while True:
                    level = Level(self.window, 'Level1', menu_return)
                    level_return = level.run()

                    if level_return == 'GAME OVER':
                        self.last_score = level.score
                        option = self.show_game_over()

                        if option == "RETRY":
                            continue
                        elif option == "MENU":
                            break
                        else:
                            break

            elif menu_return == MENU_OPTION[1]:  # SCORE
                self.show_score()

            elif menu_return == MENU_OPTION[2]:  # EXIT
                pygame.quit()
                sys.exit()

