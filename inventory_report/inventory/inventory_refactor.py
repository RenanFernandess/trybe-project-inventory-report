from inventory_report.importer.importer import Importer
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer: Importer) -> None:
        self.importer = importer
        self.data = list()

    def import_data(self, path: str, type: str = "simples"):
        self.data += self.importer.import_data(path=path)
        if type == "completo":
            return CompleteReport.generate(self.data)
        return SimpleReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
