print("Banco DEV")
saque = int(input("Quanto voçê quer sacar R$"))
total = saque
ced = 50
while True:
    if total >= ced:
        qtd = total // ced                 #Terceira forma com matematica pura
        total = total - (ced * qtd)
        print(f"O total dê {qtd} cédulas de R${ced} ")
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        if total == 0:
            break
