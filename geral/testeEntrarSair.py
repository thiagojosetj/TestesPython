entrada = input("Voce deseja entrar ou sair: ").lower()

if(entrada == "entrar"):
    print("Você entrou no sistema.")
elif(entrada == "sair"):
    print("Você saiu do sistema.")
else:
    print("Comando inválido. Digite uma opção válida.")