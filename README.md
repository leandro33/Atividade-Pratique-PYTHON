# 📍 Sistema de Cadastro e Notificação de Eventos (Console Python)

Este é um sistema de console desenvolvido em Python, orientado a objetos, para cadastro e notificação de eventos da cidade.

---

## 🧩 Funcionalidades

- Cadastro de usuários
- Criação de eventos com:
  - Nome
  - Endereço
  - Categoria (Festa, Esporte, Show, etc)
  - Data e Hora
  - Descrição
- Participação e cancelamento em eventos
- Consulta de eventos ordenados por data
- Detecção de eventos em andamento e eventos passados
- Armazenamento de dados em arquivo `events.data`

---

## 🛠 Requisitos

- Python 3.10 ou superior
- VSCode (recomendado)
- Terminal PowerShell, CMD ou bash

---

## 🚀 Instalação e Execução

### 1. Clone ou descompacte o projeto

Caso tenha baixado o `.zip`, descompacte em uma pasta local.

Se estiver usando git:
```bash
git clone <link-do-repositório>
cd event_system
```

---

### 2. Crie o ambiente virtual (Windows)

```powershell
py -m venv venv
.env\Scripts\Activate.ps1
```

Se estiver no Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Execute o programa

```bash
python main.py
```

---

## 🧪 Estrutura de Pastas

```
event_system/
│
├── main.py                 # Arquivo principal para rodar o app
├── app.py                  # Interface principal da aplicação
│
├── models/
│   ├── user.py             # Classe User
│   └── event.py            # Classe Event
│
├── services/
│   └── event_manager.py    # Classe de persistência e gerenciamento dos eventos
│
├── events.data             # Arquivo gerado automaticamente com os eventos salvos
└── README.md               # Este arquivo
```

---

## 💡 Observações

- Os dados dos eventos são armazenados com `pickle` no arquivo `events.data`.
- A aplicação carrega os dados automaticamente ao iniciar.
- Apenas eventos futuros são listados como disponíveis para participação.
- O horário do evento deve estar no formato `dd/mm/yyyy hh:mm`.

---

## ✨ Exemplo de Uso

```
=== Sistema de Eventos da Cidade ===
Nome: João Silva
Email: joao@email.com
Cidade: Porto Alegre

1. Cadastrar Evento
2. Ver Todos os Eventos
3. Participar de Evento
...
```

---

## 🧑‍💻 Autor

Desenvolvido como exercício de prática em Python com orientação a objetos. Ideal para estudo de persistência, estruturação em camadas e manipulação de datas com `datetime`.

---