
def Registradoreexercicio():
    print('***CADASTRO DE EXERCÍCIOS***')
    exercicio = input('INSIRA O EXERCÍCIO QUE FOI REALIZADO: ')
    tempoex = float(input('QUANTO TEMPO DE DURAÇÃO DO EXERCÍCIO: '))
    caloriasex = float(input('QUANTIDADE DE CALORIAS QUEIMADAS: '))
    diadasemanaex = input('DIA DA SEMANA QUE FOI REALIZADO: ').lower()

    cadastroex = []
    cadastroex.append(exercicio)
    cadastroex.append(tempoex)
    cadastroex.append(caloriasex)
    cadastroex.append(diadasemanaex)

    print('---REGISTRO---')
    print(f'EXERCÍCIO REALIZADO: {cadastroex[0]}\nTEMPO DE EXECUÇÃO: {cadastroex[1]} MINUTOS\nCALORIAS QUEIMADAS: {cadastroex[2]}\nDIA DA SEMANA: {cadastroex[3]}')
    return cadastroex

def relatoriodiario(cadastroex,exercicios,diadoexercicio):
    tempodex = 0
    qtddeex = 0
    caloriastotais = 0

    for cadastroex in exercicios:
        if cadastroex[3] == diadoexercicio:
            tempodex = tempodex + cadastroex[1]
            qtddeex +=1
            caloriastotais = caloriastotais + cadastroex[1]
    if qtddeex > 0:
        return caloriastotais / qtddeex
    else:
        return 0.0


def exerciciosregistrados(exercicios, cadastroex):
    exercicios.append(cadastroex)

def menu():
    print('***MENU***')
    print('1.CADASTRO DE EXERCÍCIOS')
    print('2.RELATÓRIO DIÁRIO')
    print('3.CALCÚLO DE IMC')
    print('4.META SEMANAL')
    print('5.FRASES MOTIVACIONAIS')
    print('6.MÉDIA DE CALÓRIAS POR EXERCÍCIO')
    print('7.GRÁFICO DE CALORIAS POR EXERCÍCIO')
    return int (input('ESCOLHA UMA DAS OPÇÕES: '))

if __name__ == '__main__':
    exercicios = []
    opcao = 0

    while opcao != -1:
        opcao = menu()
        if opcao == 1:
            cadastroex = Registradoreexercicio()
            exerciciosregistrados(exercicios, cadastroex)

        elif opcao == 2:
            if not exercicios:
                print('---NENHUM EXERCÍCIO REGISTRADO---')
            elif exercicios:
                print('---RELATÓRIO DIÁRIO---')
                diadoexercicio = input('DIA DA SEMANA: ')
                relatoriodiario(cadastroex,exercicios,diadoexercicio)

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass

        elif opcao == 5:
            pass

        elif opcao == 6:
            pass

        elif opcao == 7:
            pass

        elif opcao < 0 or opcao > 7:
            print('INSIRA UMA OPÇÃO VÁLIDA!!!')
