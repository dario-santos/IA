# Adicionar elemento
# Alterar valor 
# Mostrar todos os elementos
# Mostrar nota mais alta

def main():
    notas = {}

    while True :
        print("Gestão das Notas")
        print("1 - Adicionar Unidade Curricular")
        print("2 - Alterar nota")
        print("3 - Visualizar nota mais alta")
        print("4 - Visualizar o dicionario\n")
        print("0 - sair")
        inserido = int(input("Insira uma opcao: "))
        
        if inserido == 0:
            break
        elif inserido == 1:
            uc = input("Qual a unidade curricular: ")
            nota = int(input("Qual a nota: "))
            notas.update({uc: nota})
        elif inserido == 2:
            uc = input("Qual a unidade curricular: ")
            nota = int(input("Qual a nota: "))
            notas[uc] = nota
        elif inserido == 3:
            print(max(notas.values()))
        elif inserido == 4:
            print(notas)

main()