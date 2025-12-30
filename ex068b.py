from random import randint

linha = "=-=-=-=-=-=-=-" * 2
print(f"{linha}\nVAMOS JOGAR PAR OU ÍMPAR\n{linha}\n")

contador = 0

while True:
    computador = randint(1, 10)
    usuario = int(input("Diga um valor: "))
    opcao = input("Par ou Ímpar [P/I]: ").upper()

    soma = usuario + computador
    resultado_par = soma % 2 == 0

    print(f"Você jogou {usuario} e o computador {computador}. Total de {soma}", end=" ")

    if resultado_par:
        print("deu PAR")
    else:
        print("deu ÍMPAR")

    # vitória
    if (opcao == "P" and resultado_par) or (opcao == "I" and not resultado_par):               #Condições simplificadas da IA
        print("Você venceu!\n")
        contador += 1
    else:
        print("Você perdeu!")
        break

print(f"\nVocê acertou {contador} vezes")
