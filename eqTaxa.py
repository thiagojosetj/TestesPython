def f(taxa, valor_inicial, pagamento_mensal, n):
    return valor_inicial - pagamento_mensal * (1 - (1 + taxa)**(-n)) / taxa

def f_prime(taxa, pagamento_mensal, n):
    num = taxa * n * (1 + taxa)**(-n - 1) - (1 - (1 + taxa)**(-n))
    den = taxa**2
    return -pagamento_mensal * ( num / den )

def encontrar_taxa(valor_inicial, pagamento_mensal, n, chute_inicial=0.01, tol=1e-10, max_iter=1000):
    i = chute_inicial
    for it in range(max_iter):
        fi = f(i, valor_inicial, pagamento_mensal, n)
        fpi = f_prime(i, pagamento_mensal, n)
        if fpi == 0:
            break
        novo_i = i - fi / fpi
        if abs(novo_i - i) < tol:
            return novo_i
        i = novo_i
    return i

valor_inicial = int(input("Valor a se empresta: "))
pagamento_mensal = int(input("Valor a se pagar mensalmente: "))
qnt_pagando = int(input("Numero de meses pagando: "))

taxa_mensal = encontrar_taxa(valor_inicial, pagamento_mensal, qnt_pagando, chute_inicial=0.01)
print(f"Taxa mensal aproximada: {taxa_mensal*100:.4f}% ao mês")
taxa_anual = (1 + taxa_mensal)**12 - 1
print(f"Taxa anual equivalente: {taxa_anual*100:.4f}% ao ano")