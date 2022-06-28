import pathlib

from file_reader_for_toml import FileReaderForToml as fr_toml

class Definitions():
    def __init__(self, definition_file_path):
        self.definitioin_file = fr_toml()
        self.definitioin_file.set_file_path(pathlib.Path(definition_file_path))
        self.definitioin_file.load_file()

    def get_game_definitions():
        if display_size:
            width = int(self.definitioin_file['Game']['display_size']['width'])
            height = int(self.definitioin_file['Game']['display_size']['height'])
            return 
        return self.definitioin_file['Game']
