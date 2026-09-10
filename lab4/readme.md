# Lab 4: Organização do Ambiente, Ergonomia, Troubleshooting e Gestão Emocional em TI 🖥️🧘‍♂️

Neste laboratório, vamos abordar a **saúde física e mental do profissional de TI**, além de praticar métodos estruturados para a resolução de falhas técnicas críticas (**Troubleshooting**) sob pressão de tempo.

---

## 📚 Resumo do Conteúdo da Aula

Para sustentar uma carreira longa e produtiva em TI, o profissional precisa equilibrar a eficiência técnica com a preservação de sua saúde ocupacional e regulação emocional.

### 1. Organização do Ambiente e Ergonomia
O ambiente de trabalho em TI envolve longas jornadas de postura sentada e esforço repetitivo. A falta de cuidados ergonômicos pode causar lesões graves:
* **Riscos Físicos:** DORT/LER (Distúrbios Osteomusculares Relacionados ao Trabalho / Lesões por Esforço Repetitivo), fadiga visual (astenopia) e impactos auditivos.
* **Medidas Preventivas:**
  * **Postura:** Ajuste do monitor na altura dos olhos e manter cotovelos e joelhos em ângulos de 90°.
  * **Pausas Ativas:** Aplicação da regra 20-20-20 para visão (a cada 20 min, olhar para algo a 20 pés/6m por 20 segundos) e alongamentos regulares.

### 2. Método de Correção de Falhas (Troubleshooting)
Resolver problemas ("apagar incêndios") de forma impulsiva frequentemente gera novos bugs. O processo profissional de Troubleshooting segue 4 passos principais:
1. **Identificação e Diagnóstico:** Mapear o sintoma e ler logs do sistema.
2. **Isolamento da Causa Raiz:** Testar componentes isoladamente para encontrar a origem exata da falha.
3. **Aplicação da Correção/Patch:** Implementar a alteração necessária de forma controlada.
4. **Teste de Regressão e Documentação:** Confirmar que a falha sumiu sem quebrar outras funcionalidades e registrar o procedimento.

### 3. Regulação Emocional em Situações de Pressão
Trabalhar com sistemas fora do ar ("downtime") gera ansiedade e pressão da gestão. Manter a autoconfiança, a regulação emocional e o raciocínio lógico é indispensável para evitar decisões impulsivas e atitudes desorientadas no código.

---

## 💻 Parte 1: Pesquisa Guiada e Parecer Técnico (Atividade Teórica)

Você deverá realizar uma pesquisa objetiva utilizando a internet e montar um **parecer técnico via e-mail**.

### Diretrizes para envio do e-mail:
* **Para:** `eduardo.hernandes@docente.senai.br`
* **Assunto:** `[Pesquisa TI] Ergonomia, Troubleshooting e Gestão Emocional - [Seu Nome Completo]`
* **Corpo do E-mail:**
  * **Parte 1 (Ergonomia & Riscos):** Sintetize 2 medidas preventivas essenciais para evitar DORT/LER e a fadiga visual no ambiente de trabalho.
  * **Parte 2 (Método de Correção):** Cite os 4 passos principais de um método eficiente de Troubleshooting para atualizar e corrigir falhas sem gerar novos erros.
  * **Parte 3 (Reflexão Socioemocional):** Descreva em 3 a 5 linhas como você pretende regular suas emoções (manter a calma e a autoconfiança) quando estiver diante de um sistema fora do ar sob forte pressão de clientes/gestores.

---

## 🎯 Parte 2: Desafio Prático de Troubleshooting (Estudo de Caso Sob Pressão)

Você foi acionado para resolver uma falha crítica na API de um sistema de pagamento que interrompeu as operações da empresa. **Você tem um tempo limite para restaurar o serviço.**

### Código com Falha de Inicialização (`servico_pagamento.py`):

```python
# Módulo Crítico de Serviços de Pagamento

import time

# Configurações de Banco de Dados simuladas
CONFIG_BD = {
    "host": "localhost",
    "porta": 5432,
    "status_servico": "STOPPED", # ERRO: O serviço de banco está inativo
    "versao_minima": 2.0
}

VERSAO_SISTEMA = 1.5 # ERRO: Sistema defasado necessitando de atualização

def iniciar_servico_pagamento():
    print("Iniciando verificação do sistema de pagamentos...")
    
    # Validação 1: Versão do Sistema
    if VERSAO_SISTEMA < CONFIG_BD["versao_minima"]:
        raise SystemError(f"FALHA CRÍTICA: Versão do sistema ({VERSAO_SISTEMA}) incompatível. Requer versão {CONFIG_BD['versao_minima']} ou superior.")
    
    # Validação 2: Status da Dependência
    if CONFIG_BD["status_servico"] != "RUNNING":
        raise ConnectionError("FALHA CRÍTICA: O serviço de Banco de Dados de Pagamentos está inativo (STOPPED).")

    print("✅ Serviço de Pagamento iniciado com SUCESSO!")
    return True

# Tentativa de inicialização
if __name__ == "__main__":
    try:
        iniciar_servico_pagamento()
    except Exception as e:
        print(f"❌ ERRO ENCONTRADO AO INICIAR: {e}")
```

### Missão do Desafio:
1. Mantenha a calma, respire fundo e **não aja por impulso**.
2. Analise a mensagem do log de erro impressa no terminal.
3. Crie o arquivo `servico_pagamento_corrigido.py` aplicando as alterações necessárias (atualizando a versão do sistema e corrigindo a dependência do serviço).
4. Execute o script corrigido até obter a mensagem de sucesso `✅ Serviço de Pagamento iniciado com SUCESSO!`.

---

## 📬 Instruções para Entrega Final

1. **E-mail enviado:** Certifique-se de ter enviado o parecer técnico conforme a **Parte 1**.
2. **Anexo no e-mail (ou entrega local):** O arquivo de código corrigido `servico_pagamento_corrigido.py`.