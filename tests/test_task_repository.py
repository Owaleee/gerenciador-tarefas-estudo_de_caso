# Testes unitários para o TaskRepository
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.repository.task_repository import TaskRepository


class TestCriarTarefa:
    def setup_method(self):
        self.repositorio = TaskRepository()

    def test_criar_tarefa_retorna_objeto(self):
        tarefa = self.repositorio.criar_tarefa("Nova tarefa", "ALTA")
        assert tarefa is not None

    def test_criar_tarefa_status_inicial(self):
        tarefa = self.repositorio.criar_tarefa("Tarefa teste", "MEDIA")
        assert tarefa.status == "A_FAZER"

    def test_criar_tarefa_prioridade_maiuscula(self):
        tarefa = self.repositorio.criar_tarefa("Tarefa", "alta")
        assert tarefa.prioridade == "ALTA"


class TestListarTarefas:
    def setup_method(self):
        self.repositorio = TaskRepository()

    def test_listar_todas_vazio(self):
        assert self.repositorio.listar_todas() == []

    def test_listar_todas_com_tarefas(self):
        self.repositorio.criar_tarefa("Tarefa 1", "MEDIA")
        self.repositorio.criar_tarefa("Tarefa 2", "BAIXA")
        assert len(self.repositorio.listar_todas()) == 2

    def test_buscar_por_id_existente(self):
        tarefa = self.repositorio.criar_tarefa("Buscar isso", "ALTA")
        encontrada = self.repositorio.buscar_por_id(tarefa.id)
        assert encontrada is not None

    def test_buscar_por_id_inexistente(self):
        assert self.repositorio.buscar_por_id(999) is None


class TestAtualizarStatus:
    def setup_method(self):
        self.repositorio = TaskRepository()

    def test_atualizar_status_sucesso(self):
        tarefa = self.repositorio.criar_tarefa("Atualizar", "MEDIA")
        resultado = self.repositorio.atualizar_status(tarefa.id, "CONCLUIDO")
        assert resultado is True
        assert self.repositorio.buscar_por_id(tarefa.id).status == "CONCLUIDO"

    def test_atualizar_status_id_invalido(self):
        assert self.repositorio.atualizar_status(999, "CONCLUIDO") is False


class TestDeletarTarefa:
    def setup_method(self):
        self.repositorio = TaskRepository()

    def test_deletar_tarefa_sucesso(self):
        tarefa = self.repositorio.criar_tarefa("Deletar isso", "BAIXA")
        assert self.repositorio.deletar_tarefa(tarefa.id) is True
        assert len(self.repositorio.listar_todas()) == 0

    def test_deletar_tarefa_id_invalido(self):
        assert self.repositorio.deletar_tarefa(999) is False


class TestFiltrarPorPrioridade:
    def setup_method(self):
        self.repositorio = TaskRepository()
        self.repositorio.criar_tarefa("Urgente 1", "ALTA")
        self.repositorio.criar_tarefa("Normal", "MEDIA")
        self.repositorio.criar_tarefa("Urgente 2", "ALTA")
        self.repositorio.criar_tarefa("Baixa prio", "BAIXA")

    def test_filtrar_alta_prioridade(self):
        assert len(self.repositorio.filtrar_por_prioridade("ALTA")) == 2

    def test_filtrar_media_prioridade(self):
        assert len(self.repositorio.filtrar_por_prioridade("MEDIA")) == 1

    def test_filtrar_case_insensitive(self):
        assert len(self.repositorio.filtrar_por_prioridade("alta")) == 2