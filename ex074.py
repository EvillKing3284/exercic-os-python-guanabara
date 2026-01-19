from random import randint
maior_numero = 0
menor_numero = None
tupla = (randint(1,10),randint(1,10),randint(1,10),randint(1,10))
for c in tupla:
    if c > maior_numero :
        maior_numero = c
    if menor_numero is None or c < menor_numero:
        menor_numero = c

print(f"Os valores sorteados foram: {" ".join(map(str,tupla))}") #revisar esta técnica com map
#Esse primeiro print poderia ser feito de outra forma mais fácil, tipo assim:
#for c in tupla:
    #print(c,end=" ")
print(f"O maior valor sorteado foi: {maior_numero}")
print(f"O menor valor sorteado foi: {menor_numero}")