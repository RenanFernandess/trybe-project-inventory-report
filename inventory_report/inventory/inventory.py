from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, type: str = "simples"):
        path_len = len(path)
        if path[-4:path_len] == ".csv":
            products = CsvImporter.import_data(path=path)
        elif path[-5:path_len] == ".json":
            products = JsonImporter.import_data(path=path)
        else:
            products = XmlImporter.import_data(path=path)

        if type == "completo":
            return CompleteReport.generate(products)
        return SimpleReport.generate(products)
