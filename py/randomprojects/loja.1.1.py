import random

def geradordeestoquehoje():
    estoquehoje = random.randint(1,100)
    return estoquehoje

def geradorprecoproduto():
    precodehojeproduto = random.uniform(5.9,7)
    return precodehojeproduto

def vendoestoquehoje():
    estoque = geradordeestoquehoje()
    precoproduto = geradorprecoproduto()

    nomeproduto = input('Digite o nome do produto: ')
    print(f'TEMOS {estoque} {nomeproduto} NO NOSSO ESTOQUE DE HOJE')
    print(f'O PREÇO DO {nomeproduto} ESTÁ COTADO HÁ R${precoproduto:.1f}')
    print(f'COM ISSO TEMOS R${estoque*precoproduto:.1f} DE {nomeproduto}')

    x=0
    while x != 1:

        choiceuserprice = input(f'VOCÊ QUER ATUALIZAR O VALOR DO PRODUTO {nomeproduto} \n [SIM OU NÃO] \n ').lower()
        if choiceuserprice == 'sim' or choiceuserprice == 's':
            precoproduto = float(input(f'DIGITE O VALOR DO PRODUTO: \n COTAÇÃO ATUAL R$ {precoproduto:.1f} \n ENTRE R$5.9 A R$7.0 \n'))
            if precoproduto < 5.9 or precoproduto > 7.0:
                print('DIGITE ENTRE OS VALORES MÍNIMOS E MÁXIMO!')
            elif precoproduto >= 5.9 or precoproduto <= 7.0:
                print('PROCESSANDO...')
                print(f'NOVO VALOR DEFINIDO. \n R${precoproduto:.1f}')
                return precoproduto

        elif choiceuserprice == 'nao' or choiceuserprice == 'n' or choiceuserprice == 'não':
            print('PROCESSANDO...')
            print(f'O VALOR ATUAL SERÁ MANTIDO.')
            return precoproduto

        elif choiceuserprice != 'sim' or choiceuserprice != 'nao' or choiceuserprice != 'n' or choiceuserprice != 's' or choiceuserprice != 'não':
            print('PROCESSANDO...')
            print('---!!!ESCOLHA ENTRE SIM OU NÃO!!!---')

    print(f'TEMOS {estoque} {nomeproduto} NO NOSSO ESTOQUE DE HOJE')
    print(f'O PREÇO DO {nomeproduto} ESTÁ COTADO HÁ R${precoproduto:.1f}')
    print(f'COM ISSO TEMOS R${estoque*precoproduto:.1f} DE {nomeproduto}')

vendoestoquehoje()