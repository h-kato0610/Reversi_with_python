from file_reader_for_toml import FileReaderForToml as fr_toml

class Definitions():
    def __init__(self, definition_file_path):
        tmp = fr_toml()
        tmp.set_file_path(definition_file_path)
        tmp.load_file()
        self.definition_file = tmp.get_contents()

    def get_caption(self):
        caption = self.definitioin_file['game']['caption']['display_caption'])
        return caption

    def get_display_size(self):
        display_size = self.definitioin_file['game']['display_size']
        width = int(display_size['width'])
        height = int(display_size['height'])
        return (width, height)

    def get_background_color(self):
        background_color = self.definitioin_file['game']['background_color']
        red = int(backdound_color['red'])
        green = int(backdound_color['green'])
        blue = int(backdound_color['blue'])
        alpha = int(backdound_color['alpha'])
        return (red, green, blue, alpha)

    def get_fps(self):
        fps = int(self.definitions_file['game']['fps']['time'])
        return fps
