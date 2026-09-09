# Módulo de Cálculo de Carrinho de Compras Legado

carrinho = [
    {"item": "Notebook", "preco": 3000.0, "qtd": 1},
    {"item": "Mouse", "preco": 50.0, "qtd": 2}
]

def calcular_total_carrinho(cupom_desconto=0):
    total = 0
    for item in carrinho:
        total += item["preco"] * item["qtd"]
    
    # PROBLEMA: Desconto é subtraído diretamente sem validar o valor mínimo do carrinho!
    total_final = total - cupom_desconto
    
    return total_final

# Execução atual
total_pedido = calcular_total_carrinho(cupom_desconto=5000.0)
print(f"Total a pagar: R$ {total_pedido:.2f}")  # Exibe R$ -1900.00 (Valor Negativo!)