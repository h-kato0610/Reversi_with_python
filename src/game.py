import pygame
import sys
import pathlib

from file_reader_for_toml import FileReaderForToml as fr_toml

from pygame.locals import *

SETTING_PATH = 'setting/'
SETTING_FILENAME = 'setting.toml'

class GameDefinitions():
    """
    定数を記載。
    TODO: 外だし
          設定ファイル化
    """
    def display_size(self):
        width = 1200
        # 30pxはメニューの領域を想定
        height = 630
        return (width, height)

    def display_caption(self):
        return 'Reversi'

    def background_color(self):
        r = 0
        g = 0
        b = 0
        a = 0
        return (r, g, b, a)

    def time_wait(self):
        fps = 30
        return fps

class Game():
    def __init__(self):
        self.settings = fr_toml()
        self.settings.set_file_path(pathlib.Path(SETTING_PATH + SETTING_FILENAME))
        self.settings.load_file()

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
                    self.__end()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.__end()

    def __restart(self):
        # TODO implemented yet
        raise NotImplementedError

    def __end(self):
        pygame.quit()
        sys.exit()

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
