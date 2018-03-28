#   Djorkaeff Alexandre - Lucas Brilhante
#   Trabalho 2 - Estrutura de dados 2
#   Algorítmo de ordenação (O(n^2)) - Comb_sort

from matplotlib.pylab import plot, show, bar
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


def generateVector(total, vetor):
    print('Gerando vetor de números randômicos com %d números...' % total)
    vetor = random.sample(range(1, 10000000), total)
    print('Ordenando o vetor...')
    comb_sort(vetor)
    print('Vetor ordenado')

def timeToSort(qtd, tempos, vetor):
    inicio = timeit.default_timer()
    generateVector(qtd, vetor)
    fim = timeit.default_timer()
    tempos.append(fim-inicio)
    print('Tempo para ordenação: ' + str(fim-inicio) + ' s')

def main(tempos, vetor, tamVetor):
    for i in range(0,100000,5000):
        tamVetor.append(i)
        timeToSort(i, tempos, vetor)
        print('\n')
        print('Processo concluído..')
        print('\n\n\n')

tempos = []
vetor = []
tamVetor = []
main(tempos, vetor, tamVetor)
plot(tamVetor, tempos, 'bo')                     # draw the points
plot(tamVetor, tempos)                     # draw the graph

show()                      # show it to me!