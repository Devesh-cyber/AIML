from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    def actions(self, state):
        return list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        wrong = sum(1 for i in range(len(state)) if state[i] != GOAL[i])
        missing = len(GOAL) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
res = astar(problem)
print(res.state)

for action, state in res.path():
    print(action, " => ", state)