senha_correta = "python123"
tentativas = 0
acesso_liberado = False

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        acesso_liberado = True
        print("Acesso liberado!")
        break

    tentativas += 1
    print(f"Senha incorreta. Tentativas restantes: {3 - tentativas}")

if not acesso_liberado:
    print("Acesso bloqueado após 3 tentativas.")
