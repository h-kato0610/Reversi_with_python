import pygame
from pygame.locals import *

class Game():
    def __init__(self):
        display_size = (400, 400)
        pygame.init()
        pygame.screen = pygame.display.set_mode(display_size)
        pygame.display.set_caption('HelloWorld')

    def __is_winner(self):
        # TODO implemented yet
        return None

    def board(self):
        # TODO implemented yet
        return None

    def score(self):
        # TODO implemented yet
        return None

    def stone(self):
        # TODO implemented yet
        return None

    def player(self):
        # TODO implemented yet
        return None

    def enemy(self):
        # TODO implemented yet
        return None
