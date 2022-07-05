import pygame

from pygame.locals import *

class Board:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = None
        self.white_or_black = None
        
    def __put_initialize_potition(self):
        raise NotImplementedError

    def create_board(self, pygame, screen, color):
        self.rect = pygame.Rect(self.x, self.y, self.x * self.w, self.y * self.h)
        screen.fill(color, self.rect)

    def update_board(self):
        raise NotImplementedError

    def draw_board(self):
        return self.rect

    def put(self):
        raise NotImplementedError