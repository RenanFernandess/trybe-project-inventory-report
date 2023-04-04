# from inventory_report.inventory.product import Product
from inventory_report.inventory.product import Product


def test_cria_produto():
    """Test whether the Product class has the required attributes"""
    borracha = Product(
        nome_do_produto="Borracha",
        id=1,
        nome_da_empresa="Papelaria Solar",
        data_de_fabricacao="2021-07-04",
        data_de_validade="2029-02-09",
        numero_de_serie="FR48",
        instrucoes_de_armazenamento="Ao abrigo de luz solar",
    )

    assert borracha.id == 1
    assert borracha.nome_do_produto == "Borracha"
    assert borracha.nome_da_empresa == "Papelaria Solar"
    assert borracha.numero_de_serie == "FR48"
    assert borracha.data_de_fabricacao == "2021-07-04"
    assert borracha.data_de_validade == "2029-02-09"
    assert borracha.instrucoes_de_armazenamento == "Ao abrigo de luz solar"
