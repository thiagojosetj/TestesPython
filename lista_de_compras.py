import os

list_compras = []

while True:
    opcao = input("Selecione uma opção \n[i]nserir [a]pagar [l]istar: ")

    if opcao.lower() == 'i':
        os.system("cls")
        list_compras.append(input("Valor: "))
    elif opcao.lower() == 'a':
        if len(list_compras) == 0:
            os.system("cls")
            print("A lista está vazia.")
            continue
        else:
                try:
                    os.system("cls")
                    for i, valor in enumerate(list_compras):
                        print(i, valor)
                    list_compras.pop(int(input("Escolha o indice para apagar: ")))
                    os.system("cls")
                except ValueError:
                    os.system("cls")
                    print("Por favor, digite um número inteiro.")
                    continue
                except IndexError:
                    os.system("cls")
                    print("Indicie fora do range da lista.")
                except Exception:
                    os.system("cls")
                    print("Erro desconhecido.")
    elif opcao.lower() == 'l':
        if len(list_compras) > 0:
            os.system("cls")
            for i, valor in enumerate(list_compras):
                print(i, valor)
        else: 
            print("A lista está vazia.")
            continue
    else:
        os.system("cls")
        print("Opção inválida.")