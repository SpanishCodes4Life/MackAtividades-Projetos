import random

def le_numero():
    numero = -1
    while numero < 0 or numero > 5:
        numero = int (input('Número: '))
        if numero < 0 or numero > 5:
            print('O Valor deve ser entre 0 e 5')
    return numero

def le_par_impar():
    opcao = ''
    while opcao != "par" and opcao != 'impar':
        opcao = input('Informe par ou impar: ').lower()
        if opcao!= 'par' and opcao != 'impar':
            print ('O Valor deve ser Par ou Impar')

def gera_numero():
    return random.randint(0 , 5)



def ehpar(n):
    return n % 2 == 0


def mensagem_par_impar(numero,opcao_usuario, numero_maquina):
    soma =  numero_usuario + numero_maquina
    if ehpar(soma) and opcao_usuario == 'par':
        print(f'Você Venceu"')
    elif not ehpar(soma) and opcao_usuario == 'impar':
        print('Você Venceu!!!')
    else:
        print(f'Voce Perdeu :/ ')

if __name__ == '__main__':
    opcao_usuario = le_par_impar()
    numero_usuario = le_numero()
    numero_maquina = gera_numero()
    print(f'Número Gerado: {numero_maquina}')
    mensagem_par_impar(numero_usuario, opcao_usuario, numero_maquina)
