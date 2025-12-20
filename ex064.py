usuario = 0
soma = 0
contador = 0
while usuario != 999:
    contador = contador + 1
    soma = soma + usuario
    usuario = int(input("Digite um número [999 para parar]: "))


else:
    print(f"Voçê digitou {contador} números e a soma entre eles foi {soma} ")


