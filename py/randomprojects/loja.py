import random

def geradordeestoque():
    morango = random.randint(1, 50)
    precomorango = random.uniform(5.50, 5.90)
    print(f'Há {morango:.0f} Morangos no Estoque')
    print(f'O Preço Do Morango HOJE está: {precomorango:.1f} R$')
    print(f'Com Isso temos {morango*precomorango:.0f}R$ em Estoque')
    return precomorango

def preconovodamercadoria():
    atualestoqueevalor = geradordeestoque()
    inputforced = 0
    while inputforced != 1:
        escolhadonovovalor = input(f'VOCÊ QUER TROCAR O VALOR DO PRODUTO? [SIM OU NÃO] \n ATUAL VALOR: R${atualestoqueevalor:.1f} \n').lower()
        if escolhadonovovalor == 'sim':
            print('PROCESSANDO...')
            atualestoqueevalor = float(input('ATUALIZE O VALOR: '))
            print(f'NOVO VALOR: R${atualestoqueevalor:.1f}')
            return atualestoqueevalor
        elif escolhadonovovalor == 'nao':
            print('PROCESSANDO...')
            print(f'SUA ESCOLHA FOI NÃO \n ATUAL VALOR: R${atualestoqueevalor:.1f}')
            return atualestoqueevalor
        elif escolhadonovovalor != 'nao' or escolhadonovovalor != 'sim':
            print('PROCESSANDO...')
            print('ESCOLHA ENTRE SIM OU NÃO')
    return atualestoqueevalor

def atualloja():
    estoque = preconovodamercadoria()

def menuloja():
    print('!!!LOJA COCOMACK!!!')
    print('VOCÊ QUER VER NOSSO ESTOQUE ATUAL?')
    escolhausuario = input('SIM OU NÃO').lower()
    return escolhausuario

if __name__ == '__main__':
    atualloja()
