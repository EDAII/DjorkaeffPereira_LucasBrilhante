## Pré-requisitos

<p align="justify">Para testar o arquivo da lista 2 deve-se ter instalado em seu computador o python na versão 3 e a biblioteca matplotlib.pylab que pode ser baixada a partir de https://matplotlib.org/, esta biblioteca foi usada para gerar o gráfico de tempo de ordenação em um vetor de diferentes tamanhos.</p>

## Instruções

<p align="justify">Para iniciar o projeto deve-se abrir a pasta do arquivo no Terminal|Prompt de comando e inserir o comando _"python3 sort.py"_, feito isto será apresentado uma espécie de menu com três opções sendo elas "Ordenação com Comb-Sort", "Ordenação com Bubble-Sort" ou "Ordenação com Comb-Sort e com Bubble-Sort", após a seleção de uma dessas opções o programa irá gerar vetores aleatórios com tamanhos diversos e calculando o tempo que leva para o algoritmo de ordenação selecionado ordenar o vetor, feito isto o programa irá plotar um gráfico de TAMANHO_DO_VETOR vs. TEMPO_DE_ORDENACAO, quando a terceira opção for selecionada por padrão a linha *azul* representa o resultado do *comb-sort* e a linha *laranja* representa o tempo do *bubble-sort*.</p>

## Testes realizados

<p align="justify">Enquanto o projeto era codificado foram realizados vários testes com vetores de tamanhos variados e os algoritmos de ordenação *Bubble-Sort* e *Comb-Sort*, alguns destes testes foram explicados e explanados neste arquivo, logo em seguida:</p>

![Comb-Sort](https://i.imgur.com/UBZ35xW.png "test1")

<p align="justify">O resultado obtido para o comb-sort com um vetor de números randômicos que começa com 0 inteiros e vai até 100000 (cem mil) inteiros com passo de 1000 (hum mil) em quantidade de inteiros foi o gráfico acima.</p>

![Comparation](https://i.imgur.com/nJOJYOx.png "test2")

<p align="justify">O gráfico acima nos mostra uma comparação entre o tempo de ordenação de um algoritmo Comb-Sort e um Bubble-Sort, o tempo de *Bubble-sort* está sendo representado pela linha *laranja* e o tempo de *Comb-Sort* está sendo representado pela linha azul, o tamanho máximo de vetor levado em conta no teste em questão foi um vetor com 30000 (trinta mil) inteiros aleatórios de 1 (um) a 10000000 (dez milhões). Podemos ver facilmente que *Bubble-Sort* tem complexidade *O(n^2)* e o *Comb-Sort* tem comportamento quase *O(n)* quando comparado ao *Bubble-Sort*.</p>