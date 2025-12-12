fatorial = int(input("Digite um número: "))
multiplicacao = 1
for c in range(fatorial,0,-1):
    if c != 1:
        print(f"{c}",end=" x ")
        multiplicacao = multiplicacao * c
    else:
        print(f"{c} = {multiplicacao}")
