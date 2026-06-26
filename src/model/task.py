# Modelo de dados para uma Tarefa do sistema TaskFlow
class Task:
    """Classe que representa uma tarefa no sistema TaskFlow."""

    def __init__(self, id: int, titulo: str, status: str, prioridade: str):
        # Identificador único da tarefa
        self.id = id
        # Título descritivo da tarefa
        self.titulo = titulo
        # Status atual: A_FAZER, EM_PROGRESSO ou CONCLUIDO
        self.status = status
        # Prioridade: ALTA, MEDIA ou BAIXA
        self.prioridade = prioridade

    def __repr__(self):
        return f"[{self.id}] {self.titulo} | Status: {self.status} | Prioridade: {self.prioridade}"

# Modelo finalizado - versão 1.0