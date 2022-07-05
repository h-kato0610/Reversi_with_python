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
        all_square = int(self.definition_file['game']['all_square'])
        return all_square