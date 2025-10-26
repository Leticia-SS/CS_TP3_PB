import random
import time

class Node:
    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None


class BinaryTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome):
        self.raiz = self._inserir_recursivo(self.raiz, nome)

    def _inserir_recursivo(self, no, nome):
        if no is None:
            return Node(nome)

        if nome < no.nome:
            no.esquerda = self._inserir_recursivo(no.esquerda, nome)
        else:
            no.direita = self._inserir_recursivo(no.direita, nome)

        return no

    def buscar_por_letra(self, letra):
        resultados = []
        self._buscar_por_letra_recursivo(self.raiz, letra, resultados)
        return resultados

    def _buscar_por_letra_recursivo(self, no, letra, resultados):
        if no is None:
            return

        if no.nome.startswith(letra):
            resultados.append(no.nome)

        self._buscar_por_letra_recursivo(no.esquerda, letra, resultados)
        self._buscar_por_letra_recursivo(no.direita, letra, resultados)

    def deletar(self, nome):
        self.raiz = self._deletar_recursivo(self.raiz, nome)

    def _deletar_recursivo(self, no, nome):
        if no is None:
            return no

        if nome < no.nome:
            no.esquerda = self._deletar_recursivo(no.esquerda, nome)
        elif nome > no.nome:
            no.direita = self._deletar_recursivo(no.direita, nome)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            sucessor = self._encontrar_minimo(no.direita)
            no.nome = sucessor.nome
            no.direita = self._deletar_recursivo(no.direita, sucessor.nome)

        return no

    def _encontrar_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def deletar_por_letra(self, letra):
        registros = self.buscar_por_letra(letra)
        if registros:
            registro_deletar = random.choice(registros)
            print(f"Deletando registro: {registro_deletar}")
            self.deletar(registro_deletar)
            return registro_deletar
        return None

    def imprimir_ate_altura_5(self):
        print("\nÁrvore até altura 5:")
        self._imprimir_recursivo(self.raiz, 0, 5)

    def _imprimir_recursivo(self, no, altura_atual, altura_maxima):
        if no is None or altura_atual > altura_maxima:
            return

        espacos = "  " * altura_atual
        print(f"{espacos}{no.nome}")

        self._imprimir_recursivo(no.esquerda, altura_atual + 1, altura_maxima)
        self._imprimir_recursivo(no.direita, altura_atual + 1, altura_maxima)

    def contar_nos(self):
        return self._contar_nos_recursivo(self.raiz)

    def _contar_nos_recursivo(self, no):
        if no is None:
            return 0
        return 1 + self._contar_nos_recursivo(no.esquerda) + self._contar_nos_recursivo(no.direita)


def carregar_registros_arquivo(nome_arquivo):
    registros = []
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                registro = linha.strip()
                if registro:
                    registros.append(registro)
        return registros
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
        print("Gerando dados de exemplo...")
        nomes_exemplo = ["Alice", "Bruno", "Carlos", "Daniel", "Eduardo", "Fernanda",
                         "Gabriel", "Helena", "Igor", "João", "Karen", "Lucas",
                         "Mariana", "NatAlia", "Otávio", "Paula", "Quezia",
                         "Rafael", "Sofia", "Thiago", "Úrsula", "Vitor", "Wagner",
                         "Xavier", "Yasmin", "Zoe", "Maria", "Zacarias"]
        return nomes_exemplo * 358


def encontrar_melhor_raiz(registros):
    if not registros:
        return None
    registros_ordenados = sorted(registros)
    meio = len(registros_ordenados) // 2
    return registros_ordenados[meio]


def main():
    print("Carregando registros do arquivo...")
    registros = carregar_registros_arquivo("registros.txt")
    print(f"Total de registros carregados: {len(registros)}")

    print("\nInserindo registros na árvore binária...")
    arvore = BinaryTree()

    inicio = time.time()
    for registro in registros:
        arvore.inserir(registro)
    fim = time.time()

    print(f"Tempo de inserção: {fim - inicio:.4f} segundos")
    print(f"Total de nós na árvore: {arvore.contar_nos()}")

    print("\nExclusão de registro com letra 'M'")
    registro_deletado = arvore.deletar_por_letra('M')
    if registro_deletado:
        print(f"Registro deletado com sucesso: {registro_deletado}")
    else:
        print("Nenhum registro encontrado com a letra 'M'")

    print("\nBusca por registros com letra 'Z'")
    registros_Z = arvore.buscar_por_letra('Z')
    if registros_Z:
        print(f"Encontrados {len(registros_Z)} registros com a letra 'Z':")
        for i, registro in enumerate(registros_Z[:3]):
            print(f"  {i + 1}. {registro}")
        if len(registros_Z) > 3:
            print(f"  ... e mais {len(registros_Z) - 3} registros")
    else:
        print("Nenhum registro encontrado com a letra 'Z'")

    print("\nImpressão da árvore até altura 5")
    arvore.imprimir_ate_altura_5()

    print("\nMelhor escolha para nó raiz")
    melhor_raiz = encontrar_melhor_raiz(registros)
    print(f"Melhor raiz: {melhor_raiz}")
    print("Porque a mediana balanceia a árvore, melhorando o desempenho das operações.")

    print(f"\nTotal de nós na árvore: {arvore.contar_nos()}")


if __name__ == "__main__":
    main()