import resource
import sys

import numpy as np

from AStar import AStar
from Board import Board


def main():
    p = Board(np.array(eval(sys.argv[2])))
    alg = sys.argv[1]
    if alg == 'ast':
        s = AStar(p)
    else:
        print("Invalid input, continuing through A*")
        s = AStar(p)
    s.solve()

    file = open(f'{alg}_output1.txt', 'w')

    file.write('path_to_goal: ' + str(s.path) + '\n')
    file.write('cost_of_path: ' + str(len(s.path)) + '\n')
    file.write('nodes_expanded: ' + str(s.nodes_expanded) + '\n')
    file.write('nodes_explored: ' + str(len(s.explored_nodes)) + '\n')
    file.write('search_depth: ' + str(s.solution.depth) + '\n')
    file.write('max_search_depth: ' + str(s.max_depth) + '\n')
    file.write('running_time: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_utime + \
                                      resource.getrusage(resource.RUSAGE_SELF).ru_stime) + '\n')
    file.write('max_ram_usage: ' + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))

    file.close()


if __name__ == "__main__":
    main()