import random
import time
import timeit

# Djorkaeff Alexandre Vilela Pereira - 16/0026822
# Lucas Brilhante - 

# Função pra ordenar o vetor toda vez que for inserido um novo número
class QuickSort(object):
    def particao(self, a, ini, fim):
        pivo = a[fim-1]
        start = ini
        end = ini
        for i in range(ini,fim):
            if a[i] > pivo:
                end += 1
            else:
                end += 1       
                start += 1
                aux = a[start-1]
                a[start-1] = a[i]
                a[i] = aux
        return start-1
    def quickSort(self, a, ini, fim):
        if ini < fim:
            pp = self.randparticao(a, ini, fim)
            self.quickSort(a, ini, pp)
            self.quickSort(a, pp+1,fim)
        return a       
    def randparticao(self,a,ini,fim):
        rand = random.randrange(ini,fim)
        aux = a[fim-1]
        a[fim-1] = a[rand]
        a[rand] = aux
        return self.particao(a,ini,fim)

opcao = 3
vetor = []

# Busca binária simples 
def BuscaBinaria(vetor, ini, fim, elementoBuscado):

    if ini==fim:
        return -1

    i = int(((ini+fim)/2))

    if vetor[i] == elementoBuscado:
        return i
    else:
        if vetor[i]<elementoBuscado:
            BuscaBinaria(vetor, i, fim, elementoBuscado)
        else:
            BuscaBinaria(vetor, ini, i, elementoBuscado)

# Busca indexada com separação em blocos de 100 do vetor, e dentro de cada bloco de 100 fazemos busca binária
def BuscaIndexada(vetor, ini, fim, elementoBuscado):
    if ini-fim == 0:
        return -1
    if ini-fim < 100:
        return BuscaBinaria(vetor, ini, fim, elementoBuscado)
    for x in range(ini, fim): # Pega todo o vetor em um laço
        if vetor[x] > elementoBuscado: # se o valor da posição do vetor 0 for maior que o elemento buscado
            if x != 0: # se não estivermos no início do vetor
                valor = BuscaBinaria(vetor, x, x-100, elementoBuscado) # procuramos nos 100 números anteriores ao atual
                if valor == -1:
                    print('Número não existe')
                elif vetor[valor]==elementoBuscado:
                    return valor
                if x>len(vetor):
                    break
            break # paramos pois sabemos que ele está antes da posição atual
        x += 100 # pulamos para os próximos 100 números


#while opcao != 0:
 #   print ('1 - Inserir novo número')
  #  print ('2 - Buscar por número')
   # print ('0 - Sair')
   # opcao = int(input('Digite sua opção: '))
    #if opcao == 1:
     #   entrada = int(input('Digite um número: '))
      #  vetor.append(entrada)
       # quick = QuickSort()
        #quick.quickSort(vetor,0,len(vetor))
       # pass
    #elif opcao == 2:

import random
print('Gerando vetor de números randômicos com 1000000 números')
vetor = random.sample(range(1, 10000000), 1000000)
entrada = int(input('Digite o elemento a procurar: '))
quick = QuickSort()

inicio = timeit.default_timer()
quick.quickSort(vetor,0,len(vetor))
resultado = BuscaBinaria(vetor, 0, len(vetor), entrada)
fim = timeit.default_timer()
print ('Tempo para a busca binária: %f segundos' % (fim - inicio))

# Não tô salvando o valor retornado da busca indexada pois já estou pegando a posição em que o valor estiver pela busca binária
inicio = timeit.default_timer()
quick = QuickSort()
quick.quickSort(vetor,0,len(vetor))
resultadoIndex = BuscaIndexada(vetor, 0, len(vetor), entrada)
fim = timeit.default_timer()
print ('Tempo para a busca indexada + binária: %f segundos' % (fim - inicio))

if resultado != -1:
    print('O elemento foi encontrado no vetor.')
else:
    print('O elemento não foi encontrado no vetor.')
pass

    #elif opcao == 0:
     #   print('Obrigado por utilizar o programa')
     #   pass
    #else:
    #    print('Opção não implementada')
     #   pass


