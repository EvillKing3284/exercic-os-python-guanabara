from time import sleep
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))
escolha = 0
while escolha != 5:
    print("[ 1 ]somar\n[ 2 ]multiplicar\n[ 3 ]maior\n[ 4 ]novos números\n[ 5 ]sair do programa")
    escolha = int(input("Qual a sua escolha: "))
    if escolha == 1:
        print(f"A soma entre {valor1} e {valor2} é {valor1 + valor2} ")
    elif escolha == 2:
        print(f"O produto entre {valor1} e {valor2} é {valor1 * valor2}")
    elif escolha == 3:
        valor_geral = max(valor1, valor2)
        valor_geral2 = min(valor1, valor2)
        print(f"O maior valor é {valor_geral} e o menor valor é {valor_geral2}")
    elif escolha == 4:
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    elif escolha == 5:
        print("Finalizando...")
        sleep(1)
        print("Volte sempre!! Programa finalizado")
    else:
        print("Código incorreto, tente novamente!")
        #Após revisar e estudar como fazer este código, consegui fazer sozinho, apenas com pequenos erros, porém está corrigido!
