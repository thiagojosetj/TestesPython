import math

while True:
    entrada = input().strip()

    if entrada == "0":
        break

    a, b, c = map(int, entrada.split())

    if a == 0 or b == 0 or c == 0:
        break

    x = math.sqrt((100 * a * b) // c)
    print(f"{x:.0f}")