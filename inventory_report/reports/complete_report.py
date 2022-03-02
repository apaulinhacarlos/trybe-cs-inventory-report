from inventory_report.reports.simple_report import SimpleReport

# subclasse de dict para contar objetos hasheáveis
# https://docs.python.org/pt-br/3/library/collections.html#collections.Counter
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def products_stocked_by_company(cls, dict_list):
        companies = Counter(
            [company["nome_da_empresa"] for company in dict_list]
        ).items()

        amount_of_products_formatted = ""
        for company, quantity in companies:
            amount_of_products_formatted += f"- {company}: {quantity}\n"

        return amount_of_products_formatted

    @classmethod
    def generate(cls, dict_list):
        return (
            f"{SimpleReport.generate(dict_list)}\n"
            "Produtos estocados por empresa: \n"
            f"{cls.products_stocked_by_company(dict_list)}"
        )
