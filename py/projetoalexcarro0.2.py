#---FUNÇÕES--#

# 2. Classificação da Infração
def classificacao_infracao(Multa,pagamento_m,Velocidade, Velocidade_maxima):
    infra_l= 0
    infra_g= 0
    infra_gg= 0

    valor_l= 130.16
    valor_g= 195.23
    valor_gg= 880.41

    if Velocidade <= Velocidade_maxima:
        return print ('Nenhuma Infração.')
    elif (Velocidade_maxima * 1.20) >= Velocidade:
        infra_l += 1
        return infra_l
    elif (Velocidade_maxima * 1.20) >= Velocidade <= (Velocidade_maxima * 1.50):
        infra_g += 1
        return infra_g
    elif (Velocidade_maxima * 1.50) <= Velocidade:
        infra_gg += 1
        return infra_gg
    
    elif infra_l == 1:
        return print('Infração Leve - Multa de R$', (valor_l), 'e Nenhum ponto na CNH')
    elif infra_g == 1:
        return print ('Infração Grave - Multa de R$',(valor_g),'Reais e 5 pontos na CNH')
    elif infra_gg == 1:
        return print ('Infração Gravissíma - Multa de R$', (valor_gg) ,'e suspensão da carteira ')
    
    elif Multa == 'Sim':

        infra_l += 1
        infra_g += 1
        infra_gg += 1

        if infra_g == 1:
            print('Atenção: Multa DOBRADA por reincidência! ')
            valor_g * 2
        elif infra_gg == 1:
            print('Atenção: Multa DOBRADA por reincidência')
            print('Atenção: CNH suspensa! Compareça ao Detran.')
            valor_gg * 2

#RECICLAGEM

        elif infra_gg == 2:
            print('Atenção: Você precisa fazer um curso de reciclagem no Detran.')

#PAGAMENTO DA MULTA#

        elif pagamento_m == 'Sim':
            if infra_l == 2:
                print ('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$',(valor_l*0.80))
            elif infra_g == 2:
                print ('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$',(valor_g*0.80))
            elif infra_gg == 2:
                print ('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$',(valor_gg*0.80))
        else:


            return print('Atenção: Nenhuma Reincidência.')

# 1. PROGRAMA PRINCIPAL
Placa = input("Placa do veículo: \n")
Nome = input("Nome do motorista: \n")
Velocidade = int(input("Velocidade registrada: \n"))
Velocidade_maxima = int(input("Velocidade máxima permitida na via: \n"))
Multa = input("O motorista já foi multados antes? (Sim/Não):  \n")
pagamento_m = input ('Deseja pagar a multa agora? (Sim/Não): \n')

print('Placa: ',Placa)
print('Motorista',Nome)
print('Velocidade Registrada: ',Velocidade,'km/h')
print('Velocidade Máxima permitida: ',Velocidade_maxima, 'km/h')

infraT = classificacao_infracao(Multa,pagamento_m,Velocidade,Velocidade_maxima)
print(infraT)



