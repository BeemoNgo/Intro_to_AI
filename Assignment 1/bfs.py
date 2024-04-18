from searchClass import SearchAlgorithm
class BFS(SearchAlgorithm):
    def find_path(self):
        queue = [(self.initial_state, [])]
        visited = set()

        while queue:
            current, path = queue.pop(0)
            visited.add(current)

            if current in self.goal_states:
                return current, self.number_of_nodes, path

            for neighbor, movement in self.get_neighbors(current, visited):
                queue.append((neighbor, path + [movement]))
                visited.add(neighbor)
                self.number_of_nodes += 1

        return None, self.number_of_nodes, None
    def find_path_draw(self):
        queue = [(self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        while queue:
            current, path = queue.pop(0)
            visited.add(current)
            if current in self.goal_states:
                return current, self.number_of_nodes, path, visited, frontier
            for neighbor, _ in self.get_neighbors(current, visited):
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
                frontier.add(neighbor)
                self.number_of_nodes += 1
        return None, self.number_of_nodes, None, visited, frontier
    
   
    def find_path_draw_1(self):
        queue = [(self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        node_states = [{self.initial_state: "frontier"}]  # List to track the state changes of nodes
        

        while queue:
            current, path = queue.pop(0)
            visited.add(current)
            node_states.append({current: "visited"})  # Record current node as visited

            if current in self.goal_states:
                # Update all nodes as visited first, except those already marked or in path
                for node in node_states[-1]:
                    if node not in path:
                        node_states.append({node: "visited"})
                
                # Finally, mark the path nodes
                for node in path:
                    node_states.append({node: "path"})
                return current, self.number_of_nodes, path, node_states

            for neighbor, _ in self.get_neighbors(current, visited):
                if neighbor not in visited and neighbor not in frontier:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
                    frontier.add(neighbor)
                    node_states.append({neighbor: "frontier"})  # Record neighbors as frontier
                self.number_of_nodes += 1

        return None, self.number_of_nodes, None, node_states   