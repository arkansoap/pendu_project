import pygame
from constantes_pendu import *
import sys


class Jeu:
    def __init__(self):
        pygame.init
        pygame.font.init()
        self.clock = pygame.time.Clock
        self.screen = pygame.display.set_mode(SIZESCREEN)
        self.game_surf = pygame.Surface((GAMESURF))
        self.game_rect = self.game_surf.get_rect(topleft=(TOPLEFT_GAMESURF))
        self.game_surf.fill("grey")
        self.base_font = pygame.font.SysFont("Black", 32, True)
        self.user_text = ""

    def gere_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    self.user_text = self.user_text[:-1]

                # Unicode standard is used for string
                # formation
                else:
                    self.user_text += event.unicode

    def plop_text(self):
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        self.game_surf.blit(text_surface, (10, 10))

    def main(self):
        self.screen.fill("black")
        self.gere_event()
        self.plop_text()
        self.screen.blit(self.game_surf, self.game_rect)
        pygame.display.update()


if __name__ == "__main__":

    jeu = Jeu()
    while jeu:

        jeu.main()
