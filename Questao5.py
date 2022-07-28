def inverter(msg):
    string2 = ""
    indice = len(msg)
    while indice:
        indice -= 1
        string2 += msg[indice]
    return string2


print("Questão 5 - Teste Target")
string = str(input("Digite uma string: "))

print(f'A string invertida é {inverter(string)}.')

#print(f'A string invertida é: {string[::-1]}\n') -- outra alternativa