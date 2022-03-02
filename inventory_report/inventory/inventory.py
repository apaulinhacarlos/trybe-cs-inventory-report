import csv
import json

# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
import xmltodict

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

    @classmethod
    def read_json(cls, file_path, report_type):
        with open(file_path) as file:
            file_content = json.load(file)
            if report_type == "simples":
                return SimpleReport.generate(file_content)
            elif report_type == "completo":
                return CompleteReport.generate(file_content)

    @classmethod
    def read_xml(cls, file_path, report_type):
        with open(file_path) as file:
            file_content = [
                data
                for data in xmltodict.parse(file.read())["dataset"]["record"]
            ]
            if report_type == "simples":
                return SimpleReport.generate(file_content)
            elif report_type == "completo":
                return CompleteReport.generate(file_content)

    @classmethod
    def import_data(cls, file_path, report_type):
        if ".csv" in file_path:
            return cls.read_csv(file_path, report_type)
        elif ".json" in file_path:
            return cls.read_json(file_path, report_type)
        elif ".xml" in file_path:
            return cls.read_xml(file_path, report_type)
