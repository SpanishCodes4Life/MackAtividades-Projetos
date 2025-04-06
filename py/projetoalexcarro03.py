
#FUNÇÕES
def classinfra(Multa,Velocidade,Velocidade_maxima,pagamento_m):
    valor_l= 130.16
    valor_g= 195.23
    valor_gg= 880.41

    #NENHUMA MULTA#
    if Velocidade <= Velocidade_maxima:
        return "Nenhuma Infração"
    #END

    #MULTA LEVE
    elif (Velocidade_maxima * 1.20) >= Velocidade:
        if Multa == 'Não':
            print('Infração Leve - Multa de R$', (valor_l), 'e Nenhum ponto na CNH')
            if pagamento_m == 'Sim':
                print ('Pagamento realizado! Voce recebeu um desconto de 20%. Valor final: R$',valor_l*0.80)
            elif pagamento_m == 'Não':
                print ('Pagamento realizado! Valor final: R$',valor_l)
        elif Multa == 'Sim':
            print('Infração Leve - Multa de R$', (valor_l), 'e Nenhum ponto na CNH')
            if pagamento_m == 'Sim':
                print('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$',valor_l*0.80)
            elif pagamento_m == 'Não':
                print ('Pagamento realizado! Valor final: R$',valor_l)
    #END

    #MULTA GRAVE#
    elif (Velocidade_maxima * 1.20) <= Velocidade <= (Velocidade_maxima * 1.50):
        if Multa == 'Não':
            print ('Infração Grave - Multa de R$',(valor_g),'Reais e 5 pontos na CNH')
            if pagamento_m == 'Sim':
                print ('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$', valor_g*0.80)
            elif pagamento_m == 'Não':
                print ('Pagamento realizado! Valor final: R$', valor_g)
        elif Multa == 'Sim':
            print ('Infração Grave - Multa de R$',(valor_g),'Reais e 5 pontos na CNH')
            print ('Atenção: Multa DOBRADA por reincidência')
            if pagamento_m == 'Sim':
                print('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$',(valor_g*2)*0.80)
            elif pagamento_m == 'Não':
                print ('Pagamento realizado! Valor final: R$',(valor_g*2))
    #END#

    #MULTA GRAVISSÍMA#
    elif (Velocidade_maxima * 1.50) < Velocidade:
        if Multa == 'Não':
            print ('Infração Gravissíma - Multa de R$', (valor_gg) ,'e suspensão da carteira ')
            if pagamento_m == 'Sim':
                print ('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$', valor_gg*0.80)
            elif pagamento_m == 'Não':
                print ('Pagamento realizado! Valor final: R$', valor_gg)
        elif Multa == 'Sim':
            print ('Infração Gravissíma - Multa de R$', (valor_gg) ,'e suspensão da carteira ')
            print ('Atenção: Multa DOBRADA por reincidência')
            print ('Atenção: CNH suspensa! Compareça ao Detran.')
            print ('Atenção: Você precisa fazer um curso de reciclagem no Detran.')
            if pagamento_m == 'Sim':
                print('Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$',(valor_gg*2)*0.80)
            elif pagamento_m == 'Não':
                print ('Pagamento realizado! Valor final: R$',valor_gg*2)
    #END#

# 1. PROGRAMA PRINCIPAL
Placa = input("Placa do veículo: \n")
Nome = input("Nome do motorista: \n")
Velocidade = int(input("Velocidade registrada: \n"))
Velocidade_maxima = int(input("Velocidade máxima permitida na via: \n"))
Multa = input("O motorista já foi multado/a antes? (Sim/Não):  \n")
pagamento_m = input ('Deseja pagar a multa agora? (Sim/Não): \n')

print('Placa: ',Placa)
print('Motorista',Nome)
print('Velocidade Registrada: ',Velocidade,'km/h')
print('Velocidade Máxima permitida: ',Velocidade_maxima, 'km/h')

totclass = classinfra(Multa,Velocidade,Velocidade_maxima,pagamento_m)
print (totclass)
