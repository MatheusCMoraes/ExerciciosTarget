from matplotlib import pyplot

explode = [0, 0, 0, 0, 0]
Estados = ["SP", "RJ", "MG", "ES", "Outros"]
Faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

ValorTotal = 0
#valor em reais

print("Questão 4 - Teste Target")

for C in range(0, len(Faturamento)):
    ValorTotal += Faturamento[C]
    if Faturamento[C] == max(Faturamento):
        explode[C] = 0.05


print(f'O valor total do faturamendo do mês foi: R$ \033[34m{ValorTotal}\033[m')

for C in range(0, len(Faturamento)):
    PercentEstado = (Faturamento[C] / ValorTotal) * 100
    if Estados[C] == "Outros":
        print(f'{Estados[C]} Estados representaram {PercentEstado:.2f}% do total do faturamento.')
    else:
        print(f'O Estado de {Estados[C]} representou {PercentEstado:.2f}% do total do faturamento.')

#permite plotar o gráfico e destacar a área com melhor desempenho
pyplot.figure(figsize=(7, 7))
pyplot.pie(x=Faturamento, labels=Estados, explode=explode, autopct='%1.2f%%', shadow=True, startangle=90)
pyplot.show()
