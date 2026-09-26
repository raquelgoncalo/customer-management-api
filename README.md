# Customer Management API

API REST para gerenciamento de clientes, desenvolvida com Python e FastAPI, com persistência em PostgreSQL e autenticação baseada em JWT.

O projeto implementa operações CRUD de clientes, cadastro e autenticação de usuários, proteção de endpoints e armazenamento seguro de senhas com Argon2.

## Funcionalidades

- Cadastro de usuários
- Login com geração de token JWT
- Proteção das rotas de clientes
- Criação de clientes
- Listagem de clientes
- Consulta de cliente por ID
- Atualização de clientes
- Exclusão de clientes
- Validação de dados com Pydantic
- Verificação de e-mail duplicado
- Hash seguro de senhas com Argon2
- Persistência de dados em PostgreSQL

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Neon
- Pydantic
- PyJWT
- pwdlib / Argon2
- Uvicorn

## Endpoints

### Autenticação

| Método | Endpoint | Descrição |
| --- | --- | --- |
| POST | `/auth/register` | Cadastra um usuário |
| POST | `/auth/login` | Autentica o usuário e gera um JWT |

### Clientes

As rotas de clientes exigem autenticação via Bearer Token.

| Método | Endpoint | Descrição |
| --- | --- | --- |
| GET | `/customers` | Lista os clientes |
| POST | `/customers` | Cadastra um cliente |
| GET | `/customers/{customer_id}` | Busca um cliente por ID |
| PUT | `/customers/{customer_id}` | Atualiza um cliente |
| DELETE | `/customers/{customer_id}` | Exclui um cliente |

### Health Check

| Método | Endpoint | Descrição |
| --- | --- | --- |
| GET | `/` | Verifica se a API está online |

## Estrutura do projeto

```text
customer-management-api/
├── app/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── security/
│   ├── services/
│   └── database.py
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/customer-management-api.git
cd customer-management-api
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto utilizando `.env.example` como referência:

```env
DATABASE_URL=postgresql+psycopg://usuario:senha@host:5432/banco
JWT_SECRET_KEY=sua_chave_secreta
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Nunca publique o arquivo `.env` ou credenciais reais.

### 5. Execute a aplicação

```bash
uvicorn main:app --reload
```

A documentação interativa estará disponível em:

```text
http://127.0.0.1:8000/docs
```

## Autenticação

Após realizar o login em `/auth/login`, a API retorna um `access_token`.

Esse token deve ser enviado como Bearer Token para acessar os endpoints protegidos de clientes.

Exemplo:

```text
Authorization: Bearer <access_token>
```

## Segurança

- Senhas não são armazenadas em texto puro.
- O hash das senhas utiliza Argon2.
- As rotas de clientes exigem autenticação.
- Tokens JWT possuem tempo de expiração.
- Credenciais e chaves são carregadas por variáveis de ambiente.
- O arquivo `.env` é ignorado pelo Git.

## Documentação

O FastAPI gera automaticamente documentação interativa através do Swagger UI em `/docs`.

## Status

Projeto funcional desenvolvido para demonstração de uma API REST com autenticação, banco de dados relacional e operações CRUD.