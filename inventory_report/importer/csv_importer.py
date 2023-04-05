from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        with open(path) as file:
            return list(csv.DictReader(file, delimiter=",", quotechar='"'))
