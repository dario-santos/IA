def ler(info="Introduza uma frase: "):
    return input(info)

def main():
    frase1 = set(ler())
    frase2 = set(ler())

    print("A e B:", frase1.union(frase2))
    print("A excepto B:", frase1.difference(frase2))
    print("A excepto B:", frase1.intersection(frase2))
    print("A excepto B:", frase1.symmetric_difference(frase2))

main()