"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O numero {num} é impar.")
except ValueError:
    print("O valor informado não é um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
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

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Digite seu primeiro nome: ")

tamanho_nome = len(nome)

if tamanho_nome < 4:
    print("Seu nome é curto.")
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print("Seu nome é normal.")
elif tamanho_nome > 6:
    print("Seu nome é muito grande.")