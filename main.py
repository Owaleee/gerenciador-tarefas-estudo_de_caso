# Arquivo principal do sistema TaskFlow
from src.repository.task_repository import TaskRepository


def main():
    repositorio = TaskRepository()

    print("=" * 55)
    print("  TaskFlow — Sistema de Gerenciamento de Tarefas")
    print("  TechFlow Solutions | Startup de Logística")
    print("=" * 55)

    # CREATE — Criando tarefas
    print("\n📋 Criando tarefas...\n")
    repositorio.criar_tarefa("Configurar ambiente de desenvolvimento", "ALTA")
    repositorio.criar_tarefa("Implementar login de usuário", "ALTA")
    repositorio.criar_tarefa("Criar dashboard de tarefas", "MEDIA")
    repositorio.criar_tarefa("Escrever documentação técnica", "BAIXA")

    # READ — Listando todas
    print("--- Todas as tarefas ---")
    for tarefa in repositorio.listar_todas():
        print(" ", tarefa)

    # UPDATE — Mudando status
    repositorio.atualizar_status(1, "EM_PROGRESSO")
    repositorio.atualizar_status(2, "CONCLUIDO")

    print("\n--- Após atualização de status ---")
    for tarefa in repositorio.listar_todas():
        print(" ", tarefa)

    # FILTRO — Mudança de escopo
    print("\n--- Tarefas de ALTA prioridade ---")
    for tarefa in repositorio.filtrar_por_prioridade("ALTA"):
        print(" ", tarefa)

    # DELETE
    repositorio.deletar_tarefa(4)
    print("\n--- Após deletar tarefa 4 ---")
    for tarefa in repositorio.listar_todas():
        print(" ", tarefa)

    print("\n✅ Sistema funcionando corretamente!")


if __name__ == "__main__":
    main()
# Demonstração completa do sistema