name = input("Digite seu nome: ")
height = float(input("Digite sua altura (m): "))
weight = int(input("Digite seu peso (kg): "))

imc = weight / (height ** 2)

print(f"{name} tem {height}m de altura, pesa {weight}kg e seu IMC é {imc}")