# Plano de Manutenção de Emergência

## 1. Identificação da Manutenção

**Sistema:** Sistema de Retaguarda de E-commerce
**Módulo:** Autenticação
**Arquivo afetado:** `autenticacao.py`
**Arquivo corrigido:** `autenticacao_corrigido.py`
**Prioridade:** Crítica
**Tipo de manutenção:** Corretiva e Preventiva

### Justificativa

A manutenção é classificada principalmente como **corretiva**, pois existe uma falha de segurança no módulo de autenticação que precisa ser corrigida imediatamente.

Também possui caráter **preventivo**, pois a implementação de armazenamento seguro das credenciais e de registros de tentativas reduz o risco de novos incidentes relacionados à autenticação.

O código original armazena as senhas diretamente no dicionário `usuarios_db` e realiza a comparação em texto puro. Além disso, não registra adequadamente as tentativas de acesso.

---

# 2. Prompt Utilizado

O seguinte prompt foi utilizado como auxílio de Inteligência Artificial Generativa para analisar o código e elaborar o plano de manutenção:

> **Prompt:**
>
> Atue como um Engenheiro de Software responsável pela manutenção e segurança de sistemas.
>
> Analise o código Python do módulo de autenticação fornecido abaixo. O sistema é um módulo de autenticação de um sistema de retaguarda de um e-commerce e apresentou uma falha crítica de segurança relacionada ao armazenamento e comparação de senhas.
>
> **Código analisado:**
>
> ```python
> # Módulo de Autenticação Legado
> usuarios_db = {
>     "admin": "admin123",
>     "gerente": "senha456"
> }
>
> def login(usuario, senha):
>     # FALHA CRÍTICA: Senhas armazenadas e comparadas em texto puro!
>     # Falta de logs de tentativa de acesso.
>     if usuario in usuarios_db:
>         if usuarios_db[usuario] == senha:
>             print(f"Acesso liberado para {usuario}")
>             return True
>     print("Falha na autenticação")
>     return False
> ```
>
> Com base nesse código, gere um Plano de Manutenção de Emergência contendo:
>
> 1. O tipo de manutenção necessária (Corretiva, Preventiva, Adaptativa ou Perfectiva) e a justificativa para essa classificação.
> 2. O diagnóstico detalhado dos problemas e vulnerabilidades encontrados no código, especialmente relacionados ao armazenamento e comparação de senhas e à ausência de logs de tentativas de acesso.
> 3. A avaliação do impacto dessas vulnerabilidades para o sistema.
> 4. Um procedimento de manutenção passo a passo para corrigir os problemas, incluindo identificação, planejamento, implementação, testes e documentação.
> 5. Um plano de testes recomendados para validar a correção, incluindo testes de login com senha correta, senha incorreta, usuário inexistente e verificação de que as senhas não estão armazenadas em texto puro.
> 6. Uma estratégia de rollback caso a alteração apresente problemas após a implementação.
> 7. Uma sugestão de refatoração simples do código Python utilizando boas práticas de segurança e somente bibliotecas padrão do Python. A solução deve utilizar hash de senha com salt, preferencialmente PBKDF2-HMAC por meio da biblioteca hashlib, e comparação segura das credenciais. Também deve incluir registro de tentativas de autenticação utilizando logging.
> 8. Explique brevemente as principais alterações realizadas no código e por que elas tornam o módulo mais seguro.
>
> Organize a resposta de forma clara e profissional, utilizando títulos, listas e tabelas quando forem úteis. Não armazene senhas em texto puro na versão corrigida e não registre senhas nos logs.

---

# 3. Diagnóstico dos Problemas

## 3.1 Senhas armazenadas em texto puro

O código original possui as senhas diretamente no dicionário:

```python
usuarios_db = {
    "admin": "admin123",
    "gerente": "senha456"
}
```

Dessa forma, qualquer pessoa que tenha acesso aos dados poderá visualizar diretamente as credenciais dos usuários.

## 3.2 Comparação de senha em texto puro

O login utiliza diretamente:

```python
if usuarios_db[usuario] == senha:
```

Isso faz com que a senha informada seja comparada diretamente com o valor armazenado.

## 3.3 Ausência de logs de autenticação

O código utiliza apenas `print()` para indicar sucesso ou falha.

Isso dificulta o acompanhamento de tentativas de acesso e a investigação de possíveis incidentes.

## 3.4 Falta de proteção das credenciais

O módulo não utiliza hash, salt ou qualquer mecanismo de derivação de senha.

---

# 4. Avaliação do Impacto

A vulnerabilidade pode expor as credenciais dos usuários caso o armazenamento seja acessado indevidamente.

A ausência de registros de autenticação também dificulta a identificação de tentativas suspeitas.

**Nível de impacto:** Crítico.

**Módulo diretamente afetado:** Autenticação.

**Áreas potencialmente afetadas:** Controle de acesso, contas administrativas e segurança do sistema.

---

# 5. Procedimento de Manutenção

A manutenção seguirá um fluxo estruturado de identificação, avaliação, planejamento, implementação, testes e documentação, conforme proposto no laboratório.

### Etapa 1 — Identificar e diagnosticar

Identificar as vulnerabilidades presentes no módulo de autenticação e confirmar que as senhas estão armazenadas e comparadas em texto puro.

### Etapa 2 — Avaliar o impacto

Verificar que o problema afeta diretamente a segurança das credenciais e o controle de acesso do sistema.

### Etapa 3 — Planejar

Definir a alteração do mecanismo de autenticação, preservar uma cópia da versão original e estabelecer uma estratégia de rollback.

### Etapa 4 — Implementar

Criar o arquivo `autenticacao_corrigido.py`, substituindo o armazenamento de senhas em texto puro por hashes com salt.

Também implementar:

* `hashlib.pbkdf2_hmac()` para derivação do hash;
* `secrets` para geração de salt;
* `hmac.compare_digest()` para comparação segura;
* `logging` para registrar eventos de autenticação.

### Etapa 5 — Testar

Executar testes de autenticação válida, senha incorreta, usuário inexistente e armazenamento seguro das credenciais.

### Etapa 6 — Documentar

Registrar as alterações realizadas, os testes executados, os resultados obtidos e a versão corrigida do sistema.

---

# 6. Plano de Testes

| ID  | Teste               | Entrada                             | Resultado esperado                 |
| --- | ------------------- | ----------------------------------- | ---------------------------------- |
| T01 | Login válido        | Usuário e senha corretos            | Acesso liberado                    |
| T02 | Senha incorreta     | Usuário existente + senha incorreta | Acesso negado                      |
| T03 | Usuário inexistente | Usuário não cadastrado              | Acesso negado                      |
| T04 | Cadastro            | Novo usuário + senha                | Usuário cadastrado com hash        |
| T05 | Senha vazia         | Usuário + senha vazia               | Operação rejeitada                 |
| T06 | Armazenamento       | Usuário cadastrado                  | Senha não armazenada em texto puro |
| T07 | Logs                | Tentativas de login                 | Eventos registrados                |

### Critérios de aprovação

A correção será considerada aprovada quando:

* nenhuma senha estiver armazenada em texto puro;
* uma senha correta permitir o acesso;
* uma senha incorreta impedir o acesso;
* usuários inexistentes não conseguirem autenticar;
* as tentativas de autenticação forem registradas;
* o programa funcionar sem erros.

---

# 7. Estratégia de Rollback

Caso a versão corrigida apresente problemas:

1. Interromper a implantação.
2. Preservar os logs e informações de erro.
3. Restaurar a versão anterior em ambiente controlado.
4. Identificar a causa do problema.
5. Corrigir a implementação.
6. Executar novamente os testes.
7. Realizar uma nova implantação somente após a validação.

---

# 8. Refatoração Implementada

A versão corrigida foi criada no arquivo:

**`autenticacao_corrigido.py`**

A principal alteração foi substituir o armazenamento direto das senhas por uma estrutura contendo:

```text
salt
hash
```

O processo de autenticação passou a seguir:

```text
Senha informada
       ↓
Salt armazenado
       ↓
PBKDF2-HMAC
       ↓
Hash calculado
       ↓
Comparação segura
       ↓
Acesso permitido ou negado
```

Também foi implementado o sistema de `logging` para registrar eventos de autenticação sem registrar as senhas dos usuários.

---

# 9. Resultado Esperado

Após a manutenção, o módulo deverá armazenar somente informações derivadas das senhas, evitando o armazenamento de credenciais em texto puro.

O sistema também deverá registrar tentativas de autenticação, aumentando a rastreabilidade e facilitando a identificação de comportamentos suspeitos.

A documentação da manutenção permite acompanhar o que foi alterado, o motivo da alteração, os testes realizados e os impactos esperados, conforme o objetivo apresentado no laboratório.

---

# 10. Arquivo Entregável

**Arquivo:** `autenticacao_corrigido.py`

O arquivo contém a implementação corrigida do módulo de autenticação e deverá ser enviado junto com este plano de manutenção.
