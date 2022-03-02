import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        if ".csv" not in file_path:
            raise ValueError("Arquivo inválido")

        with open(file_path) as file:
            file_content = [data for data in csv.DictReader(file)]
            return file_content
