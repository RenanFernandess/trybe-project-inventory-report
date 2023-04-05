# from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    """Test if it is possible to colorize the report"""
    products = [
        {
            "id": "1",
            "nome_do_produto": "MESA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-05-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
        },
    ]
    colorful_simple_report = ColoredReport(SimpleReport).generate(products)
    colorful_complete_report = ColoredReport(CompleteReport).generate(products)

    assert colorful_simple_report == (
        "\x1b[32mData de fabricação mais antiga:\x1b[0m "
        + "\x1b[36m2022-05-04\x1b[0m\n"
        + "\x1b[32mData de validade mais próxima:\x1b[0m "
        + "\x1b[36m2023-02-09\x1b[0m\n"
        + "\x1b[32mEmpresa com mais produtos:\x1b[0m "
        + "\x1b[31mForces of Nature\x1b[0m"
    )
    assert colorful_complete_report == (
        "\x1b[32mData de fabricação mais antiga:\x1b[0m "
        + "\x1b[36m2022-05-04\x1b[0m\n"
        + "\x1b[32mData de validade mais próxima:\x1b[0m "
        + "\x1b[36m2023-02-09\x1b[0m\n"
        + "\x1b[32mEmpresa com mais produtos:\x1b[0m "
        + "\x1b[31mForces of Nature\x1b[0m\n"
        + "Produtos estocados por empresa:\n- Forces of Nature: 1\n"
    )
