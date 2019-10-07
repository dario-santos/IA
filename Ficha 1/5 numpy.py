import numpy as np

def lerMatriz(l, c):
    matriz = np.zeros([l,c], dtype=int)    
    for i in range(l):
        for j in range(c):
            matriz[i, j] = int(input("Inira o elemento da posicao [" + str(i) + ", " + str(j) + "]: "))
    return matriz

def main():
    print("Matriz A:")
    matriz1 = lerMatriz(2, 2)
    print("Matriz B: ")
    matriz2 = lerMatriz(2, 2)

    print("Soma das matrizes:\n", np.add(matriz1, matriz2))
    print("Multiplicação matricial:\n", np.matmul(matriz1, matriz2))
    print("Diferença de matrizes\n", np.subtract(matriz1, matriz2))
    print("Logaritmo de A\n", np.absolute(np.log(matriz1)))
    print("e) ", matriz1.max(1)[1] * matriz2.min(0)[0])

main()