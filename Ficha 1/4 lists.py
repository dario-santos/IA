def escreverLista():
    numeros = []
    
    while True :
        inserido = int(input("Insira um numero (negativo para sair): "))
        if inserido < 0 :
            break
        numeros.append(inserido)
    
    return numeros

def elementosMutuos(lista1, lista2):
    for i in lista1:
        if i in lista2:
            print(i, end= '')

def main():
    print("Primeira lista:")
    lista1 = escreverLista()
    print("Segunda lista:")
    lista2 = escreverLista()

    print("Valores mutuos:")
    elementosMutuos(lista1, lista2)

main()