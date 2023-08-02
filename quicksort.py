# Programa em Python para a implementação do algoritmo de ordenamento Quicksort

# Esta implementação utiliza o pivot como último elemento na lista,
# e o ponteiro mantem o elemento de menor valor como o pivot.
# No final da função partition(), o ponteiro é trocado com o pivot, de forma que
# a lista se torna ordenada de acordo com o pivot.

def partition(array, low, high, count):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
            if i!= j:
                count += 1
    # Inverte o elemento pivot com o elemento maior especificado por i
    (array[i+1], array[high]) = (array[high], array[i+1])
    if (i+1)!=high:
        count+=1
    # Retorna a posição a partir de onde se fez a partição, e quantas inversões foram feitas
    return i+1, count

def quickSort(array, low, high, count):
    if low < high:
        # encontra o índice do elemento na lista no qual o elemento à esquerda do pivot é menor e o elemento à direita é maior
        pi, count = partition(array, low, high, count)
        # chama o algoritmo de forma recursiva à esquerda
        count = quickSort(array, low, pi-1, count)
        # chama o algoritmo de forma recursiva à direita
        count = quickSort(array, pi+1, high, count)
    return count

def main(A):
    print("Array não ordenado")
    size = len(A)
    print(A, 0, size-1, 0)
    c = quickSort(A, 0, size-1, 0)
    print("Array ordenado de forma crescente:")
    print(A)
    print(c)

if __name__ == "__main__":
    main(A = [1, 7, 4, 1, 10, 9, -2])
    print("\n")
    main(A = [-1, 6,3,4,7,4])



            