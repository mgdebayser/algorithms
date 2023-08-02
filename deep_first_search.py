# Algoritmo DFS: Deep First Search
#
# Exemplo de problem:
# Dado um grafo representado por uma matriz binária 2D, este algoritmo encontra o número de componentes conectados
# Por exemplo:
# mat[][] = { {1,1,0,0,0}, {0,1,0,0,1}, {1,0,0,1,1}, {0,0,0,0,0}, {1,0,1,0,0}  }
# Número de ilhas: 5


class Graph:
    def __init__(self, i, j, A):
        self.ROW = i
        self.COL = j
        self.graph = A

    def isSafe(self, i, j, visited):
        # linha i e coluna j estão no limite do array, o valor do elemento é 1 e o elemento ainda não foi visitado
        return ( i>= 0 and i < self.ROW and j >=0 and j < self.COL and not visited[i][j] and self.graph[i][j]) 

    def DFS(self, i, j, visited):
        # Arrays utilizados para obter linha e coluna dos 8 vizinhos a visitar
        rowNbr = [-1,-1,-1,0,0,1,1,1]
        colNbr = [-1,0,1,-1,1,-1,0,1]

        visited[i][j] = True

        # Chama de forma recursiva todos os vizinhos conectados
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j+colNbr[k], visited):
                self.DFS(i+rowNbr[k], j+colNbr[k], visited)

    def countIslands(self):
        # Cria um array de boolean para marcar as células da matriz visitadas
        # Inicialmente, todas as células estão não visitadas
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]

        # Inicializa count com 0 e visita as células da matriz
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # se a célula com valor 1 não foi visitada ainda, então nova ilha foi encontrada
                if visited[i][j] == False and self.graph[i][j] == 1:
                    # visita todas as células na ilha e incrementa o contador de ilhas
                    self.DFS(i,j, visited)
                    count += 1
        return count
        
def main(G):
    print("Número de ilhas (componentes conectados) é: ", G.countIslands())


if __name__ == "__main__":
    graph = [ [1,1,0,0,0],
              [0,1,0,0,1],
              [1,0,0,1,1],
              [0,0,0,0,0],
              [1,0,1,0,1]]
    row = len(graph)
    col = len(graph[0])
    G = Graph(row, col, graph)
    main(G)
