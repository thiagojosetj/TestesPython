n = int(input())

lista = []
for i in range(n):
    palavra = input()
    lista.append(palavra)

for i in range(n):
    if(len(lista[i]) > 10):
        print(lista[i][0] + str((len(lista[i])-2)) + lista[i][int((len(lista[i])-1))])
    else:
        print(lista[i])