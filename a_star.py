# Implementação do Algorítmo A Star em um Grafo representado por uma lista de adjacências.

from collections import deque

class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # função heurística com o mesmo valor 1 para todos os nós (simplificada)
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list é uma lista de nós que foram visitados, porém nem todos os vizinhos foram,
        #  é inicializada com o nó inicial
        # closed_list é uma lista de nós visitados e todos os nós vizinhos foram visitados
        open_list = set([start_node])
        closed_list = set([])

        # g contém a distância corrente do start_node para todos os outros nós
        g = {}

        g[start_node] = 0

        # parents contém um mapa de adjacêncis de todos os nós
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # busca um nó com o menor custo, isto é menor valor de f() - função de avaliação
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Caminho não existe')
                return None

            # se o nó corrente é o stop_node
            # então começamos a reconstruir o caminho a partir dele ao start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Caminho ótimo encontrado: {}'.format(reconst_path))
                return reconst_path

            # para todos os nós do nó corrente faça
            for (m, weight) in self.get_neighbors(n):
                # se o nó corrente não está nas listas open_list e closed_list
                # adiciona na open_list marca n como seu nó pai
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # senão, verifica se é mais rápido primeiro visitar n, e então m
                # se sim, atualiza os dados do nó pai e dados de g
                # se o nó está na closed_list, move para a open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from da open_list, e adiciona a closed_list
            # porque todos os seus nós vizinhos foram visitados
            open_list.remove(n)
            closed_list.add(n)

        print('Caminho não existe.')
        return None
    
if __name__ == "__main__":
    adjacency_list = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')