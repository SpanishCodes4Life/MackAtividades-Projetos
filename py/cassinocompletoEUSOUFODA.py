import random


def le_aposta():
    aposta = 0
    while aposta < 2 or aposta > 12:
        aposta = int(input("Informe sua aposta: "))
        if aposta < 2 or aposta > 12:
            print("\tO valor deve ser entre 2 e 12.")
    return aposta


def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    return dado1 + dado2


def mensagem_dados(aposta, soma_dados):
    if aposta == soma_dados:
        print(f"Você venceu!")
    else:
        print(f"Você perdeu!")


def le_numero():
    numero = -1
    while numero < 0 or numero > 5:
        numero = int(input("Número: "))
        if numero < 0 or numero > 5:
            print("\tO valor deve ser entre 0 e 5")
    return numero


def le_par_impar():
    opcao = ""
    while opcao != "par" and opcao != "impar":
        opcao = input("Informe par ou impar: ").lower()
        if opcao != "par" and opcao != "impar":
            print("O valor deve ser par ou impar")
    return opcao


def gera_numero():
    return random.randint(0, 5)


def eh_par(n):
    return n % 2 == 0


def mensagem_par_impar(numero_usuario, opcao_usuario, numero_maquina):
    soma = numero_usuario + numero_maquina
    if eh_par(soma) and opcao_usuario == "par":
        print(f"Você venceu!")
    elif not eh_par(soma) and opcao_usuario == "impar":
        print(f"Você venceu!")
    else:
        print(f"Você perdeu!")


def joga_dados():
    aposta = le_aposta()
    print(f"Valor apostado: {aposta}")
    soma = lancar_dados()
    print(f"Soma dos dados: {soma}")
    mensagem_dados(aposta, soma)


def joga_par_impar():
    opcao_usuario = le_par_impar()
    numero_usuario = le_numero()
    numero_maquina = gera_numero()
    print(f"Número Gerado: {numero_maquina}")
    mensagem_par_impar(numero_usuario, opcao_usuario, numero_maquina)


def menu():
    print("*** CASSINO ***")
    print("1. Jogo de Dados")
    print("2. Jodo do Par ou Impar")
    print("3. Jogo da Pedra, Papel ou Tesoura")
    print("0. Sair")

    return int(input("Selecione uma opcao: "))

def escolhamaquinajoquempo():
    opcoesjoquempo = ('Pedra','Papel','Tesoura')
    randomizadordeescolha = random.choice(opcoesjoquempo).lower()
    print(f'A Máquina Escolheu: {randomizadordeescolha}')
    return randomizadordeescolha

def inputusuario():
    inputforced = 0
    while inputforced != 1:
        inputforced = input('Digite sua Escolha entre: \n [Pedra, Papel e Tesoura]').lower()
        if inputforced != 'pedra' and inputforced != 'papel' and inputforced != 'tesoura':
            print('A ESCOLHA DEVE SER ENTRE [PEDRA, PAPEL E TESOURA]')
        elif inputforced == 'pedra' or inputforced == 'papel' or inputforced == 'tesoura':
            print(f'Sua Escolha foi: {inputforced}')
            return inputforced

def vencedorjoquempo():
    escolhausuario = inputusuario()
    escolhamaquina = escolhamaquinajoquempo()

    if escolhausuario == 'pedra':
        if escolhamaquina == 'pedra':
            print('EMPATE :/')
        elif escolhamaquina == 'papel':
            print('VOCÊ PERDEU :/')
        elif escolhamaquina == 'tesoura':
            print('VOCÊ GANHOU :/')

    elif escolhausuario == 'papel':
        if escolhamaquina == 'pedra':
            print('VOCÊ GANHOU :/')
        elif escolhamaquina == 'papel':
            print('EMPATE :/')
        elif escolhamaquina == 'tesoura':
            print ('VOCÊ PERDEU :/')

    elif escolhausuario == 'tesoura':
        if escolhamaquina == 'pedra':
            print('VOCÊ PERDEU')
        elif escolhamaquina == 'papel':
            print('VOCÊ GANHOU')
        elif escolhamaquina == 'tesoura':
            print('EMPATE :/')


def jogojoquempo():
    winnerofgame = vencedorjoquempo()

if __name__ == "__main__":
    opcao = 1
    while opcao != 0:
        opcao = menu()
        if opcao == 1:
            joga_dados()
        elif opcao == 2:
            joga_par_impar()
        elif opcao == 3:
            jogojoquempo()
        elif opcao != 0:
            print(f"Opção Inválida")






