print("Banco DEV")
saque = int(input("Quanto voçê quer sacar R$"))
total = saque
ced = 50
while True:
    if total >= ced:
        qtd = total // ced
        print(f"O total de {qtd} cédulas de R${ced} ")
        total %= ced              #Quanto sobra de resto da divisão da primeira cédula, e assim por diante: 50, 20, 10, 5 e 1
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        if total == 0:
            break
