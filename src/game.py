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
        width = 600
        # 30pxはメニューの領域を想定
        height = 430
        return (width, height)

    def display_caption(self):
        return 'Reversi'

    def background_color(self):
        return (0, 0, 0, 0)

    def time_wait(self):
        return 30

class Game():
    def __init__(self):
        self.definitions = GameDefinitions()
        pygame.init()
        self.screen = \
            pygame.display.set_mode(self.definitions.display_size())
        pygame.display.set_caption(self.definitions.display_caption())

        self.__start()

    def __start(self):
        while(True):
            # 背景色をRGBAで指定。
            self.screen.fill(self.definitions.background_color())
            # ミリ秒での更新間隔。
            pygame.time.wait(self.definitions.time_wait())
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

    def __restart(self):
        # TODO implemented yet
        raise NotImplementedError

    def __end(self):
        # TODO implemented yet
        raise NotImplementedError

    def __is_winner(self):
        # TODO implemented yet
        raise NotImplementedError

    def menu_bar(self):
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
