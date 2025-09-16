try:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O numero {num} é impar.")
except ValueError:
    print("O valor informado não é um número inteiro.")

try:
    num = int(input("Que horas são agora? "))
    if num >= 0 and num <= 11:
        print("Bom dia!")
    elif num >= 12 and num <= 17:
        print("Boa tarde!")
    elif num >= 18 and num <= 23:
        print("Boa noite!")
    else:
        print("Horário inválido.")
except ValueError:
    print("O valor informado não é um número inteiro.")

nome = input("Digite seu primeiro nome: ")

tamanho_nome = len(nome)

if tamanho_nome < 4:
    print("Seu nome é curto.")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print("Seu nome é normal.")
elif tamanho_nome > 6:
    print("Seu nome é muito grande.")