import pygame
import sys

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
        self.screen = pygame.screen = \
            pygame.display.set_mode(definitions.display_size())
        pygame.display.set_caption(definitions.display_caption())

        self.start()

    def start(self):
        while(True):
            # 背景色をRGBAで指定。
            self.screen.fill((0, 0, 0, 0))
            # ミリ秒での更新間隔。
            pygame.time.wait(30)
            pygame.display.update()

            # 終了処理
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

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
