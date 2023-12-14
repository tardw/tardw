import json
from datetime import datetime

class ListaDeTarefas:
    def __init__(self):
        self.carregar_tarefas()

    def adicionar_tarefa(self, data, descricao):
        if data in self.tarefas:
            if descricao not in self.tarefas[data]:
                self.tarefas[data].append(descricao)
                print(f"Tarefa adicionada em {data}: {descricao}")
            else:
                print("Tarefa já existe para esta data.")
        else:
            self.tarefas[data] = [descricao]
            print(f"Tarefa adicionada em {data}: {descricao}")
        self.salvar_tarefas()

    def excluir_tarefa(self, data, descricao):
        if data in self.tarefas and descricao in self.tarefas[data]:
            self.tarefas[data].remove(descricao)
            print(f"Tarefa removida em {data}: {descricao}")
            if not self.tarefas[data]:
                del self.tarefas[data]
            self.salvar_tarefas()
        else:
            print("Tarefa não encontrada para exclusão.")

    def mostrar_tarefas(self):
        if not self.tarefas:
            print("Lista de tarefas vazia.")
        else:
            print("Lista de Tarefas:")
            for data, tarefas in self.tarefas.items():
                print(f"{data}: {', '.join(tarefas)}")

    def salvar_tarefas(self):
        with open("tarefas.json", "w") as arquivo:
            json.dump(self.tarefas, arquivo)

    def carregar_tarefas(self):
        try:
            with open("tarefas.json", "r") as arquivo:
                self.tarefas = json.load(arquivo)
        except FileNotFoundError:
            self.tarefas = {}


# Exemplo de uso
lista_tarefas = ListaDeTarefas()

lista_tarefas.adicionar_tarefa("2035-04-12", "Usar k2")
lista_tarefas.adicionar_tarefa("2034-06-31", "Jogar lol")
lista_tarefas.adicionar_tarefa("2022-02-22", "Ouçar musga")

lista_tarefas.mostrar_tarefas()

lista_tarefas.excluir_tarefa("2034-06-31", "Jogar lol")

lista_tarefas.mostrar_tarefas()