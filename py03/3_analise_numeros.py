numeros = []

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
