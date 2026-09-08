# Banco de dados simulado do estoque
estoque = {
    "101": {"nome": "Teclado USB", "preco": 100.0, "qtd": 10},
    "102": {"nome": "Mouse Óptico", "preco": 50.0, "qtd": 3},
    "103": {"nome": "Monitor 24'", "preco": 800.0, "qtd": 0}
}

def processar_venda(cod_prod, qtd_desejada):
    prod = estoque.get(cod_prod)

    if not prod:
        print("Erro: Produto não encontrado!")
        return

    # Manutenção corretiva: valida a quantidade solicitada.
    if qtd_desejada <= 0:
        print("Erro: A quantidade da venda deve ser maior que zero.")
        return

    if qtd_desejada > prod["qtd"]:
        print(
            f"Erro: Estoque insuficiente! "
            f"Disponível: {prod['qtd']} unidade(s)."
        )
        return

    prod["qtd"] -= qtd_desejada
    total = prod["preco"] * qtd_desejada
    print(f"Venda concluída! Total: R$ {total:.2f}")


def emitir_nota(cod_prod, qtd):
    prod = estoque.get(cod_prod)

    if prod:
        total = prod["preco"] * qtd
        imposto = total * 0.10
        valor_final = total + imposto

        print("--- NOTA FISCAL ---")
        print(f"Produto: {prod['nome']} | Qtd: {qtd}")
        print(f"Subtotal: R$ {total:.2f}")
        print(f"Imposto (10%): R$ {imposto:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")
        print("-------------------")
    else:
        print("Erro: Produto não encontrado!")


def repor_estoque(cod_prod, qtd):
    prod = estoque.get(cod_prod)

    if not prod:
        print("Erro: Produto não encontrado!")
        return

    if qtd <= 0:
        print("Erro: A quantidade para reposição deve ser maior que zero.")
        return

    prod["qtd"] += qtd
    print(
        f"Estoque reposto com sucesso! "
        f"Quantidade atual: {prod['qtd']} unidade(s)."
    )


# Execução de teste
processar_venda("101", 2)
emitir_nota("101", 2)
repor_estoque("103", 5)
