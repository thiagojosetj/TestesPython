palavra = input()
palavra_rev = ""
count = 0

for i in range(len(palavra)):
    palavra_rev += palavra[-1 - i]

for i in range(len(palavra)):
    if palavra[i] == palavra_rev[i]:
        count += 1

if count == len(palavra):
    if len(palavra) % 2 == 0:
        print("OFF")
    else:
        print("ON")
elif count == len(palavra) - 2:
    print("ON")
else:
    print("OFF")