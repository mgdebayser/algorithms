
# Implementação demonstrando uma Fila em Python


from queue import Queue

# Inicialização
q = Queue(maxsize = 3)

# qsize() retorna o tamanho da Fila
print(q.qsize())

# Adiciona elementos à fila
q.put('a')
q.put('b')

# Return Boolean se a fila está cheia
print("\nCheia: ", q.full())

q.put('c')

# Return Boolean se a fila está cheia
print("\nCheia: ", q.full())

# Remoção de elementos da fila
print("\nElementos desenfileirados da fila: ")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean se a fila está vazia
print("\nVazia: ", q.empty())

q.put(1)
print("\nVazia: ", q.empty())
print("Cheia: ", q.full())