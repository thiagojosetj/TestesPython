n = int(input())

x = 0

for i in range(n):
    inc = input()
    if(inc == "++X" or inc == "X++"):
        x += 1
    elif(inc == "--X" or inc == "X--"):
        x -= 1
    
print(x)