import pygame
from pygame.locals import *

class GameDefinitions():
    """
    定数を記載。
    TODO: 外だし
          設定ファイル化
    """
    def display_size():
        return (400, 400)

    def display_caption():
        return 'Reversi'

class Game():
    def __init__(self):
        definitions = GameDefinitions()
        pygame.init()
        pygame.screen = \
            pygame.display.set_mode(definitions.display_size)
        pygame.display.set_caption(definitions.captions)

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
        # TODO implemented yetする
        return None

    def player(self):
        # TODO implemented yet
        return None

    def enemy(self):
        # TODO implemented yet
        return None
