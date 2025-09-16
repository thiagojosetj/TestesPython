nome = input()
i = 0
nova_str = ''

while i < len(nome):
    letra = nome[i]
    nova_str += '*' + letra
    i += 1
print(nova_str)