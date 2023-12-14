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

# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza", 0
    elif 18.5 <= imc < 25.0:
        return "Normal", 0
    elif 25.0 <= imc < 30.0:
        return "Sobrepeso I", 0
    elif 30.0 <= imc < 40.0:
        return "Obesidade II", 0
    else:
        return "Obesidade Grave I", 0

# Função principal
def main():
    print("Escolha uma opção:")
    print("1. Calculadora de IMC")
    print("2. Lista de Tarefas")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        try:
            peso = float(input("Digite o peso em kg: "))
            altura = float(input("Digite a altura em metros: "))

            if peso <= 0 or altura <= 0:
                print("Peso e altura devem ser valores positivos.")
                return

            imc = calcular_imc(peso, altura)
            classificacao, grau_obesidade = classificar_imc(imc)

            print(f"Seu IMC é {imc:.2f}")
            print(f"Classificação: {classificacao}")
            print(f"Obesidade (Grau): {grau_obesidade}")

        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números para peso e altura.")
    
    elif opcao == "2":
        lista_tarefas = ListaDeTarefas()

        #lista_tarefas.adicionar_tarefa("2012-12-12", "Estudar")
        #lista_tarefas.adicionar_tarefa("2011-01-25", "Andar")
        #lista_tarefas.adicionar_tarefa("2022-06-16", "Jogar bola")

        #lista_tarefas.mostrar_tarefas()

        #lista_tarefas.excluir_tarefa("2011-01-25", "Andar")

        #lista_tarefas.mostrar_tarefas()

    else:
        print("Opção inválida. Escolha 1 ou 2.")

# Chamada da função principal
if __name__ == "__main__":
    main()
