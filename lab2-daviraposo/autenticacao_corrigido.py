"""Módulo de autenticação corrigido.

Implementa armazenamento seguro de senhas usando PBKDF2-HMAC com salt
individual e registra tentativas de autenticação.
"""

import hashlib
import hmac
import logging
import secrets


# Configuração básica de logs.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Banco de usuários de exemplo.
# Em uma aplicação real, esses dados devem ser persistidos em um banco seguro.
usuarios_db = {}

ITERATIONS = 600_000
KEY_LENGTH = 32
SALT_LENGTH = 16


def gerar_hash_senha(senha, salt=None):
    """Gera salt e hash PBKDF2 para uma senha."""
    if not isinstance(senha, str) or not senha:
        raise ValueError("A senha deve ser uma string não vazia.")

    if salt is None:
        salt_bytes = secrets.token_bytes(SALT_LENGTH)
    else:
        salt_bytes = bytes.fromhex(salt)

    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt_bytes,
        ITERATIONS,
        dklen=KEY_LENGTH
    )

    return salt_bytes.hex(), hash_bytes.hex()


def cadastrar_usuario(usuario, senha):
    """Cadastra um usuário armazenando somente salt e hash."""
    if usuario in usuarios_db:
        raise ValueError("Usuário já cadastrado.")

    salt, hash_senha = gerar_hash_senha(senha)
    usuarios_db[usuario] = {
        "salt": salt,
        "hash": hash_senha
    }

    logging.info("Usuário '%s' cadastrado com sucesso.", usuario)


def verificar_senha(senha, salt, hash_armazenado):
    """Verifica a senha informada contra o hash armazenado."""
    _, hash_calculado = gerar_hash_senha(senha, salt)

    return hmac.compare_digest(hash_calculado, hash_armazenado)


def login(usuario, senha):
    """Realiza a autenticação do usuário."""
    if usuario not in usuarios_db:
        logging.warning("Tentativa de login com usuário inexistente: '%s'.", usuario)
        print("Falha na autenticação")
        return False

    dados_usuario = usuarios_db[usuario]

    if verificar_senha(senha, dados_usuario["salt"], dados_usuario["hash"]):
        logging.info("Login realizado com sucesso para o usuário '%s'.", usuario)
        print(f"Acesso liberado para {usuario}")
        return True

    logging.warning("Falha de autenticação para o usuário '%s'.", usuario)
    print("Falha na autenticação")
    return False


if __name__ == "__main__":
    # Exemplo de uso.
    # Para demonstração, criamos usuários com senhas conhecidas.
    usuarios_db.clear()

    cadastrar_usuario("admin", "admin123")
    cadastrar_usuario("gerente", "senha456")

    login("admin", "admin123")       # Deve permitir acesso.
    login("admin", "senha_errada")   # Deve negar acesso.
    login("inexistente", "123456")   # Deve negar acesso.
