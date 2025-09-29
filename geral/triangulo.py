a, b, c = map(float, input().split())

a, b, c = sorted([a, b, c], reverse=True)

if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    elif a ** 2 > b ** 2 + c ** 2:
        print("TRIANGULO OBTUSANGULO")
    elif a ** 2 < b ** 2 + c ** 2:
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    if (a == b and a != c) or (b == c and b != a) or (a == c and a != b):
        print("TRIANGULO ISOSCELES")
