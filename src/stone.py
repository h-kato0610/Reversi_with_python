class Stone:
    def __init__(self):
        self.is_black = None
        
    def reverce(self):
        if self.is_black is True:
            self.is_black = False