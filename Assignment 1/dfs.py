from searchClass import SearchAlgorithm

class DFS(SearchAlgorithm):
    def __init__(self, grid, initial_state, goal_states):
        super().__init__(grid, initial_state, goal_states)
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)][::-1]  # Reverse the order of directions
        self.movement_names = ['up', 'left', 'down', 'right'][::-1]  # Reverse the order of movement names

    def find_path(self):
        stack = [(self.initial_state, [])]
        visited = set()
        number_of_nodes = 1

        while stack:
            current, path = stack.pop()

            if current in visited:
                continue

            visited.add(current)

            if current in self.goal_states:
                return current, number_of_nodes, path

            for i in range(4):
                neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])

                if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                    stack.append((neighbor, path + [self.movement_names[i]]))
                    number_of_nodes += 1

        return None, number_of_nodes, None
    def find_path_draw(self):
        stack = [(self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        visited_cells = []  # Initialize a list to store visited cells
        number_of_nodes = 1
        while stack:
            current, path = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            visited_cells.append(current)  # Add the current cell to the visited_cells list
            if current in self.goal_states:
                return current, number_of_nodes, path, visited_cells, frontier
            for i in range(4):
                neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])
                if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))
                    frontier.add(neighbor)
                    number_of_nodes += 1
        return None, number_of_nodes, None, visited_cells, frontier
    def find_path_draw_1(self):
        stack = [(self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        node_states = [{self.initial_state: "frontier"}]  # Initial state as frontier
        number_of_nodes = 1

        while stack:
            current, path = stack.pop()

            if current in visited:
                continue

            visited.add(current)
            node_states.append({current: "visited"})  # Record current node as visited

            if current in self.goal_states:
                # Mark all path nodes
                for node in path:
                    node_states.append({node: "path"})
                return current, number_of_nodes, path, node_states

            for i in range(4):
                neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])

                if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
                    frontier.add(neighbor)
                    node_states.append({neighbor: "frontier"})  # Record neighbor as frontier
                    number_of_nodes += 1

        return None, number_of_nodes, None, node_states