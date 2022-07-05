class Stone:
    def __init__(self, x, y, w, h, stone_span):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.is_black = None
        self.stone_span = stone_span
        
    def reverce(self):
        if self.is_black is True:
            self.is_black = False

    def create_stone(self):
        'hoge'

    def draw_stone(self, pygame, screen, color=None):
        # FIXME: Stoneはうまく計算できていない。今後の課題
        pygame.draw.ellipse(screen, (255, 255, 255), (self.x, self.y, self.w - self.stone_span, self.h - self.stone_span))