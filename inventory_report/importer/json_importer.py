from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.__contains__(".json"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            return list(json.load(file))
