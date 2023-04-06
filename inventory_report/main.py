from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
import sys


def main():
    try:
        _, path, type = sys.argv

        if path.__contains__(".csv"):
            Importer = InventoryRefactor(CsvImporter)
        elif path.__contains__(".json"):
            Importer = InventoryRefactor(JsonImporter)
        else:
            Importer = InventoryRefactor(XmlImporter)

        sys.stdout.write(Importer.import_data(path, type))
    except ValueError:
        sys.stderr.write("Verifique os argumentos\n")
