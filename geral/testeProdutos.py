prod1 = input("Digite o nome do primeiro produto: ")
preco1 = float(input("Digite o valor do primeiro produto: "))
prod2 = input("Digite o nome do primeiro produto: ")
preco2 = float(input("Digite o valor do primeiro produto: "))
prod3 = input("Digite o nome do primeiro produto: ")
preco3 = float(input("Digite o valor do primeiro produto: "))

total_pre = preco1 + preco2 + preco3

print("=" * 30)
print(f"Recibo de compra".center(30))
print("=" * 30)

print(f"{'':<2}{prod1:<15} R${preco1:>7.2f}")
print(f"{'':<2}{prod2:<15} R${preco2:>7.2f}")
print(f"{'':<2}{prod3:<15} R${preco3:>7.2f}")

print("=" * 30)

print(f"{'':<2}{'TOTAL':<15} R${total_pre:>7.2f}")