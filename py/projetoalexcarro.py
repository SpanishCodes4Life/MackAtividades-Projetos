# 1. Cadastro das Informações
Placa = (input("Placa do veículo: \n"))
Nome = input("Nome do motorista: \n")
Velocidade = int(input("Velocidade registrada: \n"))
Velocidade_maxima = int(input("Velocidade máxima permitida na via: \n"))
Multa = input("Já foi multado anteriormente?  \n")

#if Multa == "sim"#

# 2. Classificação da Infração
def classificacao_infracao(Velocidade, Velocidade_maxima):
    if Velocidade <= Velocidade_maxima:
        return "Nenhuma Infração"
    elif (Velocidade_maxima * 1.20) >= Velocidade:
        return "Infração Leve!"
    elif (Velocidade_maxima * 1.20) >= Velocidade <= (Velocidade_maxima * 1.50):
        return "Infração Grave!!"
    elif (Velocidade_maxima * 1.50) <= Velocidade:
        return "Infração Gravissíma!!!"

classificacao = classificacao_infracao(Velocidade, Velocidade_maxima)
print(classificacao)

# 3. Cálculo de Penalidades
def calculo_penalidade(Velocidade, Velocidade_maxima):

    if (Velocidade_maxima * 1.20) >= Velocidade:
        return "Infração Leve! - Multa de R$ 130,16"
    elif (Velocidade_maxima * 1.20) >= Velocidade <= (Velocidade_maxima * 1.50):
        return "Infração Grave!! - Multa de R$ 195,23, 5 pontos na CNH"
    elif (Velocidade_maxima * 1.50) <= Velocidade:
        return "Infração Gravissíma!!! - MUlta de R$ 880,41, 7 pontos na CNH e SUSPENSÃO DA CARTEIRA"

calculo = calculo_penalidade(Velocidade, Velocidade_maxima)
print(calculo)

# 4. Verificação de Reincidência#FAZER TEST COM'SIM,'S',Sim,'sim'.... BÁSICO FEITO

def verificacao_reincidencia(Multa, Velocidade, Velocidade_maxima):
    if Multa == 'Sim' and (Velocidade_maxima * 1.20) >= Velocidade <= (Velocidade_maxima * 1.50):
        print("Haverá dobramento do valor da multa por reincidência", (195.23 * 2),"$Reais")
        return print ('ATENÇÃO: Multa DOBRADA por reincidência!')
    elif Multa == 'Sim'and (Velocidade_maxima * 1.50) <= Velocidade:
        print('Haverá dobramento do valor da multa por reincidência', (880.41 * 2),'$Reais')
        return print('ATENÇÃO: Multa DOBRADA por reincidẽncia!')
    else:
        return print ('Não há dobramento do valor por reincidência')

verificacao = verificacao_reincidencia(Multa, Velocidade, Velocidade_maxima)

# 5. Curso de Reciclagem

def curso_reciclagem(Velocidade,Velocidade_maxima):
    if (Velocidade_maxima * 1.50) <= Velocidade:
        print('Você deve realizar um Curso de Reciclagem - Infração Gravissíma!!!')
    else:
        print('Sem Nenhum Curso de Reciclagem.')
curso = curso_reciclagem(Velocidade,Velocidade_maxima)
print(curso)

# 6. Simulação de Pagamento da Multa

Pagamento = input ("Deseja pagar a multa agora? ")

def pagamento_multa(Multa,Velocidade,Velocidade_maxima):
        #if (Pagamento == 'sim' or 'Sim') and (Velocidade * 1.20) <= Velocidade_maxima:
            ("Haverá um desconto de 20% sobre o valor de R$ 135,16 = R$", (135,16 / 0.20) - 135,16)
            if (Pagamento == 'sim' or 'Sim') and (Velocidade * 1.20) >= Velocidade_maxima <= (Velocidade * 1.50):
                print("Haverá um desconto de 20% sobre o valor de R$ 195,23 = R$", (195,23 / 0.20) - 195,23)
            if (Pagamento == 'sim' or 'Sim') and (Velocidade * 1.50) > Velocidade_maxima:
                print("Haverá um desconto de 20% sobre o valor de R$ 880,41 = R$", (880,41 / 0.20) - 880,41)
                if not Pagamento == 'sim' or 'Sim':
                    print('O Pagemento ')
pagamento = pagamento_multa()
print(pagamento)#