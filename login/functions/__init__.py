def lines(formato="-", tamanho=50, texto=False):

    if not texto:
        print(formato * tamanho)

    else:
        print(formato * tamanho)
        print(f"{texto}".center(tamanho))
        print(formato * tamanho)


def menu(*texto):
    quantidade = len(texto)

    lines(texto="Central")
    for numeracao, txt in enumerate(texto):
        print(f"{numeracao + 1} - {txt}")
    lines()

    while True:

        try:
            escolha = int(input("Your option > "))

            if 1 <= escolha <= quantidade:
                return escolha
            else:
                print("Opção inválida!")
        except:
            print("Erro! Digite um valor válido!")
