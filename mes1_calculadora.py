# Desenvolver uma aplicação em Python que realiza operações estatísticas básicas como média, mediana, e desvio padrão.

# Ler um arquivo e armazenar seu conteúdo numa lista.
# Fornecer as opções de operações no console.
# > Exibir um histograma;
# Retornar o solicitado.

import numpy as np
from matplotlib import pyplot as plt

caso = 0
print("Informe o nome do arquivo inserido na pasta do programa (lembre-se da extensão):")
nome = input()

try:
    file = np.loadtxt(nome, delimiter=" ")

    print("Escolha a operação desejada:")
    print("1. Média"
          "\n2. Variância"
          "\n3. Mediana"
          "\n4. Desvio Padrão Populacional"
          "\n5. Desvio Padrão Amostral"
          "\n6. Encerrar")

    file_float = file.astype(float)

    plt.hist(file_float, bins=len(file_float), edgecolor='black')
    plt.title("Dados")
    plt.xlabel("Valores")
    plt.ylabel("Quantidades")
    plt.show()

    while caso != 6:
        caso = input()
        caso = int(caso)

        if caso == 1:
            print("Média: " + str(np.mean(file)))
        elif caso == 2:
            print("Variância: " + str(np.var(file)))
        elif caso == 3:
            print("Mediana: " + str(np.median(file)))
        elif caso == 4:
            print("Desvio Padrão Populacional: " + str(np.std(file)))
        elif caso == 5:
            print("Desvio Padrão Amostral: " + str(np.std(file, ddof=1)))

except FileNotFoundError:
    print("O arquivo não foi localizado.")
