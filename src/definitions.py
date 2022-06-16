
class GameDefinitions():
    """
    定数を記載。
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

