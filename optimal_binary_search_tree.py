#!/usr/bin/env python3

#  Este programa em Python implementa o algoritmo de busca binária em árvore ótima
#  com desempenho O(nˆ2).
#  O objetivo do problema de busca binária em árvore ótima é construir a árvore
#  de menor custo com um conjunto de nós, sendo que cada nó contém uma chave e uma frequência.
#  A frequência do nó é definida em quantas vezes o nó foi buscado.
#
#  O cálculo do custo da busca na árvore binária de busca é:
#
# custo(1, n) = sum{i = 1 to n}((depth(node_i) + 1)* node_i_freq)
#
# onde n é o número de nós na árvore binária de busca.
#
# Com este algoritmo, os nós com alta frequência serão posicionados próximos da raiz da árvore,
# enquanto os nós com baixa frequência serão posicionados próximos das folhas da árvore,
# reduzindo o tempo de busca.

import sys
from random import randint


class Node:
    """Binary Search Tree Node"""

    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        return f"Node(key={self.key}, freq={self.freq})"


def print_binary_search_tree(root, key, i, j, parent, is_left):
    """
    Função recursiva para imprimir a Árvore Binária de Busca a partir da raiz.
    """
    if i > j or i < 0 or j > len(root) - 1:
        return

    node = root[i][j]
    if parent == -1: 
        print(f"{key[node]} é o nó raiz da árvore binária de busca.")
    elif is_left:
        print(f"{key[node]} é o nó filho esquerdo da chave {parent}.")
    else:
        print(f"{key[node]} é o nó filho direito da chave {parent}.")

    print_binary_search_tree(root, key, i, node - 1, key[node], True)
    print_binary_search_tree(root, key, node + 1, j, key[node], False)


def find_optimal_binary_search_tree(nodes):
    """
    Esta função calcula e imprime a árvore binária de busca ótima.
    https://en.wikipedia.org/wiki/Introduction_to_Algorithms

    """
    # Tree nodes must be sorted first, the code below sorts the keys in
    # increasing order and rearrange its frequencies accordingly.
    nodes.sort(key=lambda node: node.key)

    n = len(nodes)

    keys = [nodes[i].key for i in range(n)]
    freqs = [nodes[i].freq for i in range(n)]

    # This 2D array stores the overall tree cost (which's as minimized as possible);
    # for a single key, cost is equal to frequency of the key.
    dp = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # sum[i][j] stores the sum of key frequencies between i and j inclusive in nodes
    # array
    total = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
    # stores tree roots that will be used later for constructing binary search tree
    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]

    for interval_length in range(2, n + 1):
        for i in range(n - interval_length + 1):
            j = i + interval_length - 1

            dp[i][j] = sys.maxsize  # set the value to "infinity"
            total[i][j] = total[i][j - 1] + freqs[j]

            # Apply Knuth's optimization
            # Loop without optimization: for r in range(i, j + 1):
            for r in range(root[i][j - 1], root[i + 1][j] + 1):  # r is a temporal root
                left = dp[i][r - 1] if r != i else 0  # optimal cost for left subtree
                right = dp[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + total[i][j] + right

                if dp[i][j] > cost:
                    dp[i][j] = cost
                    root[i][j] = r

    print("Nós da Árvore Binária de Busca:")
    for node in nodes:
        print(node)

    print(f"\nO custo da Árvore Binária de Busca ótima para os nós da árvore é {dp[0][n - 1]}.")
    print_binary_search_tree(root, keys, 0, n - 1, -1, False)


def main():
    # Uma amostra de árvore binária com 10 nós
    nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]
    find_optimal_binary_search_tree(nodes)


if __name__ == "__main__":
    main()
