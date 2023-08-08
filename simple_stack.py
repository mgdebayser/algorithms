# Encontre a posição mais profunda de um elemento em uma pilha de números
#
# Dados de entrada: 
# A pilha de tamanho N que contém elementos E. 
# Um inteiro x, cuja posição mais profunda é a ser encontrada.
#
# Dados de saída:
# O índice da posição mais profunda do inteiro x.
#
# Restrições
# 1 <= N <= 100
# 1 <= E, x <= 100.000.000

def simple_stack(stack, x):
    result = 0
    index = len(stack)
    if index < 1 or index > 100:
        print("O tamanho da pilha tem que ser entre 1 e 100.")
        return False
    
    if x < 1 or x > 100000000:
            print("O elemento buscado precisa ser um inteiro entre 1 e 10ˆ8.")
            return False
    
    for i in range(0,len(stack)):
        e = stack.pop()
        if e < 1 or e > 100000000:
            print("Todos os elementos da pilha precisam ser inteiros entre 1 e 10ˆ8.")
            return False
        if e == x:
            result = i

    return result+1

if __name__ == "__main__":
    print("A pilha é:")
    stack = [10,20,10]
    print(stack)
    result = simple_stack(stack, 10)
    print("O índice mais profundo da pilha é: ", result)

    print("A pilha é:")
    stack = [-1,20,10]
    print(stack)
    result = simple_stack(stack, 10)

    print("A pilha é:")
    stack = [10,20,10]
    print(stack)
    result = simple_stack(stack, -1)