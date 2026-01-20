tupla = ("aprender","programar","linguagem","python","curso","gratis","estudar","praticar","trabalhar","mercado","programar","futuro")
for c in tupla:
    print(f"\nNa palavra {c.upper()} temos: ", end="")
    for palavra in c:
        if palavra.upper() in "AEIOU":
            print(f"{palavra.upper()}", end=" ")