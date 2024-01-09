def ImprimirEstrofe1():
    f01 = 'Erguei as mãos e dai glória a Deus \nErguei as mãos e dai glória a Deus \nErguei as mãos \nE cantai como os filhos do Senhor'
    print(f"{f01}\n ")

def ImprimirEAnimais1(animais01, animais02):
    f02 = 'Os animaizinhos subiram de dois em dois'
    for j in range(3):
        if j == 1:
            print("(Para não!)")
            continue
        print(f02)
        print(f02)
        print(animais01[j])
        print(f"E {animais02[j]}, como os filhos do Senhor\n ")

def ImprimirEstrofe15():
    f03 = "Deus disse a Noé: Constrói uma arca"
    for k in range (2):
        print(f03)
    f04 = "Que seja feita \nDe maneira para os filhos do Senhor"
    print(f"{f04}\n\nPor isso...!")  

def Parte1():
    animais01 = ['O elefante', 'A minhoquinha', 'O canguru']
    animais02 = ['os passarinhos', 'os pinguins', 'o sapinho']

    ImprimirEstrofe1()

    ImprimirEAnimais1(animais01, animais02)

    ImprimirEstrofe15()

    for i in range(3):
        ImprimirEstrofe1()

def ImprimirEstrofe2():
    f05 = "O Senhor tem muitos filhos \nMuitos filhos ele tem \nEu sou um deles, você também \nLouvemos ao senhor"
    print(f"{f05}\n ")

def ImprimirBDPD(iteracao,f06):
    f07 = "Braço direito"
    if iteracao > 0:
        f07 += ", braço esquerdo"
    if iteracao > 1:
        f07 += "\nPerna direita"
    if iteracao > 2:
        f07 += ", perna esquerda"
    if iteracao > 5:
        f07 += f"\n{f06}\nDá um pulinho"
    if iteracao > 6:
        f07 += " e abraça o irmão"        
    print(f"{f07}\n ")

def Parte2():
    for n in range(8):
        f06 = "Balança a cabeça, dá uma voltinha"
        if n == 5:
            print(f06[0:16])
        if n == 6:
            print(f06)

        ImprimirEstrofe2()
        ImprimirBDPD(n, f06)

while True:
    try:
        parte = input("Digite a parte da música que você gostaria - 0: Tudo / 1: 1º Parte / 2: 2º Parte / (Caso queira sair digite 'n'): ")
        
        if parte.lower() == 'n':
            break

        parte = int(parte)
        
        if parte == 1:
            print("-"*80)
            Parte1()
        elif parte == 2:
            print("-"*80)
            Parte2()
        elif parte == 0:
            print("-"*80)
            Parte1()
            print("E atenção agora, porque\n ")
            Parte2()
        else:
            print("Opção inválida. Por favor, escolha 0, 1, ou 2.")

    except ValueError:
        print("Valor inserido inválido. Por favor, insira um número válido.")




