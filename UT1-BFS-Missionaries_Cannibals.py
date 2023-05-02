from queue import PriorityQueue

class State:
    def __init__(self, m_left, c_left, b, m_right, c_right):
        self.m_left = m_left
        self.c_left = c_left
        self.b = b
        self.m_right = m_right
        self.c_right = c_right
    
    def is_valid(self):
        if self.m_left < 0 or self.c_left < 0 or self.m_right < 0 or self.c_right < 0:
            return False
        if self.m_left != 0 and self.m_left < self.c_left:
            return False
        if self.m_right != 0 and self.m_right < self.c_right:
            return False
        return True
    
    def is_goal(self):
        return self.m_left == 0 and self.c_left == 0
    
    def generate_next_states(self):
        next_states = [
            State(self.m_left - 2, self.c_left, 1, self.m_right + 2, self.c_right),
            State(self.m_left, self.c_left - 2, 1, self.m_right, self.c_right + 2),
            State(self.m_left - 1, self.c_left - 1, 1, self.m_right + 1, self.c_right + 1),
            State(self.m_left - 1, self.c_left, 1, self.m_right + 1, self.c_right),
            State(self.m_left, self.c_left - 1, 1, self.m_right, self.c_right + 1)
        ]
        return [state for state in next_states if state.is_valid()]
    
    def heuristic_cost(self):
        return (self.m_left + self.c_left) // 2
    
    def __lt__(self, other):
        return self.heuristic_cost() < other.heuristic_cost()

def solve():
    initial_state = State(3, 3, 0, 0, 0)
    frontier = PriorityQueue()
    frontier.put(initial_state)
    explored_set = set()
    steps = 1
    while not frontier.empty():
        current_state = frontier.get()
        if current_state.is_goal():
            return True
        explored_set.add(current_state)
        next_states = current_state.generate_next_states()
        for next_state in next_states:
            if next_state not in explored_set:
                frontier.put(next_state)
        # print the current state and the number of steps
        print(f"Step {steps}: {current_state.m_left}M {current_state.c_left}C {current_state.b}B --- {current_state.m_right}M {current_state.c_right}C")
        steps += 1
    return False

if solve():
    print("The problem is solvable!")
else:
    print("The problem is unsolvable!")