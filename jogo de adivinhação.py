import random
from fractions import Fraction

print("*" * 60)
print("Seja muito bem vindo(a) ao o jogo de adivinhação númerica")
print("*" * 60)

ajuda = input("Se precisar de ajuda digite 'help'\ncaso contrário aperte qualquer tecla para continuar: ")

if ajuda.lower() == "help":
    print('''\n   O seguinte programa faz um sorteio de números que pode estar entre quaisqueres números que você quiser.
Primeiramente, você terá que inserir a *quantidade de tentativas* que deseja. Após isso, você dirá 
*ENTRE* quais números o número sorteado vai estar. Por fim, teste sua sorte e chute o número

Muito obrigado e boa sorte! >:D''')


def jogo():
    contador = 0

    try:
        limite = int(input("\nInsira a quantidade de chances: "))
        valor1 = int(input("\nO número sorteado será um valor entre o número: "))
        valor2 = int(input("e: "))
        numero_secreto = random.randint(valor1, valor2)
    except ValueError:
        print("Digite apenas números inteiros")
        jogo()

    if limite <= 0:
        print("\nEsse programa apenas aceita números naturais. Insira apenas números não nulos positivos (1, 2, 3, 4, 5...) :/")
        jogo()

    while contador < limite:
        contador += 1

        try:
            tentativa = int(input(f"\nAdivinhe um numero entre {valor1} e {valor2}: "))
            if tentativa == numero_secreto:
                if contador == 1:
                    print(
                        f"\nWOOOOOOWW VOCÊ ACERTOOOOU EM APENAS UMA TENTATIVA!! ESTÁ COM SORTE EM!\nO NÚMERO SORTEADO REALMENTE ERA O {numero_secreto}")
                    break
                else:
                    print(
                        f"\nPARABÉNSSS!!! VOCÊ ACERTOU COM {contador} TENTATIVAS\nO NÚMERO SORTEADO REALMENTE ERA O {numero_secreto}")
                    break
            elif contador != limite:
                print("Você errou, mas ainda tem chances. Tente novamente!")

            else:
                print("\nVocê perdeu :(\nO número sorteado foi o {}".format(numero_secreto))
                print("Mais sorte da próxima vez...")

        except ValueError:
            print("Digite apenas números -.-'")
            jogo()

    try:
        probabilidade = limite/valor2
        probabilidade_simplificada = Fraction(limite, valor2)

        print(f"\nA probabilidade de acerto era de {probabilidade_simplificada} ou melhor dizendo de {probabilidade:.2%}")
        print("\nAbraços! :)\n")

    except ZeroDivisionError:
        print('Desculpe-me, mas não é possível calcular a probabilidade dessa tentativa :/')


try:
    jogo()
except:
    print("Vi aqui que você não digitou números algumas vezes... mais atenção! To de olho em rsrsrs")