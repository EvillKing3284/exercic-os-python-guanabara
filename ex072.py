numeros = ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez",
           "onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito",
           "dezenove","vinte")
usuario = str(input("Digite um número entre 0 e 20: "))
while not str(usuario).isnumeric() or not (0 <= int(usuario) <= 20): #1º OBS: Achei interessante o uso do isnumeric junto com not
        usuario = str(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f"Voçê digitou o número {numeros[int(usuario)]}")
