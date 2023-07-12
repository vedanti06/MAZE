import maze
import generate_maze
import random
import queue
import sys


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    cell_stack = []
    current_cell = 0
    visited_cells = 0

    while current_cell != m.total_cells - 1:
        neighbors = m.cell_neighbors(current_cell)
        if neighbors:
            new_cell, dir = random.choice(neighbors)
            m.visit_cell(current_cell, new_cell, dir)
            cell_stack.append(current_cell)
            current_cell = new_cell
            visited_cells += 1
        else:
            m.backtrack(current_cell)
            current_cell = cell_stack.pop()
        m.refresh_maze_view()

    print_solution_array(m)
    m.state = 'idle'


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    cell_queue = queue.Queue()
    current_cell = 0
    in_dir = 0b0000
    visited_cells = 0
    cell_queue.put((current_cell, in_dir))

    while current_cell != m.total_cells - 1 and not cell_queue.empty():
        current_cell, in_dir = cell_queue.get()
        m.bfs_visit_cell(current_cell, in_dir)
        visited_cells += 1
        m.refresh_maze_view()

        neighbors = m.cell_neighbors(current_cell)
        for n in neighbors:
            cell_queue.put(n)

    m.reconstruct_solution(current_cell)

    print_solution_array(m)
    m.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='bfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()