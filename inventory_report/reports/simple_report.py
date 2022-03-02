from abc import ABC, abstractmethod
import json

# metodo generate recebe uma lista de dict (dicionarios) e retorna string formatada como relatorio


class SimpleReport(ABC):
    def __init__(self, export_file):
        self.export_file = export_file

    @abstractmethod
    def generate(self):
        raise NotImplementedError


class reportJSON(SimpleReport):
    def generate(self):
        with open(self.export_file) as file:
            inventory_list = json.load(file)
            return list(inventory_list)

            # for item in inventory_list:
            #     return list(item["nome_do_produto"])
            # json.dump(file)
            # return list(file)
            # return (
            #     f"Data de fabricação mais antiga: YYYY-MM-DD {file}\n"
            #     "Data de validade mais próxima: YYYY-MM-DD\n"
            #     "Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA\n"
            # )


teste = reportJSON("inventory_report/data/inventory.json")
print(teste.generate())
