idade = int(input("Digite a idade do cliente: "))
renda = float(input("Digite a renda mensal do cliente: R$ "))

if idade < 18 or renda < 2000:
    categoria = "Bronze"
elif renda < 5000:
    categoria = "Prata"
elif renda < 10000:
    categoria = "Ouro"
else:
    categoria = "Diamante"

print(f"Categoria do cliente: {categoria}")
