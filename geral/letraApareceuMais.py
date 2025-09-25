palavra = input("Digite uma frase sem numeros para realizar a contagem de qual a letra que mais aparece: ")
letra_atual = ''
qnt_mais_vezes = 0
qnt_mais_vezes_atual = 0
i = 0
while i < len(palavra):

    letra_atual = palavra[i]

    if letra_atual == ' ' or letra_atual == letra_mais_vezes:
        i += 1
        continue

    qnt_mais_vezes_atual = palavra.count(letra_atual)

    if(qnt_mais_vezes < qnt_mais_vezes_atual):
        letra_mais_vezes = letra_atual
        qnt_mais_vezes = qnt_mais_vezes_atual
    
    i += 1

print(type(letra_mais_vezes))
print(f"A letra que apareceu mais vezes foi a '{letra_mais_vezes}', ela apareceu {qnt_mais_vezes} vezes.")