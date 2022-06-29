from abc import ABCMeta, abstractmethod

class FileReader(metaclass=ABCMeta):
    def __init__(self):
        self._file_path = ''
        self._contents = ''

    @abstractmethod
    def set_file_path(self, file_path):
        raise NotImplementedError()

    @abstractmethod
    def get_contents(self):
        raise NotImplementedError()
