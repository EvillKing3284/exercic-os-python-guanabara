usuario = "".upper()
contador = 0
somador = 0
maior = None
menor = None
while usuario != "N":
    resposta = int(input("Digite um número: "))
    usuario = str(input("Quer continuar? [S/N]: ")).upper()
    contador = contador + 1
    somador = somador + resposta
    if maior is None:
        maior = resposta
        menor = resposta
    else:
        maior = max(maior, resposta)
        menor = min(menor, resposta)

if usuario == "N":
       media = somador / contador
       print(f"A média de todos os valores é : {media:.2f}")
       print(f" O maior número é {maior}\n E o menor é {menor}")
