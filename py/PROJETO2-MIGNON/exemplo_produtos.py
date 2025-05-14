def le_produto():
    print("* Informe os dados do produto *")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    departamento = input("Departamento: ")
    produto = []
    produto.append(nome)
    produto.append(preco)
    produto.append(departamento)
    return produto

def adiciona_produto(produtos, produto):
    produtos.append(produto)

def media_departamento(produtos, departamento):
    soma = 0.0
    qtde = 0
    for produto in produtos:
        if produto[2] == departamento:
            soma = soma + produto[1]
            qtde = qtde + 1
    if qtde > 0:
        return soma / qtde
    else:
        return 0.0
                  

def menu():
    print("*** MENU ***")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Valor Médio de Departamento")
    print("0. Sair")
    return int(input("Informe uma opção: "))

if __name__ == "__main__":
    produtos = [
        ["Teclado", 150.25, "INFO"],
        ["TV", 3500.00, "ELETRO"]
    ]

    opcao = 1
    while opcao != 0:
        opcao = menu()
        if opcao == 1:
            produto = le_produto()
            adiciona_produto(produtos, produto)
        elif opcao == 2:
            print(produtos)
        elif opcao == 3:
            departamento = input("Informe o departamento: ")
            media = media_departamento(produtos, departamento)
            print(f"Média: {media:.2f}")
        elif opcao < 0 or opcao > 3:
            print("Opção Inválida")
        

    


    
