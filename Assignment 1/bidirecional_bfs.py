from searchClass import SearchAlgorithm
from collections import deque

class CUS1(SearchAlgorithm):
    def find_path(self):
        forward_queue = deque([(self.initial_state, [])])
        backward_queue = deque([(goal_state, []) for goal_state in self.goal_states])
        forward_visited = {self.initial_state: []}
        backward_visited = {goal_state: [] for goal_state in self.goal_states}

        while forward_queue and backward_queue:
            if forward_queue:
                current_forward, path_forward = forward_queue.popleft()
                forward_visited[current_forward] = path_forward

                for i in range(4):
                    forward_neighbor = (current_forward[0] + self.directions[i][0], current_forward[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current_forward, forward_neighbor) and forward_neighbor not in forward_visited:
                        new_path = path_forward + [self.movement_names[i]]
                        forward_queue.append((forward_neighbor, new_path))
                        forward_visited[forward_neighbor] = new_path
                        self.number_of_nodes += 1
                        if forward_neighbor in backward_visited:
                            return forward_neighbor, self.number_of_nodes, new_path + self.reverse_directions(backward_visited[forward_neighbor][::-1])

            if backward_queue:
                current_backward, path_backward = backward_queue.popleft()
                backward_visited[current_backward] = path_backward

                for i in range(4):
                    backward_neighbor = (current_backward[0] + self.directions[i][0], current_backward[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current_backward, backward_neighbor) and backward_neighbor not in backward_visited:
                        new_path = path_backward + [self.movement_names[i]]
                        backward_queue.append((backward_neighbor, new_path))
                        backward_visited[backward_neighbor] = new_path
                        self.number_of_nodes += 1
                        if backward_neighbor in forward_visited:
                            return backward_neighbor, self.number_of_nodes, forward_visited[backward_neighbor] + self.reverse_directions(new_path[::-1])

        return None, self.number_of_nodes, None
    def find_path_draw_1(self): #For tracking the node expanded
        forward_queue = deque([(self.initial_state, [self.initial_state])])
        backward_queue = deque([(goal_state, [goal_state]) for goal_state in self.goal_states])
        forward_visited = {self.initial_state: []}
        backward_visited = {goal_state: [] for goal_state in self.goal_states}
        node_states = [{self.initial_state: "frontier"}, {goal: "frontier" for goal in self.goal_states}]

        while forward_queue and backward_queue:
            if forward_queue:
                current_forward, path_forward = forward_queue.popleft()
                forward_visited[current_forward] = path_forward
                node_states.append({current_forward: "visited"})  # Mark as visited

                for i in range(4):
                    forward_neighbor = (current_forward[0] + self.directions[i][0], current_forward[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current_forward, forward_neighbor) and forward_neighbor not in forward_visited:
                        new_path = path_forward + [forward_neighbor]
                        forward_queue.append((forward_neighbor, new_path))
                        forward_visited[forward_neighbor] = new_path
                        node_states.append({forward_neighbor: "frontier"})  # Add to frontier
                        self.number_of_nodes += 1
                        if forward_neighbor in backward_visited:
                            # Meeting point
                            complete_path = new_path + backward_visited[forward_neighbor][::-1]
                            for x in complete_path:
                                node_states.append({x:"path"})
                            return forward_neighbor, self.number_of_nodes, complete_path, node_states

            if backward_queue:
                current_backward, path_backward = backward_queue.popleft()
                backward_visited[current_backward] = path_backward
                node_states.append({current_backward: "visited"})  # Mark as visited

                for i in range(4):
                    backward_neighbor = (current_backward[0] + self.directions[i][0], current_backward[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current_backward, backward_neighbor) and backward_neighbor not in backward_visited:
                        new_path = path_backward + [backward_neighbor]
                        backward_queue.append((backward_neighbor, new_path))
                        backward_visited[backward_neighbor] = new_path
                        node_states.append({backward_neighbor: "frontier"})  # Add to frontier
                        self.number_of_nodes += 1
                        if backward_neighbor in forward_visited:
                            # Meeting point
                            complete_path = forward_visited[backward_neighbor] + new_path[::-1]
                            for x in complete_path:
                                node_states.append({x:"path"})
                            return backward_neighbor, self.number_of_nodes, complete_path, node_states

        return None, self.number_of_nodes, None, node_states
    def reverse_directions(self,directions):
        # Define a dictionary to map each direction to its opposite
        opposite = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        # Use list comprehension to replace each direction with its opposite
        reversed_directions = [opposite[dir] for dir in directions if dir in opposite]
        return reversed_directions

    def find_path_draw(self): #For visualising the methods
        # Initialize queues for both directions with the start or goal states and the paths taken to get there
        forward_queue = deque([(self.initial_state, [self.initial_state])])
        backward_queue = deque([(goal_state, [goal_state]) for goal_state in self.goal_states])

        # Set up visited tracking for both directions
        forward_visited = {self.initial_state: [self.initial_state]}
        backward_visited = {goal_state: [goal_state] for goal_state in self.goal_states}

        # Set up combined visited and frontier for visualization
        combined_visited = set(forward_visited.keys() | backward_visited.keys())
        combined_frontier = set(forward_visited.keys() | backward_visited.keys())

        while forward_queue and backward_queue:
            if forward_queue:
                current_forward, path_forward = forward_queue.popleft()
                combined_visited.add(current_forward)  # Update combined visited
                combined_frontier.add(current_forward)  # Update combined frontier

                for i in range(4):
                    forward_neighbor = (current_forward[0] + self.directions[i][0], current_forward[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current_forward, forward_neighbor) and forward_neighbor not in forward_visited:
                        new_path = path_forward + [forward_neighbor]
                        forward_queue.append((forward_neighbor, new_path))
                        forward_visited[forward_neighbor] = new_path
                        combined_visited.add(forward_neighbor)  # Update combined visited
                        combined_frontier.add(forward_neighbor)  # Update combined frontier
                        self.number_of_nodes += 1
                        if forward_neighbor in backward_visited:
                            complete_path = new_path + backward_visited[forward_neighbor][::-1]
                            return forward_neighbor, self.number_of_nodes, complete_path, combined_visited, combined_frontier

            if backward_queue:
                current_backward, path_backward = backward_queue.popleft()
                combined_visited.add(current_backward)  # Update combined visited
                combined_frontier.add(current_backward)  # Update combined frontier

                for i in range(4):
                    backward_neighbor = (current_backward[0] + self.directions[i][0], current_backward[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current_backward, backward_neighbor) and backward_neighbor not in backward_visited:
                        new_path = path_backward + [backward_neighbor]
                        backward_queue.append((backward_neighbor, new_path))
                        backward_visited[backward_neighbor] = new_path
                        combined_visited.add(backward_neighbor)  # Update combined visited
                        combined_frontier.add(backward_neighbor)  # Update combined frontier
                        self.number_of_nodes += 1
                        if backward_neighbor in forward_visited:
                            complete_path = forward_visited[backward_neighbor] + new_path[::-1]
                            return backward_neighbor, self.number_of_nodes, complete_path, combined_visited, combined_frontier

        return None, self.number_of_nodes, None, combined_visited, combined_frontier
