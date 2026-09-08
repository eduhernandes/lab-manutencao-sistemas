# Lab 1: Tipos de Manutenção de Software 🔧

Este laboratório aborda os conceitos fundamentais sobre **Manutenção de Sistemas** e a aplicação prática dos diferentes tipos de manutenção utilizando a linguagem Python.

---

## 📚 Resumo do Conteúdo da Aula

A manutenção de software não consiste apenas em corrigir problemas. Ela engloba todas as atividades realizadas após a entrega de um sistema para manter seu funcionamento, evoluir suas funcionalidades e garantir sua qualidade.

### Os 5 Tipos de Manutenção de Software

1. 🔴 **Manutenção Corretiva:** Realizada para corrigir bugs, falhas de execução e erros existentes no sistema.

2. 🟢 **Manutenção Preventiva:** Tem como objetivo evitar problemas futuros por meio de limpeza de código, atualizações e testes preliminares.

3. 🔵 **Manutenção Adaptativa:** Adequa o sistema quando ocorrem mudanças no ambiente externo, como novas leis, atualizações de sistemas operacionais, bancos de dados ou APIs.

4. 🟣 **Manutenção Evolutiva:** Consiste na adição de novas funcionalidades e recursos que não existiam anteriormente no sistema.

5. ⚡ **Manutenção Perfectiva:** Busca melhorar a qualidade interna do software, como desempenho, organização, refatoração e facilidade de manutenção, sem alterar a regra de negócio.

---

## 💻 Código Base

O laboratório utiliza um sistema simplificado de **gestão de estoque e vendas** desenvolvido em Python.

O sistema possui:

* Cadastro simulado de produtos;
* Processamento de vendas;
* Emissão de notas fiscais;
* Controle de quantidade em estoque.

O código original apresentava problemas de validação, lentidão proposital e limitações funcionais que deveriam ser solucionados através de diferentes tipos de manutenção.

---

## 🎯 Desafios Propostos

Foram realizadas quatro intervenções principais no sistema:

### 🔴 1. Manutenção Corretiva

A função `processar_venda()` permitia:

* Venda de quantidade igual a zero;
* Venda de quantidade negativa;
* Venda de uma quantidade superior ao estoque disponível.

Foi adicionada uma validação para impedir essas situações.

#### Alteração realizada

```python
if qtd_desejada <= 0:
    print("Erro: A quantidade da venda deve ser maior que zero.")
    return

if qtd_desejada > prod["qtd"]:
    print(
        f"Erro: Estoque insuficiente! "
        f"Disponível: {prod['qtd']} unidade(s)."
    )
    return
```

Essa alteração garante que uma venda somente seja realizada quando a quantidade solicitada for válida e estiver disponível no estoque.

---

### ⚡ 2. Manutenção Perfectiva

O código original possuía um laço `for` utilizado apenas para simular lentidão:

```python
for _ in range(10000000):
    pass
```

Esse trecho não possuía nenhuma função para o sistema e prejudicava o desempenho da aplicação.

Ele foi removido para tornar o processamento da venda mais rápido e eficiente.

---

### 🔵 3. Manutenção Adaptativa

O sistema precisou ser adaptado a uma mudança na legislação fiscal.

Foi estabelecida uma taxa obrigatória de **10% de imposto** sobre o valor da venda.

A função `emitir_nota()` foi modificada para apresentar:

* Subtotal;
* Valor do imposto;
* Valor final da venda.

#### Alteração realizada

```python
total = prod["preco"] * qtd
imposto = total * 0.10
valor_final = total + imposto
```

A nota fiscal passou a apresentar:

```text
--- NOTA FISCAL ---
Produto: Teclado USB | Qtd: 2
Subtotal: R$ 200.00
Imposto (10%): R$ 20.00
Valor final: R$ 220.00
-------------------
```

---

### 🟣 4. Manutenção Evolutiva

Foi solicitada pelo gerente uma nova funcionalidade para permitir a reposição do estoque.

Foi criada a função:

```python
repor_estoque(cod_prod, qtd)
```

A função permite adicionar novas unidades a um produto existente.

Também foram adicionadas validações para impedir:

* Reposição de produto inexistente;
* Reposição com quantidade zero;
* Reposição com quantidade negativa.

#### Exemplo

```python
repor_estoque("103", 5)
```

Resultado:

```text
Estoque reposto com sucesso! Quantidade atual: 5 unidade(s).
```

---

## 🧪 Testes Realizados

Foram utilizados testes para verificar o funcionamento das alterações.

### Teste de venda

```python
processar_venda("101", 2)
```

Resultado esperado:

```text
Venda concluída! Total: R$ 200.00
```

### Teste de emissão da nota

```python
emitir_nota("101", 2)
```

Resultado esperado:

```text
--- NOTA FISCAL ---
Produto: Teclado USB | Qtd: 2
Subtotal: R$ 200.00
Imposto (10%): R$ 20.00
Valor final: R$ 220.00
-------------------
```

### Teste de reposição

```python
repor_estoque("103", 5)
```

Resultado esperado:

```text
Estoque reposto com sucesso! Quantidade atual: 5 unidade(s).
```

---

## 📊 Resumo das Manutenções

| Tipo          | Função/Trecho       | Alteração realizada                  |
| ------------- | ------------------- | ------------------------------------ |
| 🔴 Corretiva  | `processar_venda()` | Validação da quantidade e estoque    |
| ⚡ Perfectiva  | `processar_venda()` | Remoção do laço que causava lentidão |
| 🔵 Adaptativa | `emitir_nota()`     | Inclusão de imposto de 10%           |
| 🟣 Evolutiva  | `repor_estoque()`   | Nova funcionalidade de reposição     |

---

## 📁 Estrutura do Projeto

```text
lab1-daviraposo/
│
├── README.md
│
└── sistema_loja_resolvido.py
```

### Arquivos

**`README.md`**
Documentação do laboratório, contendo o objetivo, conceitos, alterações e testes realizados.

**`sistema_loja_resolvido.py`**
Código Python contendo as quatro intervenções de manutenção solicitadas.

---

## 📌 Conclusão

A atividade demonstrou que a manutenção de software possui diferentes objetivos e não se limita à correção de bugs.

No sistema desenvolvido foram aplicadas quatro categorias diferentes:

* **Corretiva**, para solucionar problemas nas vendas;
* **Perfectiva**, para melhorar o desempenho;
* **Adaptativa**, para adequar o sistema à nova regra fiscal;
* **Evolutiva**, para adicionar a funcionalidade de reposição de estoque.

Dessa forma, foi possível aplicar na prática diferentes estratégias de manutenção em um sistema desenvolvido em Python.

---

### Assunto

```text
[Manutenção de Sistemas] Entrega Lab 1 - Davi Raposo
```
