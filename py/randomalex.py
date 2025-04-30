#BIBLIOTECA RANDOM

import random
opcao = 's' 
while opcao.lower() == 's':
    input('Pressione <Enter>')
    n = random.randint(0,10)
    print(n)
    opcao = input('Deseja continuar (s/n): ')
    if opcao == 'n' or opcao == 'N':
        print('LAÇO TERMINADO!')
        break
    
#ATIVIDADE 2. - PROF MIGNON

print('CASSINO ONLINE $$$')

def le_aposta():
    aposta = 0
    while aposta <= 2 or aposta >= 12:
        aposta = int (input('INFORME SUA APOSTA \n'))
        if aposta < 2 or aposta > 12:
            print('\tO Valor deve ser entre 2 e 12')
    return aposta

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f'Dado 1: {dados1}')
    print(f'Dado 2: `{dado2}')
    return dado1 + dado2

def mensagem(aposta,soma):
    if aposta == soma:
        print(f'VOCÊ GANHOU!!!')
    else:
        print(f'VOCÊ PERDEU!!!')
        

if __name__== '__main__':
    aposta = le_aposta()
    soma = lancar_dados()
    print(f'Valor apostado: {aposta}')
    mensagem(aposta, soma)


    


