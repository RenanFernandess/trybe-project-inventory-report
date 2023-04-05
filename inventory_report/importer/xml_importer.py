from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.__contains__(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]
