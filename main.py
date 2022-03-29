from datetime import datetime
from src.classes.SearchAlgorithms import BuscaLargura
from src.classes.SearchAlgorithms import BuscaProfundidade
from src.classes.SearchAlgorithms import BuscaProfundidadeIterativa
from src.classes.SearchAlgorithms import BuscaCustoUniforme
from src.classes.SearchAlgorithms import BuscaGananciosa
from src.classes.SearchAlgorithms import AEstrela
from src.classes.Puzzle import Puzzle

easy = [[1,2,3],[0,8,4],[7,6,5]]
medium = [[8,1,3],[0,7,2],[6,5,4]]
hard = [[7,8,6],[2,3,5],[1,4,0]]
hard1 = [[7,8,6], [2,3,5], [0,1,4]]

def main():
    print('Busca em largura')
    state = Puzzle(0, 2, hard1, "; ")
    print()
    for line in state.board:
        print ('  '.join(map(str, line)))
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()