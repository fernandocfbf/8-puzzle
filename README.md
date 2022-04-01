# 8-puzzle

O objetivo do projeto é resolver o problema 8puzzle através de um programa python que implementa o algoritmo A*.

O projeto é composto de uma classe principal, chamada Puzzle. Nela são implementados as técnicas de geração de sucessores e heurísitca.

A geração de sucessores consiste basicamente em, dado um posição do número 0 no tabuleiro, gerar todos os possíveis movimentos. Entende-se por possível movimento aquele onde a posição (x,y) está dentro dos limites do tabuleiro.

Além disso, para a heurística foi escolhido a distância de manhattan, a qual é admissível, uma vez que a distância sempre será menor ou igual ao custo real para que uma peça chegue ao local desejado
