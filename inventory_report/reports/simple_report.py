from datetime import datetime

# Método que retorna o valor mais comum de dados discretos ou nominais.
# https://docs.python.org/3/library/statistics.html#statistics.mode
from statistics import mode


class SimpleReport:
    @classmethod
    def earliest_manufacturing_date(cls, dict_list):
        min_date = min(
            [
                datetime.fromisoformat(product["data_de_fabricacao"])
                for product in dict_list
            ]
        )
        return min_date.date()

    @classmethod
    def closest_expiration_date(cls, dict_list):
        current_date = datetime.now()
        min_date = min(
            [
                datetime.fromisoformat(product["data_de_validade"])
                for product in dict_list
                if datetime.fromisoformat(product["data_de_validade"])
                > current_date
            ]
        )
        return min_date.date()

    @classmethod
    def company_with_the_largest_amount_of_products_stocked(cls, dict_list):
        return mode([product["nome_da_empresa"] for product in dict_list])

    @classmethod
    def generate(cls, dict_list):
        company = cls.company_with_the_largest_amount_of_products_stocked(
            dict_list
        )
        return (
            "Data de fabricação mais antiga: "
            f"{cls.earliest_manufacturing_date(dict_list)}\n"
            "Data de validade mais próxima: "
            f"{cls.closest_expiration_date(dict_list)}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{company}\n"
        )
