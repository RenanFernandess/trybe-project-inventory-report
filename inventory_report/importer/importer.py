from abc import ABC, abstractmethod


class Importer(ABC):
    @abstractmethod
    @classmethod
    def import_data(cls, path: str):
        raise NotImplementedError
