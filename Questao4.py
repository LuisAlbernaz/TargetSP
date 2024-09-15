faturamento_estados = [
    ["SP", 67836.43],
    ["RJ", 36678.66],
    ["MG", 29229.88],
    ["ES", 27165.48],
    ["Outros", 19849.53]
]

faturamento_total = 0

for estado in faturamento_estados:
    faturamento_total += estado[1]
print(faturamento_total)

percentuais = []
for estado in faturamento_estados:
    percentual = (estado[1] / faturamento_total) * 100
    percentuais.append([estado[0], percentual])

for estado in percentuais:
    print(f"{estado[0]}: {estado[1]:.2f}%")



