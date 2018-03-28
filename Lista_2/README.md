## Pré-requisitos

<p align="justify">Para testar o arquivo da lista 2 deve-se ter instalado em seu computador o python na versão 3 e a biblioteca matplotlib.pylab que pode ser baixada a partir de https://matplotlib.org/, esta biblioteca foi usada para gerar o gráfico de tempo de ordenação em um vetor de diferentes tamanhos.</p>

## Instruções

<p align="justify">Para iniciar o projeto deve-se abrir a pasta do arquivo no <b>Terminal | Prompt de comando</b> e inserir o comando <b>"python3 sort.py"</b>, feito isto será apresentado uma espécie de menu com três opções sendo elas <b>"Ordenação com Comb-Sort"</b>, <b>"Ordenação com Bubble-Sort"</b> ou <b>"Ordenação com Comb-Sort e com Bubble-Sort"</b>, após a seleção de uma dessas opções o programa irá gerar vetores aleatórios com tamanhos diversos e calculando o tempo que leva para o algoritmo de ordenação selecionado ordenar o vetor, feito isto o programa irá plotar um gráfico de TAMANHO_DO_VETOR vs. TEMPO_DE_ORDENACAO, quando a terceira opção for selecionada por padrão a <b>linha azul</b> representa o resultado do <b>comb-sort</b> e a <b>linha laranja</b> representa o tempo do <b>bubble-sort</b>.</p>

## Testes realizados

<p align="justify">Enquanto o projeto era codificado foram realizados vários testes com vetores de tamanhos variados e os algoritmos de ordenação <b>Bubble-Sort</b> e <b>Comb-Sort</b>, alguns destes testes foram explicados e explanados neste arquivo, logo em seguida:</p>

![Comb-Sort](https://i.imgur.com/UBZ35xW.png "test1")

<p align="justify">O resultado obtido para o comb-sort com um vetor de números randômicos que começa com 0 inteiros e vai até 100000 (cem mil) inteiros com passo de 1000 (hum mil) em quantidade de inteiros foi o gráfico acima.</p>

<p align="center">
  <img src="https://i.imgur.com/nJOJYOx.png" alt="test" />
</p>

<p align="justify">O gráfico acima nos mostra uma comparação entre o tempo de ordenação de um algoritmo <b>Comb-Sort</b> e um <b>Bubble-Sort</b>, o tempo de <b>Bubble-sort</b> está sendo representado pela <b>linha laranja</b> e o tempo de <b>Comb-Sort</b> está sendo representado pela <b>linha azul</b>, o tamanho máximo de vetor levado em conta no teste em questão foi um vetor com 30000 (trinta mil) inteiros aleatórios de 1 (um) a 10000000 (dez milhões). Podemos ver facilmente que <b>Bubble-Sort</b> tem complexidade <b>O(n^2)</b> e o <b>Comb-Sort</b> tem comportamento quase <b>O(n)</b> quando comparado ao <b>Bubble-Sort</b>.</p>
