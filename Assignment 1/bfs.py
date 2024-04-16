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
    # def find_path_draw(self, output_file ="res.txt"):
    #     queue = [(self.initial_state, [self.initial_state])]
    #     visited = set()
    #     frontier = set()
    #     number_of_nodes = 1
    #     with open(output_file, 'w') as file:
    #         while queue:
    #             current, path = queue.pop(0)
    #             visited.add(current)
    #             file.write(f"Node: {current}, Visited: {visited}, Frontier: {frontier}, Path: {path}\n")
    #             if current in self.goal_states:
    #                 file.write(f"Goal reached: {current}, Number of nodes: {number_of_nodes}, Path: {path}\n")
    #                 return
    #             for neighbor, _ in self.get_neighbors(current, visited):
    #                 new_path = path + [neighbor]
    #                 queue.append((neighbor, new_path))
    #                 frontier.add(neighbor)
    #                 number_of_nodes += 1
    #         file.write(f"No goal found, Number of nodes: {number_of_nodes}\n")