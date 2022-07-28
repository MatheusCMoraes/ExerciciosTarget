import json

menorFaturamento = 0
maiorFaturamento = 0
mediaMensal = 0
diasComFaturamento = 0

print("Questão 3 - Teste target")

with open("dados.json") as DadosFaturamento:
    data = json.load(DadosFaturamento)
    # os dados de faturamento estão em uma lista, com dicionários em seus indíces.
    # os dicionários se dividem em 'dia' e 'valor'

resp = str(input("Deseja mostrar os dados do faturamento? [S/N] "))
if resp in "sS":
    for dia, v in enumerate(data): #dia se refere ao índice, ordena os dados do arquivo JSON
        print(f'dia {dia+1} -- faturamento {data[dia]["valor"]}')
elif resp not in "SsNn":
    print("Opção incorreta, o faturamento não será mostrado.")

for c in range(0, len(data)):
    if c == 0 and data[c]['valor'] != 0:
        menorFaturamento = data[0]['valor']
        maiorFaturamento = data[0]['valor']
    elif c == 0 and data[c]['valor'] == 0: #deve-se evitar que o primeiro dado atribuido seja nulo
        B = c                              #utilizei B para que o valor de c não sofresse alteração
        while data[B]['valor'] == 0:       #vamos atribuir até achar um valor não nulo
            maiorFaturamento = menorFaturamento = data[B]['valor']
            B += 1
    else: #atribui os menores e maiores valores
        if data[c]['valor'] > maiorFaturamento:
            maiorFaturamento = data[c]['valor']
        if data[c]['valor'] < menorFaturamento and data[c]['valor'] != 0:
            menorFaturamento = data[c]['valor']

    if data[c]['valor'] != 0: #para excluir os dias nulos do calculo da média
        mediaMensal = data[c]['valor']
        diasComFaturamento += 1

mediaMensal /= diasComFaturamento

print(f'\nO maior faturamento registrado foi: {maiorFaturamento}\n')
print(f'O menor faturamento registrado foi: {menorFaturamento}\n')
print(f'A média mensal registrada foi:  {mediaMensal:.4f}')

