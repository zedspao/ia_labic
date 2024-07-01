# Objetivo: Desenvolver um sistema para gerenciar livros em uma biblioteca,
# utilizando estruturas de dados apropriadas.
    # Criar funcionalidades para *adicionar, *remover, *buscar e *listar livros.
    # Usar dicionários para armazenar informações dos livros* e listas para manter uma coleção de livros disponíveis e emprestados.
    # Implementar um sistema de busca para encontrar livros por título*, autor* ou categoria*.

import os

acervo = dict()

acervo["dracula"] = ["bram stoker", "romance", "disponivel"]
acervo["dracula 2"] = ["bram stoker", "conto", "disponivel"]
acervo["frankenstein"] = ["mary shelly", "romance", "emprestado"]

livros_disponiveis = ["dracula", "dracula 2"]

def propriedades_volume(titulo):
    print(" ")
    print("Nome do Volume: " + titulo)
    print("Autor: " + str(acervo[titulo][0]))
    print("Ano de Publicação: " + str(acervo[titulo][1]))
    print("Disponibilidade: " + str(acervo[titulo][2]))
    
def consultar_acervo():
    colecao_livros = list(acervo.keys())
    if colecao_livros == []:
        print("O acervo está vazio.")
    else:
        for livros in range(len(colecao_livros)):
            print(str(colecao_livros[livros]))
        
        volume_consultado = input("Que volume deseja consultar?: ")
        if volume_consultado in colecao_livros:
            propriedades_volume(volume_consultado)
        else:
            print("Esse volume não está no acervo.")

def buscar_acervo(escolha_buscar):
    """
    (1): Titulo; (2): Autor; (3): Categoria
    """
    # Busca pelo título
    if escolha_buscar == 1:
        livro_buscado = input("Qual o nome do volume que está procurando?: ")
        if livro_buscado in list(acervo.keys()):
            print("Esse volume está no acervo.")
            propriedades_volume(livro_buscado)
        else:
            print("Esse volume não está no acervo.")

    # Busca pelo autor
    elif escolha_buscar == 2:
        parametro_buscado = []
        chave = []
        autor_buscado = input("Qual o autor do volume que está procurando?")

        for livros in list(acervo.keys()):
            parametro_buscado.append(acervo[livros][0])

        for livros in list(acervo.keys()):
            if autor_buscado == acervo[livros][0]:
                chave.append(livros)

        if autor_buscado in parametro_buscado:
            for chaves in chave:
                propriedades_volume(chaves)
                print(" ")
        else:
            print("Não há nenhum volume no acervo com esse autor.")

    # Busca pela categoria
    elif escolha_buscar == 3:
        parametro_buscado = []
        chave = []
        categoria_buscado = input("Qual a categoria do volume que está procurando?")

        for livros in list(acervo.keys()):
            parametro_buscado.append(acervo[livros][1])

        for livros in list(acervo.keys()):
            if categoria_buscado == acervo[livros][1]:
                chave.append(livros)

        if categoria_buscado in parametro_buscado:
            for chaves in chave:
                propriedades_volume(chaves)
                print(" ")
        else:
            print("Não há nenhum volume no acervo com essa categoria.")

def modificar_acervo(escolha_modificar):
    """
    (1): Adicionar; (2): Remover; (3) Disponibilidade dos livros.
    """
    # Adicionar um livro
    if escolha_modificar == 1:
        quantidade_adicionar = int(input("Quantos livros deseja adicionar?"))
        for livros_adicionados in range(quantidade_adicionar):
            nome = str(input("Nome do volume: "))
            autor = str(input("Autor do volume: "))
            ano = str(input("Ano do volume: "))
            disponibilidade = str(input("Disponibilidade do volume: "))

            acervo[nome] = [autor, ano, disponibilidade]
            print("Volume adicionado.")
        if disponibilidade == "disponivel":
            livros_disponiveis.append(nome)
    # Remover um livro
    if escolha_modificar == 2:
        quantidade_remover = int(input("Quantos livros deseja remover?"))
        for livros_removidos in range(quantidade_remover):
            nome = str(input("Nome do volume: "))
            if nome in acervo.keys():
                acervo.pop(nome)
                if nome in livros_disponiveis:
                    livros_disponiveis.remove(nome)
                print("Volume removido.")
            else:
                print("Esse volume não está no acervo.")
    # Disponibilidade de livros
    if escolha_modificar == 3:
        nome = str(input("Que volume deseja alterar a disponibilidade?"))
        if nome in acervo.keys():
            if acervo[nome][2] == "disponivel":
                acervo[nome][2] = "emprestado"
                print("Disponibilidade de " + str(nome) + " foi alterada com sucesso.")
            else:
                acervo[nome][2] = "disponivel"
                print("Disponibilidade de " + str(nome) + " foi alterada com sucesso.")
        else:
            print("Esse volume não está no acervo.")

def menu():
    os.system('cls')
    print("Que operação deseja realizar?")
    print("1. Consultar acervo.")
    print("2. Modificar o acervo.")
    print("3. Finalizar operação")

menu()

while True:

    user_input = int(input())

    if user_input == 1:
        os.system('cls')
        consultar_acervo()
        input("Digite qualquer tecla para prosseguir.")
        menu()
    elif user_input == 2:
        os.system('cls')
        operacao_desejada = int(input("1. Adicionar ao acervo || 2. Remover do acervo || 3. Alterar disponibilidade de obra. : "))
        modificar_acervo(operacao_desejada)
        input("Digite qualquer tecla para prosseguir.")
        menu()
    elif user_input == 3:
        os.system('cls')
        break