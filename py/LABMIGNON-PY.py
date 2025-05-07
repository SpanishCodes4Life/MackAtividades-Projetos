#EXERCICIO2

def numberfunction():
    n1 = int(input('DIGITE SEU NÚMERO: '))
    pares = 0
    impares = 0
    print('PROCESSANDO...')
    print(f'SEU NÚMERO É {n1}')

    for i in range(n1):
        if i %2 == 0:
            pares +=1
        else:
            impares +=1
            print(i)
    
    print(f'NESTE NÚMERO HÁ {pares} IMPARES')
    #USEI LISTA X

def exercise2():
    n = int(input('DIGITE SEU NÚMERO: '))
    pares = 0
    impares = 0
    soma = 0
    print('PROCESSANDO...')
    print(f'SEU NÚMERO É {n}')

    while (n>0):
        resto = n % 10
        n = (n - resto)/10
        soma = soma + resto

    print(f'A SOMA DOS NÚMEROS É: {soma}')

    while (pares<n):
        resto = n % 10
        if n %2 == 0:
            n = (n-resto)/10
            print(n)


def exercise1():
    x = 0
    while x != 1:
        intervalo = int(input('QUANTOS INTERVALOS? :'))
        usorecurso = int(input('QUAL O USO DO RECURSO? ENTRE 0 A 100 '))
        if 100> usorecurso <= 0:
            usorecurso = intervalo / usorecurso
            print(usorecurso)
        elif usorecurso >100 or usorecurso<0:
            print('ESCOLHA ENTRE 0 A 100')

exercise1()
