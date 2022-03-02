import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def read_csv(cls, file_path, report_type):
        with open(file_path) as file:
            file_content = [data for data in csv.DictReader(file)]
            if report_type == "simples":
                return SimpleReport.generate(file_content)
            elif report_type == "completo":
                return CompleteReport.generate(file_content)
            return list(file_content)

    @classmethod
    def read_json(cls, file_path, report_type):
        with open(file_path) as file:
            file_content = [data for data in json.load(file)]
            if report_type == "simples":
                return SimpleReport.generate(file_content)
            elif report_type == "completo":
                return CompleteReport.generate(file_content)
            return list(file_content)

    @classmethod
    def import_data(cls, file_path, report_type):
        if ".csv" in file_path:
            return cls.read_csv(file_path, report_type)
        elif ".json" in file_path:
            return cls.read_json(file_path, report_type)
