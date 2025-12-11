from time import sleep
valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
jogador = int(input(">>>>>> Qual a sua opção: "))
if jogador == 1:
    print(f"A soma entre {valor1} + {valor2} é {valor1 + valor2}")
if jogador == 2:
    print(f"A multiplicação entre {valor1} x {valor2} é {valor2 * valor2}")
if jogador == 3:
    print("Maior:", max(valor1, valor2))
    print("Menor:", min(valor1, valor2))
if jogador == 5:
    print("Finalizando.....")
    sleep(2)
    print("-=-=-=-=-=-\nFim do programa! volte sempre!!")

while jogador == 4:
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite outro valor: "))
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    jogador = int(input(">>>>>> Qual a sua jogada: "))

    if jogador != 1 and jogador != 2 and jogador != 3 and jogador != 4 and jogador != 5:
        print("ERRO! TENTE NOVAMENTE")
        sleep(2)
        print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
        jogador = int(input(">>>>>> Qual a sua opção: "))

    if jogador == 1:
        print(f"A soma entre {valor1} + {valor2} é {valor1 + valor2}")
    if jogador == 2:
        print(f"A multiplicação entre {valor1} x {valor2} é {valor2 * valor2}")
    if jogador == 3:
        print("Maior:", max(valor1, valor2))
        print("Menor:", min(valor1, valor2))
    if jogador == 5:
        print("Finalizando.....")
        sleep(2)
        print("-=-=-=-=-=-\nFim do programa! volte sempre!!")



while jogador == 1 or jogador == 2 or jogador == 3:
    sleep(1)
    print("[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa")
    jogador = int(input(">>>>>> Qual a sua jogada: "))
    if jogador == 1:
        print(f"A soma entre {valor1} + {valor2} é {valor1 + valor2}")
    if jogador == 2:
        print(f"A multiplicação entre {valor1} x {valor2} é {valor2 * valor2}")
    if jogador == 3:
        print("Maior:", max(valor1, valor2))
        print("Menor:", min(valor1, valor2))
    if jogador == 5:
        print("Finalizando.....")
        sleep(2)
        print("-=-=-=-=-=-\nFim do programa! volte sempre!!")

#Boa tentativa, mas não funciona








