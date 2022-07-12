import pygame
import sys
import pathlib

from board import Board
from definitions import Definitions
from file_reader_for_toml import FileReaderForToml as fr_toml

from pygame.locals import *

SETTING_PATH = 'setting/'
SETTING_FILENAME = 'setting.toml'

class Game:
    def __init__(self):
        tmp = fr_toml()
        tmp.set_file_path(pathlib.Path(SETTING_PATH + SETTING_FILENAME))
        self.settings = tmp.get_contents()

        definition_file_path = pathlib.Path(\
            self.settings['definition_file']['directory'] + \
            self.settings['definition_file']['file_name'])
        self.definitions = Definitions(definition_file_path)

        pygame.init()
        self.screen = \
            pygame.display.set_mode(self.definitions.get_display_size())
        pygame.display.set_caption(self.definitions.get_display_caption())

        self.__start()

    def __start(self):
        # 背景色をRGBAで指定。
        self.screen.fill(self.definitions.get_display_background_color())

        boards = self.__initialize_board(pygame)
        square_color = self.definitions.get_square_color()

        for board in boards:
            [i.draw_square(pygame, self.screen, square_color) for i in board]

        while(True):
            # ミリ秒での更新間隔。
            pygame.time.wait(self.definitions.get_display_time_wait())
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

    def __initialize_board(self, pygame):
        one_line = self.definitions.get_one_line()
        square_width = self.definitions.get_square_width()
        square_height = self.definitions.get_square_height()
        stone_color = self.definitions.get_stone_color()
        boards = []
        for y in range(one_line):
            tmp_list = []
            for x in range(one_line):
                tmp_board = Board(x, y, square_width, square_height, stone_color)
                tmp_board.create_board()
                tmp_list.append(tmp_board)
            boards.append(tmp_list)

        # initialize_position_board
        init_pos_black1 = (4, 3)
        init_pos_white1 = (3, 3)
        init_pos_black2 = (3, 4)
        init_pos_white2 = (4, 4)

        is_black = True
        boards[init_pos_black1[0]][init_pos_black1[1]].put(pygame, self.screen, is_black)
        boards[init_pos_white1[0]][init_pos_white1[1]].put(pygame, self.screen, not is_black)
        boards[init_pos_black2[0]][init_pos_black2[1]].put(pygame, self.screen, is_black)
        boards[init_pos_white2[0]][init_pos_white2[1]].put(pygame, self.screen, not is_black)
        
        return boards

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
