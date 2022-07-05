class Stone:
    def __init__(self, x, y, w, h, stone_arg):
        self.__elipse = None

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_black = None
        self.stone_span = stone_arg['stone_span']
        self.stone_color = stone_arg['stone_color']
        
    def reverce(self):
        if self.is_black is True:
            self.is_black = False

    def create_stone(self):
        # FIXME: Stoneはうまく計算できていない。今後の課題
        self.__elipse = (self.x, self.y, self.w - self.stone_span, self.h - self.stone_span)

    def draw_stone(self, pygame, screen, color=None):
        color = self.stone_color['stone_black_color'] if self.is_black else self.stone_color['stone_white_color']
        
        # pygame.draw.ellipse(screen, color, self.__elipse)
        pygame.draw.ellipse(screen, color, self.__elipse)