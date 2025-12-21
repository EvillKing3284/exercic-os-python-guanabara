from random import randint
print(f"{"=-=-=-=-=-=-=-"*2}\nVAMOS JOGAR PAR OU ÍMPAR\n{"=-=-=-=-=-=-=-"*2}\n")
contador = 0
while True:

    computador = randint(1, 10)
    usuario = int(input("Diga um valor: "))
    opcao = str(input("Par ou Ímpar [P/I]: ").upper())
    soma = usuario + computador
    if soma % 2 == 0:
        print(f"Voçê jogou {usuario} e computador {computador}. Total de {soma} deu par")
    else:
        print(f"Voçê jogou {usuario} e computador {computador}. Total de {soma} deu ímpar")
    if opcao == "I":
        if soma % 2 != 0:
            resultado = "Voçê Venceu!"
            contador += 1
        if soma % 2 == 0:
            resultado = "Voçê perdeu"
            print(resultado)
            break
    elif opcao == "P":
        if soma % 2 == 0:
            resultado = "Voçê Venceu!"
            contador += 1
        if soma % 2 != 0:
            resultado = "Voçê perdeu!"
            print(resultado)
            break
    print(resultado)

print(f"Voçê acertou {contador} vezes")