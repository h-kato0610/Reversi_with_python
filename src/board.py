import pygame

from pygame.locals import *

# TODO to deffile
WIDTH = 100
HEIGHT = 100
COLOR = (0, 255, 0, 0)

class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.white_or_black = None
        
    def __initialize_board(self):
        raise NotImplementedError

    def create_board(self, pygame, screen):
        raise NotImplementedError

    def update_board(self):
        raise NotImplementedError

    def draw_board(self, pygame, screen, r):
        raise NotImplementedError

    def put(self):
        raise NotImplementedError