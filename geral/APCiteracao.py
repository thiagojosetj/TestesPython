import math

def escolheOperacao():
    while True:
        print("### CALCULADORA ###")
        print()
        print("1- Raiz quadrada aproximada")
        print("2- Raiz cubica aproximada")
        print("3- Numero de fibonacci")
        print()
        ope = int(input("Digite o numero da operação desejada: "))
        if ope > 3:
            print("Ecolha uma opção válida!")
        if ope > 0 and ope <= 3:
            return ope

def raizAproximada(num, n):
    epsilon = 0.0001
    est = num
    while True:
        if n == 2:
            nova_est = (est + num/est) / 2
        elif n == 3:
            nova_est = (2 * est ** 3 + num) / (3 * est ** 2)
        
        if abs(nova_est - est) < epsilon:
            break
        est = nova_est
    return nova_est

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        num1 = 0
        num2 = 1
        i = 2
        while i <= num:
            res = num1 + num2
            num1 = num2
            num2 = res
            i += 1
        return res

while True:
    ope = escolheOperacao()
    num = int(input("Digite um numero inteiro: "))

    if ope == 1:
        print(f"A raiz quadrada de {num} é {raizAproximada(num, 2):.2f}")
    elif ope == 2:
        print(f"A raiz cubica de {num} é {raizAproximada(num, 3):.2f}")
    elif ope == 3:
        print(f"O {num} de Fibonacci é {fib(num)}")

    if input("Deseja realizar outra operação? [s]sim ou [n]nao: ").lower().startswith('n'):
        break

#print(f"Raiz quadrada de {num} é {num ** (1/2)}")
#print(f"Raiz cubica de {num} é {num ** (1/3)}")