frase = input()
find_in_frase = input()

palavras = frase.split()

if find_in_frase in palavras:
    resultado = []
    for p in palavras:
        if p == find_in_frase:
            resultado.append("*")
        else:
            resultado.append(p)
    print(" ".join(resultado))
else:
    print("tudo certo :)")