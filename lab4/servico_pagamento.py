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