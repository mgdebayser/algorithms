# Encontre a posição mais profunda de um elemento em uma pilha de números
#
# Dados de entrada: 
# A pilha que contém elementos E. 
# Um inteiro x, cuja posição mais profunda é a ser encontrada.
#
# Dados de saída:
# O índice da posição mais profunda do inteiro x.
#
# Restrições
# 1 <= N <= 100
# 1 <= E, c <= 100.000.000

def simple_stack(stack, x):
    result = 0
    index = len(stack)
    for i in range(0,len(stack)-1):
        if stack.pop() == x:
            result = i
    return result+1

if __name__ == "__main__":
    print("A pilha é:")
    stack = [10,20,10]
    print(stack)
    result = simple_stack(stack, 10)
    print("O índice mais profundo da pilha é: ", result)