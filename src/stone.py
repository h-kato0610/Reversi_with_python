class Stone:
    def __init__(self, x, y, w, h, stone_color):
        self.__elipse = None

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_black = None
        self.stone_color = stone_color
        
    def reverce(self):
        if self.is_black is True:
            self.is_black = False

    def create_stone(self):
        x = 1 * self.x * self.w
        y = 1 * self.y * self.w
        w = self.x + self.w
        h = self.y + self.h
        self.__elipse = (x, y, w, h)

    def draw_stone(self, pygame, screen, color=None):
        color = self.stone_color['stone_black_color'] if self.is_black else self.stone_color['stone_white_color']
        
        pygame.draw.ellipse(screen, color, self.__elipse)