import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if ".xml" not in file_path:
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            file_content = [
                data
                for data in xmltodict.parse(file.read())["dataset"]["record"]
            ]
            return file_content
