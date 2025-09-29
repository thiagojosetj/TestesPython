salary = float(input())

if salary <= 2000:
    print("Isento")
elif salary <= 3000:
    tax8 = (salary - 2000) * 0.08
    print(f"R$ {tax8:.2f}")
elif salary <= 4500:
    tax8 = 1000 * 0.08
    tax18 = (salary - 3000) * 0.18
    tax_total = tax8 + tax18
    print(f"R$ {tax_total:.2f}")
else:
    tax8 = 1000 * 0.08
    tax18 = 1500 * 0.18
    tax28 = (salary - 4500) * 0.28
    tax_total = tax28 + tax8 + tax18
    print(f"R$ {tax_total:.2f}")