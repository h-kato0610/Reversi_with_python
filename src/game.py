import pygame
from pygame.locals import *

class GameDefinitions():
    """
    定数を記載。
    TODO: 外だし
          設定ファイル化
    """
    def display_size(self):
        return (400, 400)

    def display_caption(self):
        return 'Reversi'

class Game():
    def __init__(self):
        definitions = GameDefinitions()
        pygame.init()
        pygame.screen = \
            pygame.display.set_mode(definitions.display_size())
        pygame.display.set_caption(definitions.display_caption())

    def __is_winner(self):
        # TODO implemented yet
        raise NotImplementedError

    def board(self):
        # TODO implemented yet
        raise NotImplementedError

    def score(self):
        # TODO implemented yet
        raise NotImplementedError

    def stone(self):
        # TODO implemented yet
        raise NotImplementedError

    def player(self):
        # TODO implemented yet
        raise NotImplementedError

    def enemy(self):
        # TODO implemented yet
        raise NotImplementedError
