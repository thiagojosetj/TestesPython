import os

os.system("cls")

print("=" * 100)
print("Jogo da forca, escolha uma palavra e peça para alguem acertar qual foi a palavra escolhida.")
print("Seram dadas 6 vidas até que se acerte a palavra")
print("=" * 100)

palavra_secreta = input("Digite a palavra escolhida: ")

os.system("cls")

count = 0
letras_usadas = set()
letras_acertadas = ''
erros = 0

while True:

    letra = input("Digite uma letra: ")

    if letra in letras_usadas:
        print("Você já usou essa letra, tente outra!")
        continue

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue

    if letra == "" or letra == " " or letra.isdigit():
        print("Digite uma letra.")
        continue

    letras_usadas.add(letra)

    count += 1

    if letra in palavra_secreta:
        letras_acertadas += letra
    else:
        erros += 1
        print(palavra_formada)
        if erros >= 6:
            print(f"Sinto muito, voce ja errou {erros} vezes.")
            break
        print(f"Cuidade, voce ja obteve {erros} erro(s).")
        continue
    
    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    if palavra_formada == palavra_secreta:
        break

    print(palavra_formada)
    print(f"Voce ja teve {count} tentativas.")

os.system("cls")

if palavra_formada == palavra_secreta:
    print("=" * 100)
    print(f"Voce acertou todas as letras da palavra {palavra_secreta} em {count} tentativas e obteve {erros} erro(s).")
    print("=" * 100)

else:
    print("=" * 100)
    print("Sinto muito!")
    print(f"Voce acertou todas as letras da palavra {palavra_secreta} em {count} tentativas.")
    print("=" * 100)