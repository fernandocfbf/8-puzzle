from Graph import State

#
# Initial state: 1
# Operations: +1 and +2
# Final state: any number bigger than 0
#

class Puzzle(State):

    def __init__(self):

    def env(self):
        return 

    def sucessors(self):
        return

    def is_goal(self):
        return

    def description(self):
        return "Algorithm to solve the 8-Puzzle problem through search algorithms"

    def cost(self):
        return

    def h(self):
        return 0

    def print(self):
        return str(self.operator)
