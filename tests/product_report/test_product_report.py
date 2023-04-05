# from inventory_report.inventory.product import Product
from inventory_report.inventory.product import Product


def test_relatorio_produto():
    """Test that the report is generated in the correct format"""
    borracha = Product(
        nome_do_produto="Borracha",
        id=1,
        nome_da_empresa="Papelaria Solar",
        data_de_fabricacao="2021-07-04",
        data_de_validade="2029-02-09",
        numero_de_serie="FR48",
        instrucoes_de_armazenamento="Ao abrigo de luz solar",
    )

    assert str(borracha) == (
        "O produto Borracha"
        + " fabricado em 2021-07-04"
        + " por Papelaria Solar com validade"
        + " até 2029-02-09"
        + " precisa ser armazenado Ao abrigo de luz solar."
    )
