from file_reader_for_toml import FileReaderForToml as fr_toml

class Definitions:
    def __init__(self, definition_file_path):
        tmp = fr_toml()
        tmp.set_file_path(definition_file_path)
        self.definition_file = tmp.get_contents()

    def get_display_caption(self):
        caption = self.definition_file['game']['display_caption']
        return caption

    def get_display_size(self):
        display_size = self.definition_file['game']['display_size']
        width = int(display_size['width'])
        height = int(display_size['height'])
        return (width, height)

    def get_display_background_color(self):
        background_color = \
            self.definition_file['game']['display_background_color']
        red = int(background_color['red'])
        green = int(background_color['green'])
        blue = int(background_color['blue'])
        alpha = int(background_color['alpha'])
        return (red, green, blue, alpha)

    def get_display_time_wait(self):
        time = int(self.definition_file['game']['display_time_wait'])
        return time

    def get_all_square(self):
        square = int(self.definition_file['board']['all_square'])
        return square

    def get_one_line(self):
        one_line = int(self.definition_file['board']['one_line'])
        return one_line

    def get_square_width(self):
        square_width = int(self.definition_file['board']['square']['width'])
        return square_width

    def get_square_height(self):
        square_height = int(self.definition_file['board']['square']['height'])
        return square_height

    def get_square_color(self):
        background_color = \
            self.definition_file['board']['square_color']
        red = int(background_color['red'])
        green = int(background_color['green'])
        blue = int(background_color['blue'])
        alpha = int(background_color['alpha'])
        return (red, green, blue, alpha)

    def get_stone_span(self):
        stone_span = float(self.definition_file['stone']['span'])
        return stone_span

    def get_stone_color(self):
        stone_black_color = self.definition_file['stone']['black']
        stone_white_color = self.definition_file['stone']['white']

        stone_color = {
            'stone_black_color' : (stone_black_color['red'], stone_black_color['green'], stone_black_color['blue']),
            'stone_white_color' : (stone_white_color['red'], stone_white_color['green'], stone_white_color['blue'])
        }
        
        return stone_color