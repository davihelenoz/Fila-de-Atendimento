# 📋 Sistema de Fila de Atendimento

Mini aplicação web desenvolvida em **Python**, utilizando **Flask** e **SQLite**, para gerenciamento de uma fila de atendimento.

O sistema permite cadastrar clientes, visualizar a fila, chamar o próximo cliente seguindo a lógica **FIFO (First In, First Out)**, alterar o status dos atendimentos e cancelar atendimentos.

## 🚀 Funcionalidades

* 👤 Cadastro de clientes na fila
* 📋 Visualização da fila de espera
* 📞 Chamada do próximo cliente
* 🔄 Controle de status dos atendimentos
* ✅ Conclusão de atendimentos
* ❌ Cancelamento de atendimentos
* 💾 Armazenamento dos dados utilizando SQLite
* 🔢 Organização da fila seguindo o princípio FIFO

## 🛠️ Tecnologias utilizadas

* **Python**
* **Flask**
* **SQLite**
* **HTML**
* **CSS**
* **Jinja2**

## 📁 Estrutura do projeto

```text
fila_atendimento/
│
├── app.py
├── fila.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

> O arquivo `fila.db` é criado automaticamente na primeira execução da aplicação.

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd fila_atendimento
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
python app.py
```

Depois, abra o endereço mostrado no terminal, normalmente:

```text
http://127.0.0.1:5000
```

## 🔄 Funcionamento da fila

O sistema utiliza a lógica **FIFO — First In, First Out**.

Isso significa que o primeiro cliente que entrar na fila será o primeiro cliente chamado.

Exemplo:

```text
1 - João
2 - Maria
3 - Carlos
```

Ao clicar em **Chamar próximo**, João será chamado primeiro.

Depois:

```text
1 - João      → atendimento
2 - Maria     → aguardando
3 - Carlos    → aguardando
```

Ao chamar novamente:

```text
1 - João      → atendimento
2 - Maria     → atendimento
3 - Carlos    → aguardando
```

Essa lógica é implementada através da ordenação dos clientes pelo seu `id` no banco de dados.

## 📊 Status

Cada cliente pode possuir um dos seguintes estados:

| Status        | Descrição                   |
| ------------- | --------------------------- |
| `aguardando`  | Cliente esperando na fila   |
| `atendimento` | Cliente está sendo atendido |
| `concluido`   | Atendimento foi finalizado  |
| `cancelado`   | Atendimento foi cancelado   |

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenar os clientes.

A tabela principal possui:

| Campo     | Descrição                      |
| --------- | ------------------------------ |
| `id`      | Identificador único do cliente |
| `nome`    | Nome do cliente                |
| `servico` | Serviço solicitado             |
| `horario` | Horário de entrada na fila     |
| `status`  | Estado atual do atendimento    |

## 🎯 Objetivo

Este projeto foi desenvolvido como um mini projeto para praticar conceitos de:

* Desenvolvimento web com Flask
* Banco de dados relacionais
* Operações SQL
* CRUD
* Rotas HTTP
* Formulários HTML
* Organização de projetos Python
* Lógica de filas e FIFO

## 👨‍💻 Autor

**Davi Heleno**

Projeto desenvolvido para fins educacionais.
