import pygame

from pygame.locals import *

class Board:
    def __init__(self, x, y, w, h, b):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.b = b
        self.position = None
        self.white_or_black = None
        
    def __put_initialize_potition(self):
        raise NotImplementedError

    def create_board(self):
        x = 1 * self.x * self.w
        y = 1 * self.y * self.w
        w = self.x + self.w
        h = self.y + self.h
        self.position = (x, y, w, h)

    def update_board(self):
        raise NotImplementedError

    def draw_square(self, pygame, screen, color):
        return pygame.draw.rect(screen, color, self.position)

    def put(self):
        raise NotImplementedError