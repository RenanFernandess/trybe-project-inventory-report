from inventory_report.reports.simple_report import SimpleReport
from datetime import datetime


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list[dict]):
        manufacturing_dates = list()
        expiration_dates = list()
        company_with_quantity_products = dict()
        for product in products:
            manufacturing_dates.append(
                datetime.strptime(
                    product["data_de_fabricacao"], "%Y-%m-%d"
                ).strftime("%Y-%m-%d")
            )
            expiration_dates.append(
                datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
            )
            try:
                company_with_quantity_products[product["nome_da_empresa"]] += 1
            except KeyError:
                company_with_quantity_products[product["nome_da_empresa"]] = 1

        company_with_more_products = sorted(
            list(company_with_quantity_products.items()),
            key=lambda i: i[1],
            reverse=True,
        )

        nearest_expiration_date = min(
            expiration_dates, key=lambda i: abs(i - datetime.now())
        ).strftime("%Y-%m-%d")

        stock = str()
        for item in company_with_more_products:
            stock += f"- {item[0]}: {item[1]}\n"
        return (
            f"Data de fabricação mais antiga: {min(manufacturing_dates)}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products[0][0]}\n"
            f"Produtos estocados por empresa:\n" + stock
        )
