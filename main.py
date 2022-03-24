from datetime import datetime
from src.classes.SearchAlgorithms import BuscaLargura
from src.classes.SearchAlgorithms import BuscaProfundidade
from src.classes.SearchAlgorithms import BuscaProfundidadeIterativa
from src.classes.SearchAlgorithms import BuscaCustoUniforme
from src.classes.SearchAlgorithms import BuscaGananciosa
from src.classes.SearchAlgorithms import AEstrela

def main():
    print('Busca em largura')
    state = U2([], ['bono', 'larry', 'adam', 'edge'], 'right', 17, '', 0)
    algorithm = BuscaCustoUniforme()
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