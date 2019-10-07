def ler(info="Introduza uma frase: "):
    return input(info)

def gravar(filePath, content):
    f = open(filePath, "w")
    f.write(content)
    f.close()

def conta_vogais(frase):
    cnt = 0
    for c in frase:
        if c in "aeiouAEIOU" :
            cnt += 1
    return cnt

def main():
    primeira_frase = ler()
    segunda_frase = ler()
    filePath = ler("Insira o nome do ficheiro a escrever ")
    if(conta_vogais(primeira_frase) > conta_vogais(segunda_frase)):
        gravar(filePath, primeira_frase)
    else:
        gravar(filePath, segunda_frase)

main()