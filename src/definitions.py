from file_reader_for_toml import FileReaderForToml as fr_toml

class Definitions():
    def __init__(self, definition_file_path):
        tmp = fr_toml()
        tmp.set_file_path(definition_file_path)
        tmp.load_file()
        self.definition_file = tmp.get_contents()

    def get_caption(self):
        caption = self.definitioin_file['game']['caption'])
        return caption

    def get_display_size(self):
        width = int(self.definitioin_file['game']['display_size']['width'])
        height = int(self.definitioin_file['game']['display_size']['height'])
        return (width, height)
