# Lab 3: Organização do Trabalho — PDCA, Checklist e Gestão de Manutenção 📋🔄

Neste laboratório, você aprenderá a aplicar metodologias de organização do trabalho técnico. Utilizaremos o **Ciclo PDCA (Plan, Do, Check, Act)** e um **Checklist de Manutenção** para estruturar a resolução de um problema de software de forma profissional e auditável.

---

## 📚 Resumo do Conteúdo da Aula

A manutenção de sistemas não pode ser realizada de forma desorganizada ou impulsiva ("Gambiarras"). Para garantir a estabilidade do produto, a equipe de engenharia utiliza metodologias de gestão e ferramentas de acompanhamento.

### 1. Ferramentas de Gerenciamento
* **Sistemas de Chamados/Tickets (ex: Jira, Trello, Redmine):** Organizam as solicitações de manutenção por prioridade, responsável e status (A Fazer, Em Progresso, Em Teste, Concluído).
* **Quadros Kanban:** Visualização do fluxo de trabalho para evitar gargalos na equipe.

### 2. O Ciclo PDCA na Manutenção de Software
* 📌 **Plan (Planejar):** Identificar o problema, analisar as causas raiz, definir a meta e criar o plano de ação.
* 🛠️ **Do (Executar):** Realizar as alterações no código e aplicar as correções conforme planejado.
* 🔍 **Check (Checar/Verificar):** Executar bateria de testes para validar se o problema foi resolvido sem gerar novos bugs (Testes de Regressão).
* 🔄 **Act (Agir/Padronizar):** Documentar o processo, atualizar procedimentos e aplicar lições aprendidas para evitar reincidência.

### 3. Roteiro de Trabalho (Checklist)
O checklist é uma ferramenta simples e poderosa para evitar que passos cruciais de segurança e qualidade sejam esquecidos durante a manutenção.

---

## 💻 Atividade Prática: O Caso do Bug do Carrinho de Compras

A equipe de suporte recebeu múltiplos chamados informando que o sistema de vendas está aplicando descontos indevidos e permitindo fechar pedidos zerados. 

### Código com Problemas de Organização (`carrinho.py`):

```python
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
```

---

## 🎯 Desafio Prático: Aplicando o Ciclo PDCA e Checklist

Você atuará como o líder técnico responsável por organizar a resolução deste chamado seguindo rigorosamente as 4 etapas do PDCA e preenchendo um checklist de validação.

### Tarefa 1: Elaborar o Documento PDCA
Crie um arquivo de texto chamado `PDCA_chamado_104.txt` (ou inclua no e-mail) preenchendo as seções abaixo:

* **P (Plan):** Descreva o problema encontrado no arquivo `carrinho.py`, o risco comercial e qual a regra correta (o valor final nunca pode ser menor que R$ 0.00).
* **D (Do):** Descreva qual alteração lógica foi feita na função `calcular_total_carrinho`.
* **C (Check):** Liste 3 cenários de teste executados (ex: cupom válido, cupom maior que o total, sem cupom).
* **A (Act):** Descreva a ação tomada para padronizar essa regra (ex: inclusão da regra no checklist de código do time).

### Tarefa 2: Aplicar o Checklist de Manutenção
Antes de enviar o código, verifique se ele cumpre todos os itens do checklist:

- [ ] **Item 1:** A função não permite totais de pedidos negativos (retorna no mínimo 0.0).
- [ ] **Item 2:** O código não possui imports ou variáveis sem uso.
- [ ] **Item 3:** Foram adicionados comentários explicativos nas novas regras.
- [ ] **Item 4:** Todos os testes de verificação executaram com sucesso.

### Tarefa 3: Implementar a Solução
Crie o arquivo `carrinho_corrigido.py` aplicando a regra de negócio correta e as validações necessárias.

---

## 📬 Instruções para Entrega

Envie para o e-mail: **`eduardo.hernandes@docente.senai.br`**

1. **Anexo 1:** O arquivo do documento PDCA (`PDCA_chamado_104.txt`).
2. **Anexo 2:** O arquivo do código Python corrigido (`carrinho_corrigido.py`).
3. **Assunto do e-mail:** `[Manutenção de Sistemas] Entrega Lab 3 - <Seu Nome Completo>`

## Slide
[Apresentação](https://docs.google.com/presentation/d/1M99ckKJr4QWhAMWNW8tHOpepRTx5-s95G_YVTTTYZQY/edit?usp=sharing)

