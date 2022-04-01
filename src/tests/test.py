from Puzzle import Puzzle
from SearchAlgorithms import AEstrela
from datetime import date, datetime
from goal_position import GOAL_BOARD
from check_solvable import isSolvable


def test01():
    board = [
        [8,1,3],
        [0,7,2],
        [6,5,4]
    ]
    state = Puzzle(0,1,board,"")
    algorithm = AEstrela()
    init = datetime.now()
    result = algorithm.search(state)
    end = datetime.now()
    print(end - init)
    assert result.state.env() == str(GOAL_BOARD)


def test02():
    board = [
        [7,8,6],
        [2,3,5],
        [1,4,0]
    ]
    state = Puzzle(2,2,board,"")
    algorithm = AEstrela()
    init = datetime.now()
    result = algorithm.search(state)
    end = datetime.now()
    print(end - init)
    assert result.state.env() == str(GOAL_BOARD)

def test03():
    board = [
        [7,8,6],
        [2,3,5],
        [0,1,4]
    ]
    state = Puzzle(0,2,board,"")
    algorithm = AEstrela()
    init = datetime.now()
    result = algorithm.search(state)
    end = datetime.now()
    print(end - init)
    assert result.state.env() == str(GOAL_BOARD)

def test04():
    board = [
        [8,3,6],
        [7,5,4],
        [2,1,0]
    ]
    state = Puzzle(2,2,board,"")
    algorithm = AEstrela()
    init = datetime.now()
    result = algorithm.search(state)
    end = datetime.now()
    print(end - init)
    assert result.state.env() == str(GOAL_BOARD)


def test05():
    board = [
        [5,4,0],
        [6,1,8],
        [7,3,2]
    ]
    assert isSolvable(board) == False