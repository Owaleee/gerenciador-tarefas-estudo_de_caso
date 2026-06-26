# Repositório responsável pelo CRUD de tarefas
from src.model.task import Task
from typing import Optional


class TaskRepository:
    """Gerencia criação, leitura, atualização e exclusão de tarefas."""

    def __init__(self):
        # Lista que simula o banco de dados
        self._tarefas: list[Task] = []
        self._proximo_id: int = 1

    # CREATE — Adiciona uma nova tarefa
    def criar_tarefa(self, titulo: str, prioridade: str) -> Task:
        nova = Task(
            id=self._proximo_id,
            titulo=titulo,
            status="A_FAZER",
            prioridade=prioridade.upper()
        )
        self._tarefas.append(nova)
        self._proximo_id += 1
        return nova

    # READ — Lista todas as tarefas
    def listar_todas(self) -> list[Task]:
        return list(self._tarefas)

    # READ — Busca tarefa por ID
    def buscar_por_id(self, id: int) -> Optional[Task]:
        for tarefa in self._tarefas:
            if tarefa.id == id:
                return tarefa
        return None

    # UPDATE — Atualiza o status de uma tarefa
    def atualizar_status(self, id: int, novo_status: str) -> bool:
        tarefa = self.buscar_por_id(id)
        if tarefa:
            tarefa.status = novo_status
            return True
        return False

    # DELETE — Remove uma tarefa pelo ID
    def deletar_tarefa(self, id: int) -> bool:
        tarefa = self.buscar_por_id(id)
        if tarefa:
            self._tarefas.remove(tarefa)
            return True
        return False

    # FILTRO POR PRIORIDADE — Mudança de escopo
    def filtrar_por_prioridade(self, prioridade: str) -> list[Task]:
        return [t for t in self._tarefas if t.prioridade == prioridade.upper()]