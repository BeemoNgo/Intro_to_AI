import sys
from bfs import BFS
from dfs import DFS
from gbfs import GBFS
from a_star import AStar
from bidirecional_bfs import CUS1
from ida import CUS2

class Generate:
    def __init__(self, file_path):
        self.grid, self.initial_state, self.goal_states = self.read_map(file_path)
        self.methods = ["bfs", 'dfs', "as", "gbfs", "cus1", "cus2"]

    def read_map(self, file_path):
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

    def find_path(self, method):
        goal = None
        number_of_node = 0
        path = None

        if method in self.methods:
            if method == "bfs":
                path_finder = BFS(self.grid, self.initial_state, self.goal_states)
                goal, number_of_node, path = path_finder.find_path()
            elif method == "dfs":
                path_finder = DFS(self.grid, self.initial_state, self.goal_states)
                goal, number_of_node, path = path_finder.find_path()
            elif method == "gbfs":
                path_finder = GBFS(self.grid, self.initial_state, self.goal_states)
                goal, number_of_node, path = path_finder.find_path()
            elif method == "as":
                path_finder = AStar(self.grid, self.initial_state, self.goal_states)
                goal, number_of_node, path = path_finder.find_path()
            elif method == "cus1":
                path_finder = CUS1(self.grid, self.initial_state, self.goal_states)
                goal, number_of_node, path = path_finder.find_path()
            elif method == "cus2":
                path_finder = CUS2(self.grid, self.initial_state, self.goal_states)
                goal, number_of_node, path = path_finder.find_path()
        else:
            print("Unknown method")

        return goal, number_of_node, path

if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_path = sys.argv[1]
        method = sys.argv[2].lower()

        path_finder = Generate(file_path)
        goal, number_of_node, path = path_finder.find_path(method)

        print(f'{sys.argv[1]} {method}')
        if goal is None:
            print("No goal is reachable;", number_of_node)
        else:
            print(f"<Node {goal}> {number_of_node}")
            print(path)
    else:
        print("Wrong number of arguments")