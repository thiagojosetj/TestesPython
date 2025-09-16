simb = input("Enter the symbol: ")
size = int(input("Enter the size of the grid: "))

for i in range(size):
    for j in range(size):
        print(simb, end=" ")
    print()