import pygame

from stone import Stone

from pygame.locals import *

class Board:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = None
        self.stone = Stone()
        
    def create_board(self):
        x = 1 * self.x * self.w
        y = 1 * self.y * self.w
        w = self.x + self.w
        h = self.y + self.h
        self.rect = (x, y, w, h)

    def draw_square(self, pygame, screen, color):
        return pygame.draw.rect(screen, color, self.rect, width=1)

    def put(self, is_black):
        self.stone.is_black = is_black

    def update_board(self):
        raise NotImplementedError