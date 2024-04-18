import heapq
from searchClass import SearchAlgorithm

class GBFS(SearchAlgorithm):
    def __init__(self, grid, initial_state, goal_states):
        super().__init__(grid, initial_state, goal_states)

    def manhattan_distance(self, point_a):
        min_distance = float('inf')
        for goal_state in self.goal_states:
            dist = abs(point_a[0] - goal_state[0]) + abs(point_a[1] - goal_state[1])
            min_distance = min(min_distance, dist)
        return min_distance

    def find_path(self):
        queue = [(self.manhattan_distance(self.initial_state), 0, self.initial_state, [])]
        visited = set()
        number_of_nodes = 1
        visited.add(self.initial_state)

        while queue:
            f_score, _, current, path = heapq.heappop(queue)

            if current in self.goal_states:
                return current, number_of_nodes, path

            for i in range(4):
                neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])

                if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                    new_path = path + [self.movement_names[i]]
                    number_of_nodes += 1
                    f_score = self.manhattan_distance(neighbor)
                    visited.add(neighbor)
                    heapq.heappush(queue, (f_score, number_of_nodes, neighbor, new_path))

        return None, number_of_nodes, None
    
    def find_path_draw_1(self):
        queue = [(self.manhattan_distance(self.initial_state), 0, self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set([self.initial_state])  # Track nodes in the frontier
        node_states = [{self.initial_state: "frontier"}]
        number_of_nodes = 1

        while queue:
            f_score, _, current, path = heapq.heappop(queue)

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

                if self.is_valid_neighbor(current, neighbor) and neighbor not in visited and neighbor not in frontier:
                    new_path = path + [neighbor]
                    f_score = self.manhattan_distance(neighbor)
                    heapq.heappush(queue, (f_score, number_of_nodes, neighbor, new_path))
                    frontier.add(neighbor)
                    node_states.append({neighbor: "frontier"})  # Record neighbor as frontier
                    number_of_nodes += 1

        return None, number_of_nodes, None, node_states
    
    def find_path_draw(self):
        queue = [(self.manhattan_distance(self.initial_state), 0, self.initial_state, [self.initial_state])]
        visited = set()
        frontier = set()
        visited_cells = []  # Initialize a list to store visited cells
        number_of_nodes = 1
        visited.add(self.initial_state)
        while queue:
            f_score, _, current, path = heapq.heappop(queue)
            visited_cells.append(current)  # Add the current cell to the visited_cells list
            if current in self.goal_states:
                return current, number_of_nodes, path, visited_cells, frontier
            for i in range(4):
                neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])
                if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                    new_path = path + [neighbor]
                    number_of_nodes += 1
                    f_score = self.manhattan_distance(neighbor)
                    visited.add(neighbor)
                    frontier.add(neighbor)
                    heapq.heappush(queue, (f_score, number_of_nodes, neighbor, new_path))
        return None, number_of_nodes, None, visited_cells, frontier