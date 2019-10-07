def readNumber():
    while(True):
        number = input("Insira um numero entre 0 e 100: ")
        if(int(number) > 0 and int(number) < 100):
            return number

def main():
    number = readNumber()

    if(len(number) == 2):
        print("Dezenas: " + number[1])
        print("Unidades: " + number[0])
    elif(len(number) == 1):
        print("Unidades: " + number[0])

main()