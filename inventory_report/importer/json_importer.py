from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        with open(path) as file:
            return list(json.load(file))
