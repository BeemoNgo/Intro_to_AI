from searchClass import SearchAlgorithm
class BFS(SearchAlgorithm):
    def find_path(self):
        queue = [(self.initial_state, [])]
        visited = set()
        number_of_nodes = 1

        while queue:
            current, path = queue.pop(0)
            visited.add(current)

            if current in self.goal_states:
                return current, number_of_nodes, path

            for neighbor, movement in self.get_neighbors(current, visited):
                queue.append((neighbor, path + [movement]))
                visited.add(neighbor)
                number_of_nodes += 1

        return None, number_of_nodes, None
    def find_path_draw(self):
        queue = [(self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        number_of_nodes = 1
        while queue:
            current, path = queue.pop(0)
            visited.add(current)
            if current in self.goal_states:
                return current, number_of_nodes, path, visited, frontier
            for neighbor, _ in self.get_neighbors(current, visited):
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                frontier.add(neighbor)
                number_of_nodes += 1
        return None, number_of_nodes, None, visited, frontier
    
    def find_path_draw_1(self):
        queue = [(self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        node_states = {}
        number_of_nodes = 1
        while queue:
            current, path = queue.pop(0)
            visited.add(current)
            node_states[current] = "visited"
            if current in self.goal_states:
                node_states[current] = "path"
                for node in path:
                    node_states[node] = "path"
                return current, number_of_nodes, path, node_states
            for neighbor, _ in self.get_neighbors(current, visited):
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                frontier.add(neighbor)
                if neighbor not in node_states:
                    node_states[neighbor] = "frontier"
                number_of_nodes += 1
        return None, number_of_nodes, None, node_states
    