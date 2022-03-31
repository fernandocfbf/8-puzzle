from src.classes.Graph import State
from copy import deepcopy
from src.constants.goal_position import GOAL, GOAL_BOARD
#
# Initial state: 1
# Operations: +1 and +2
# Final state: any number bigger than 0
#

class Puzzle(State):

    def __init__(self, x, y, board, operator):
        self.x = x
        self.y = y
        self.board = board #matriz [3 x 3]
        self.operator = operator #current operation

    def env(self):
        return "{0}".format(self.board)

    def sucessors(self):
        childrens = list()

        possibilities = [
                [0, -1],
        [-1, 0],        [1,  0],
                [0,  1]
        ]
        for pos in possibilities:
            mov_y = self.y + pos[1]
            mov_x = self.x + pos[0]
            if((mov_y < 3 and mov_y >= 0) and (mov_x < 3 and mov_x >= 0)):
                current_board = deepcopy(self.board)
                changed_board = self.switch(current_board, mov_x, mov_y)
                move=self.get_move(pos)
                childrens.append(Puzzle(mov_x, mov_y, changed_board, move))
        return childrens

    def is_goal(self):
        return self.board == GOAL_BOARD

    def switch(self, board, cx, cy):
        res = board
        e = board[cy][cx]
        res[self.y][self.x] = e
        res[cy][cx] = 0
        print()
        for line in res:
            print ('  '.join(map(str, line)))
        return res

    def get_move(self, pos):
        if pos == [0, -1]:
            return 'up'
        elif pos == [-1, 0]:
            return 'left'
        elif pos == [1, 0]:
            return 'right'
        return 'down'

    def description(self):
        return "Algorithm to solve the 8-Puzzle problem through search algorithms"

    def cost(self):
        return 1

    def h(self):
        return self.manhattan()

    def print(self):
        return str(self.operator)

    def manhattan(self):
        board_distance = 0
        for line in range(len(self.board)):
            for column in range(len(self.board)):
                number = str(self.board[line][column])
                goal_position = GOAL[number]
                distance = abs(line - goal_position[0]) + abs(column - goal_position[1])
                board_distance += distance
        return board_distance
