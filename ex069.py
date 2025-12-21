contador = contador2 = contador3 = contador4 = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ").upper())
    while sexo != "M" and sexo != "F":
        sexo = str(input("Digite seu sexo [M/F]: ").upper())    # or (OU lógico) → basta uma parte ser verdadeira
    opcao = str(input("Quer continuar [S/N]: ").upper())        # and (E lógico) → todas precisam ser verdadeiras
    while opcao != "S" and opcao != "N":
        opcao = str(input("Quer continuar [S/N]: ").upper())
    if sexo == "M":
        if idade < 20:
            contador4 += 1
    if sexo == "M":
        contador2 += 1
    if idade > 18:
        contador += 1
    if opcao == "N":
            break

print(f"Existem {contador} pessoas maiores de 18 anos\n{contador2} homens foram cadastrados\n{contador4} mulheres com menos de 20 anos")


