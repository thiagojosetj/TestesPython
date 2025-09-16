continuar = True

while continuar:
    num1 = input("Digite o primeiro valor: ")
    num2 = input("Digite o segundo valor: ")
    op = input("Escolha uma das operações para realizar(+-*/): ")
    num_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_validos = True
    except:
        num_validos = None
    
    if(num_validos):
        sum = num1_float + num2_float
        sub = num1_float - num2_float
        div = num1_float / num2_float
        mult = num1_float * num2_float

        if(op not in "*/-+"):
            print("Digite um operador válido.")
            continue
        else:
            if(len(op) > 1):
                print("Digite apenas 1 operador.")
                continue

        if(op == '+'):
            print(f"O resultado da operação é {sum}")
        if(op == '-'):
            print(f"O resultado da operação é {sub}")
        if(op == '/'):
            print(f"O resultado da operação é {div}")
        if(op == '*'):
            print(f"O resultado da operação é {mult}")

        continuar = input("Deseja realizar mais uma operação? [S]sim ou [N]não   ").lower().startswith('s')
    else:
        print("Escolha números válidos.")
        continue