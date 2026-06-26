# 🚀 TaskFlow — Sistema de Gerenciamento de Tarefas

**TechFlow Solutions** | Projeto Ágil | Engenharia de Software — UniFECAF

---

## 📌 Objetivo do Projeto

Sistema de gerenciamento de tarefas desenvolvido para uma startup de logística,
permitindo acompanhar o fluxo de trabalho em tempo real, priorizar tarefas
críticas e monitorar o desempenho da equipe com base em metodologias ágeis.

---

## 📐 Escopo Inicial

- CRUD completo de tarefas (Criar, Listar, Atualizar, Deletar)
- Controle de status: A Fazer → Em Progresso → Concluído
- Testes automatizados com Pytest
- Pipeline de integração contínua com GitHub Actions

---

## 🔄 Mudança de Escopo

**Feature adicionada:** Filtro de tarefas por prioridade (ALTA, MEDIA, BAIXA)

**Justificativa:** Durante o desenvolvimento, o cliente (startup de logística)
identificou a necessidade de visualizar rapidamente as tarefas críticas separadas
das demais. A funcionalidade `filtrar_por_prioridade()` foi adicionada ao
`TaskRepository` sem impactar as funcionalidades existentes.

---

## 🛠️ Metodologia Ágil

Utilizamos **Kanban** como metodologia principal, com o quadro organizado
no GitHub Projects em três colunas:

| Coluna | Descrição |
|--------|-----------|
| A Fazer | Tarefas planejadas aguardando início |
| Em Progresso | Tarefas sendo executadas |
| Concluído | Tarefas finalizadas e validadas |

---

## 📁 Estrutura do Projeto

taskflow/

├── src/

│   ├── model/

│   │   └── task.py

│   └── repository/

│       └── task_repository.py

├── tests/

│   └── test_task_repository.py

├── docs/

├── .github/

│   └── workflows/

│       └── ci.yml

├── main.py

└── README.md

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.11 ou superior

```bash
# Rodar o sistema
python main.py

# Rodar os testes
pip install pytest
pytest tests/ -v
```

---

## 🧪 Testes Automatizados

14 testes unitários com **Pytest**:

| Classe | O que valida |
|--------|-------------|
| TestCriarTarefa | Operação CREATE |
| TestListarTarefas | Operações READ |
| TestAtualizarStatus | Operação UPDATE |
| TestDeletarTarefa | Operação DELETE |
| TestFiltrarPorPrioridade | Mudança de escopo |

---

## ⚙️ Pipeline CI — GitHub Actions

A cada push na branch `main` o pipeline executa automaticamente:
1. Checkout do código
2. Configuração do Python 3.11
3. Instalação do Pytest
4. Execução de todos os testes
5. Confirmação de sucesso