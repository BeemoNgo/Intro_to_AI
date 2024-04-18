from searchClass import SearchAlgorithm

class CUS2(SearchAlgorithm):
    def __init__(self, grid, initial_state, goal_states):
        super().__init__(grid, initial_state, goal_states)

    def manhattan_distance(self, point_a):
        min_distance = float('inf')
        for goal_state in self.goal_states:
            dist = abs(point_a[0] - goal_state[0]) + abs(point_a[1] - goal_state[1])
            min_distance = min(min_distance, dist)
        return min_distance

    def find_path(self):
        threshold = None
        flag = False
        while True:
            if threshold is None:
                threshold = self.manhattan_distance(self.initial_state)
            path = [] #reset path
            pruned = [] #reset pruned list
            visited = set() #reset visited list
            stack = [(0, 0, 0, self.initial_state, [])]  #f_score, order, g_score, current, path)
            while stack:
                f_score, order, g_score, current, path = stack.pop()  # LIFO
                visited.add(current)

                if current in self.goal_states:
                    flag = True
                    break #stop the prpgrm when a goal is found
                
                for i in range(4):  
                    neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                        g_score_new = g_score + 1
                        h_score = self.manhattan_distance(neighbor)
                        f_score_new = g_score_new + h_score
                        if f_score_new <= threshold:
                            new_path = path + [self.movement_names[i]]
                            self.number_of_nodes += 1
                            stack.append((f_score_new, self.number_of_nodes, g_score_new, neighbor, new_path))
                        else: 
                            pruned.append((f_score_new))
            if flag:
                return current, self.number_of_nodes, path
            elif not pruned: #if both stack and pruned lists are None the program cannot reach the goal
                return None, self.number_of_nodes, None
            else: #if pruned list is not empty
                threshold = min(f_score_new for f_score_new in pruned)
        
    def find_path_draw_1(self):
        threshold = None
        flag = False
        node_states = [{self.initial_state: "frontier"}]
        while True:
            if threshold is None:
                threshold = self.manhattan_distance(self.initial_state)
        
            path = [] #reset path
            pruned = [] #reset pruned list
            visited = set() #reset visited list
            stack = [(0, 0, 0, self.initial_state, [])]  #f_score, order, g_score, current, path)
            while stack:
                f_score, order, g_score, current, path = stack.pop()  # LIFO
                visited.add(current)
                node_states.append({current: "visited"})
                if current in self.goal_states:
                    flag = True
                    for p in path:
                        node_states.append({p: "path"})  # Add path nodes to states
                    node_states.append({current: "path"})  # Mark goal as path
                    break #stop the prpgrm when a goal is found
                
                for i in range(4):  
                    neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])
                    if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                        g_score_new = g_score + 1
                        h_score = self.manhattan_distance(neighbor)
                        f_score_new = g_score_new + h_score
                        if f_score_new <= threshold:
                            new_path = path + [neighbor]
                            self.number_of_nodes += 1
                            node_states.append({neighbor: "frontier"})
                           
                            stack.append((f_score_new, self.number_of_nodes, g_score_new, neighbor, new_path))
                        else: 
                            pruned.append((f_score_new))
            if flag:
                return current, self.number_of_nodes, path, node_states
            elif not pruned: #if both stack and pruned lists are None the program cannot reach the goal
                return None, self.number_of_nodes, None,node_states
            else: #if pruned list is not empty
                threshold = min(f_score_new for f_score_new in pruned)
              
            


# Assuming you have the necessary grid, initial and goal states defined
# ida_star_instance = IDAStar(grid, initial_state, goal_states)
# result = ida_star_instance.find_path()
# print(result)