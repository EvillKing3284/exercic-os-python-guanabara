while True:
    usuario = int(input("Digite um número inteiro: "))
    if usuario < 0:
        print("Programa encerrado")
        break
    cont = 0 #tinha errado o redimensionamento da linha
    while True:
        cont += 1
        print(f"{usuario} x {cont} = {usuario * cont}")
        if cont > 10:
            break




