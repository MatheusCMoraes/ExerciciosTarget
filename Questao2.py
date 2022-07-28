
c = 0
encerrar = False
Fibonnaci = list()
NF = 20 #numeros de termos a serem gerados

def calc_fibonnaci(N):
    """
    Calcula a sequencia de Fibonnaci
    :param N: representa os termos que serão calculados na sequencia, com limite igual a NF
    :return: retorna o valor de N ou o termo seguinte da séria de Fibonnaci, até NF
    """
    if N == 0 or N == 1:
        return N
    else:
        return calc_fibonnaci(N -2) + calc_fibonnaci(N -1)


while True:
    try:
        print("Questão 2 - Teste Target")
        NF = int(input("Deseja verificar quantos termos da série de Fibonnaci ? "))
    except (ValueError, TypeError):
        print("Erro! Digite um número inteiro valido!")
        continue
    except KeyboardInterrupt:
        print("\033[1;31mProgama interrompido pelo usuário.\033[m")
        encerrar = True
        break
    else:
        while c < NF: #armazena os termos em uma lista
            Termo = calc_fibonnaci(c)
            Fibonnaci.append(Termo)
            c += 1
    while True:
        if encerrar:
            break
        try:
            Num = int(input('Digite o valor que deseja verificar se está na seguência: '))
        except (ValueError, TypeError):
            print("Erro! Digite um número inteiro valido!")
            continue
        except KeyboardInterrupt:
            print("\033[1;31mProgama interrompido pelo usuário.\033[m")
            encerrar = True
            break
        else:
            print(f'A sequência de Fibonnaci para {NF} termos é:\n', Fibonnaci, '\n')

            if Num in Fibonnaci:
                print(f'O número {Num} pertence a sequencia de Fibonnaci')
            else:
                print(f'O número {Num} não pertence a sequencia de Fibonnaci')
            break

    if encerrar:
        print("Encerrando ...")
        break

    resp = str(input("Deseja verificar outro número? [S/N] "))
    if resp not in "SsNn":
        while True:
            print("Digite um resposta válida!")
            resp = str(input("Deseja verificar outro número? [S/N] "))
            if resp in "SsNn":
                break
    if resp in "Ss":
        continue

    if resp in "Nn":
        print("Encerrando ...")
        break


