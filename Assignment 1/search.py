import sys
from bfs import bfs
from dfs import dfs
from gbfs import gbfs
from a_star import a_star
from bidirecional_bfs import cus1

def read_map(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
        grid_size = tuple(map(int, lines[0][1:-1].split(',')))
        initial_state = tuple(map(int, lines[1][1:-1].split(',')))

        goal_states = [
            tuple(int(num) for num in state.translate(str.maketrans('', '', '() ')).split(','))
            for state in lines[2].split('|')
        ]

        walls = [tuple(map(int, wall[1:-1].split(','))) for wall in lines[3:]]

        grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
        grid[initial_state[1]][initial_state[0]] = 4
        for x, y in goal_states:
            grid[y][x] = 9
        for x, y, w, h in walls:
            for i in range(x, x + w):
                for j in range(y, y + h):
                    grid[j][i] = 1

        return grid, initial_state, goal_states

methods = ["bfs",'dfs',"as","gbfs","cus1","cus2"]
if len(sys.argv) == 3:
    file_path = sys.argv[1]
    method = sys.argv[2].lower()
    grid, initial_state, goal_states = read_map(file_path)
    goal = None
    number_of_node = 0
    path = None
    if method in methods:
        if method == "bfs":
           goal, number_of_node, path = bfs(grid, initial_state, goal_states)
        elif method == "dfs":
            goal, number_of_node, path = dfs(grid, initial_state, goal_states)
        elif method == "gbfs":
            goal, number_of_node, path = gbfs(grid, initial_state, goal_states)
        elif method == "as":
            goal, number_of_node, path = a_star(grid, initial_state, goal_states)
        elif method == "cus1":
            goal, number_of_node, path = cus1(grid, initial_state, goal_states)
        # elif method == "cus2":
        #goal, number_of_node, path = cus2(grid, initial_state, goal_states))
        print(f'{sys.argv[1]} {method}')
        if goal is None:
            print("No goal is reachable; ", number_of_node)
        else:
            print(goal,number_of_node)
            print(path)
    else:
        print("Unknown method")
elif len(sys.argv) > 2:
    print("wrong number of argument")








