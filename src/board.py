import pygame

from stone import Stone

from pygame.locals import *

class Board:
    def __init__(self, x, y, w, h, stone_arg):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.__rect = None
        self.stone = Stone(self.x, self.y, self.w, self.h, stone_arg)
        
    def create_board(self):
        x = 1 * self.x * self.w
        y = 1 * self.y * self.w
        w = self.x + self.w
        h = self.y + self.h
        self.__rect = (x, y, w, h)

    def draw_square(self, pygame, screen, color):
        return pygame.draw.rect(screen, color, self.__rect, width=1)

    def put(self, pygame, screen, is_black):
        self.stone.is_black = is_black

        self.stone.create_stone()
        self.stone.draw_stone(pygame, screen)

    def update_board(self):
        raise NotImplementedError