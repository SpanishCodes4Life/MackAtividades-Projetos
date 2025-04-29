#EM UM SISTEMA DE CAIXA DE UMA LOJA, O CLIENTE DEVE PAGAR O VALOR TOTAL DA COMPRA
#EM DINHEIRO. O SISTEMA DEVE REGISTRAR OS VALORES INSERIDOS PELO USUÁRIO(SIMULANDO O RECEBIMENTO DE CÉDULAS)
#E MANTER O PROCESSO DE RECEBIMENTO ENQUANTO O VALOR TOTAL RECEBIDO FOR MENOR QUE O VALOR DA COMPRA

#AO FINAL DE CADA ENTRADA, O SISTEMA DEVE INFORMAR QUANTO AINDA FALTA PAGAR.QUANDO O VALOR TOTAL ATINGIR OU ULTRAPASSAR O
#VALOR DA COMPRA, O SISTEMA DEVERÁ ENCERRAR A REPETIÇÃO, EXIBIR A CONFIRMAÇÃO DE PAGAMENTO E, SE HOUVER, O VALOR DO TROCO A SER DEVOLVIDO AO CLIENTE

#REQUISITOS:
#SOLICITAR AO OPERADOR O VALOR TOTAL DA COMPRA.
#RECEBER, EM ETAPAS, OS VALORES PAGOS (COMO SE FOSSEM INSERIDOS CÉDULA POR CÉDULA)
#CONTINUAR SOLICITANDO VALORES ENQUANTO O TOTAL RECEBIDO FOR INFERIOR AO TOTAL DA COMPRA.
#INFORMAR, A CADA ENTRADA, O VALOR RESTANTE A SER PAGO.
#AO FINAL, CONFIRMAR O PAGAMENTO E INDICAR O VALOR DO TROCO, CASO O CLIENTE TENHA PAGO UM VALOR MAIOR.

def sistemafinal():
    v_valor_pagamento = 0 #VAR QUE RECEBE O VALOR TOTAL DO PAGAMENTO
    v_valor_sub = 0 #VAR NÃO UTILIZADA

    v_valor_do_produto = int(input('Digite o Valor da Compra: \n'))
    pagamento = int(input('Digite o Valor do PAGAMENTO: \n'))
    if pagamento == v_valor_do_produto:
        print('Pagamento realizado!!!')

    elif pagamento > v_valor_do_produto:
        print(f'Pagamento Realizado!!!\n Seu Troco foi de R${pagamento - v_valor_do_produto}')

    else:
        while pagamento < v_valor_do_produto:
            
            pagamento = int(input('\n ATENÇÃO! Insira um Valor correpondente ao Produto R$'))
            
        print('Pagamento realizado!!!')

sistemafinal()
