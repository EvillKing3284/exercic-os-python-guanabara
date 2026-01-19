a = int(input("Digite um valor: "))
b = int(input("Digite um segundo valor: "))
c = int(input("Digite um terceiro valor: "))
d = int(input("Digite um quarto valor: "))
contador = 0
contador2 = 0
tupla = (a,b,c,d)
for percorrendo in tupla:
    if percorrendo % 2 == 0:
        contador2 += 1
    if percorrendo == 9:
        contador += 1
print(f"O valor 9 apareceu {contador} vezes")
if 3 in tupla:
    print(f"O valor 3 apareceu na posição {tupla.index(3) + 1}")
else:
    print("O valor 3 não aparece na tupla")
print(f"Os números pares foram: {contador2}")


