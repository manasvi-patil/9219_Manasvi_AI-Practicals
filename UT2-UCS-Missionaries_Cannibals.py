from queue import PriorityQueue

class State:
    def __init__(self, left_m, left_c, boat_pos):
        self.left_m = left_m
        self.left_c = left_c
        self.boat_pos = boat_pos

    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return (self.left_m == other.left_m and
                self.left_c == other.left_c and
                self.boat_pos == other.boat_pos)

    def __hash__(self):
        return hash((self.left_m, self.left_c, self.boat_pos))

    def is_valid(self):
        if self.left_m < 0 or self.left_c < 0 or self.left_m > 3 or self.left_c > 3:
            return False
        if self.left_c > self.left_m and self.left_m > 0:
            return False
        if 3 - self.left_c > 3 - self.left_m and 3 - self.left_m > 0:
            return False
        return True

    def get_successors(self):
        successors = []
        if self.boat_pos == 'left':
            for i in range(3):
                for j in range(3):
                    if i+j > 2:
                        continue
                    state = State(self.left_m - i, self.left_c - j, 'right')
                    if state.is_valid():
                        successors.append((state, (i, j)))
        else:
            for i in range(3):
                for j in range(3):
                    if i+j > 2:
                        continue
                    state = State(self.left_m + i, self.left_c + j, 'left')
                    if state.is_valid():
                        successors.append((state, (i, j)))
        return successors

def ucs(start_state):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start_state, []))

    while not pq.empty():
        cost, state, path = pq.get()

        if state not in visited:
            visited.add(state)

            if state.left_m == 0 and state.left_c == 0 and state.boat_pos == 'right':
                return path + [(state, (0, 0))]

            for successor, step_cost in state.get_successors():
                pq.put((cost + 1, successor, path + [(state, step_cost)]))

    return None

start_state = State(3, 3, 'left')
solution = ucs(start_state)

if solution is None:
    print("No solution found")
else:
    print("Solution found with cost", solution[-1][1])
    for state, step_cost in solution:
        if step_cost == (0, 0):
            print("Boat is now on the", state.boat_pos, "bank")
        else:
            print("Boat moved", step_cost[0], "missionaries and", step_cost[1], "cannibals from", state.boat_pos, "to the other bank")
        print("Left bank:", state.left_m, "M", state.left_c, "C")
        print("Right bank:", 3 - state.left_m, "M", 3 - state.left_c, "C")
        print()