name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

if(name != "" and age > 0):
    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")
    if(' ' in name):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")

    print(f"Seu nome tem {len(name)} letras")
    print(f"A ultima letra do seu nome é {name[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")