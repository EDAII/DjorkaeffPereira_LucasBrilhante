#   Djorkaeff Alexandre - Lucas Brilhante
#   Trabalho 2 - Estrutura de dados 2
#   Algorítmo de ordenação (O(n^2)) - Comb_sort

import matplotlib.pyplot as plt
import random
import time
import timeit

def comb_sort(vetor):
    gap = int(len(vetor)/1.3)
    i = 0
    aux = 0
    while gap > 0 and i != (len(vetor) - 1):
        i = 0
        while i+gap < len(vetor):
            if vetor[i] > vetor[i+gap]:
                aux = vetor[i]
                vetor[i] = vetor[i+gap]
                vetor[i+gap] = aux
            i=i+1
        gap = int(gap/1.3)

def bubble_sort(vetor):
    for count in range(len(vetor)-1,0,-1):
        for i in range(count):
            if vetor[i]>vetor[i+1]:
                temp = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = temp

def generateVector(total, vetor, typeSort):
    print('Gerando vetor de números randômicos com %d números...' % total)
    vetor = random.sample(range(1, 10000000), total)
    print('Ordenando o vetor...')
    if typeSort==1:
        print('Comb-Sort')
        comb_sort(vetor)
    if typeSort==2:
        print('Bubble-Sort')
        bubble_sort(vetor)
    print('Vetor ordenado')

def timeToSort(qtd, tempos, vetor, typeSort):
    inicio = timeit.default_timer()
    generateVector(qtd, vetor, typeSort)
    fim = timeit.default_timer()
    tempos.append(fim-inicio)
    print('Tempo para ordenação: ' + str(fim-inicio) + ' s')

def main(typeSort):
    tempos = []
    vetor = []
    tamVetor = []
    for i in range(0,30001,5000):
        tamVetor.append(i)
        timeToSort(i, tempos, vetor, typeSort)
        print('\n')
        print('Processo concluído..')
        print('\n\n\n')
    # plot(tamVetor, tempos, 'bo')                     # draw the points
    plt.plot(tamVetor, tempos)

print('1 - Ordenação com comb-sort')
print('2 - Ordenação com bubble-sort')
print('3 - Ordenação com bubble-sort e com comb-sort')
entrada = int(input('Digite a opção escolhida: '))
if entrada==1:
    main(1)
elif entrada==2:
    main(2)
elif entrada==3:
    main(1)
    main(2)

plt.xlabel('Tamanho vetor')
plt.ylabel('Tempo (s)')
plt.legend(['Comb-Sort', 'Bubble-Sort'])
plt.grid(True)
plt.show()