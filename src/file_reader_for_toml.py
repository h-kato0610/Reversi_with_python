import toml

from file_reader import FileReader

class FileReaderForToml(FileReader):
    def set_file_path(self, file_path):
        try:
            with open(file_path, encoding='utf8') as f:
                toml_file = toml.load(f)
                self._contents = toml_file
        except FileNotFoundError:
            raise FileNotFoundError(error_value)

    def get_contents(self):
        return self._contents
