'''
JOEL - RA: 10737369
THEO - RA:
FELIPE - RA: 
'''


def Registradoreexercicio():
    print('\n***CADASTRO DE EXERCÍCIOS***')
    exercicio = input('INSIRA O EXERCÍCIO QUE FOI REALIZADO: ')
    tempoex = float(input('QUANTO TEMPO DE DURAÇÃO DO EXERCÍCIO: '))
    caloriasex = float(input('QUANTIDADE DE CALORIAS QUEIMADAS: '))
    diadasemanaex = input('DIA DA SEMANA QUE FOI REALIZADO: ').upper().strip()

    cadastroex = []
    lista_exercicios = []
    lista_duracao_ex = []
    lista_qtd_calorias = []
    lista_dia_da_semana = []
    
    cadastroex.append(exercicio)
    cadastroex.append(tempoex)
    cadastroex.append(caloriasex)
    cadastroex.append(diadasemanaex)

    print('\n---REGISTRO---')
    #print(f'EXERCÍCIO REALIZADO: {cadastroex[0]}\nTEMPO DE EXECUÇÃO: {cadastroex[1]} MINUTOS\nCALORIAS QUEIMADAS: {cadastroex[2]}\nDIA DA SEMANA: {cadastroex[3]}')
    return cadastroex


def relatoriodiario(cadastroex,exercicios,diadoexercicio):
    tempodex = 0
    qtddeex = 0
    caloriastotais = 0
    exrealizado = ''
    
    for cadastroex in exercicios:
        if cadastroex[3] == diadoexercicio:
            exrealizado += cadastroex[0]
            tempodex = tempodex + cadastroex[1]
            qtddeex +=1
            caloriastotais = caloriastotais + cadastroex[2]
            
            print(f'---\n---\n ---{diadoexercicio}---\n EXERCÍCIO REALIZADO: {exrealizado}\n TEMPO GASTO: {tempodex} MINUTOS\n CALORIAS GASTAS: {caloriastotais}\n---')


def exerciciosregistrados(exercicios, cadastroex):
    exercicios.append(cadastroex)

    
def sair_do_programa():
    return False


def menu():
    print('***Monitoramento de Exercícios e Saúde***\n')
    print('1.CADASTRO DE EXERCÍCIOS')
    print('2.RELATÓRIO DIÁRIO')
    print('3.CALCÚLO DE IMC')
    print('4.META SEMANAL')
    print('5.FRASES MOTIVACIONAIS')
    print('6.MÉDIA DE CALÓRIAS POR EXERCÍCIO')
    print('7.GRÁFICO DE CALORIAS POR EXERCÍCIO')
    print('8.ENCERRAR PROGRAMA')
    return int (input('ESCOLHA UMA DAS OPÇÕES: '))


def exibe_msg_opcao_invalida():
    print()
    print("=~" * 15)
    print('INSIRA UMA OPÇÃO VÁLIDA!!!')
    print("=~" * 15)
    print()

def exibe_msg_finalizando_prog():
    print()
    print("=~" * 15)
    print("Finalizando programa....")
    print("=~" * 15)
    print()

if __name__ == '__main__':
    exercicios = []
    main_menu = True
    opcao = 0


    while main_menu:
        opcao = menu()
        if opcao == 1:
            cadastroex = Registradoreexercicio()
            exerciciosregistrados(exercicios, cadastroex)

        elif opcao == 2:
            if not exercicios:
                print('---NENHUM EXERCÍCIO REGISTRADO---')
            elif exercicios:
                print('---RELATÓRIO DIÁRIO---')
                diadoexercicio = input('DIA DA SEMANA: ').upper().strip()
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

        elif opcao == 8:
            exibe_msg_finalizando_prog()
            main_menu = sair_do_programa()
            
        else:
            exibe_msg_opcao_invalida()
            
