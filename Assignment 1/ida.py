import heapq

def distance(point_a, goal_states):
    min_distance = float('inf')
    for goal_state in goal_states:
        dist = abs(point_a[0] - goal_state[0]) + abs(point_a[1] - goal_state[1])
        min_distance = min(min_distance, dist)
    return min_distance

def ida_star(grid, initial_state, goal_states):
    def dfs(current, path, g_score, threshold):
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)][::-1]
        movement_names = ['up', 'left', 'down', 'right'][::-1]
        nonlocal number_of_nodes
        f_score = g_score + distance(current, goal_states)
        if f_score > threshold:
            return f_score
        if current in goal_states:
            return current, number_of_nodes, path
        min_cost = float('inf')
        for i in range(4):
            neighbor = (current[0] + directions[i][0], current[1] + directions[i][1])
            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid) and \
                    grid[neighbor[1]][neighbor[0]] != 1 and neighbor not in path:
                number_of_nodes += 1
                new_path = path + [movement_names[i]]
                cost = dfs(neighbor, new_path, g_score + 1, threshold)
                if isinstance(cost, list):
                    return cost
                min_cost = min(min_cost, cost)
        return min_cost

    threshold = distance(initial_state, goal_states)
    number_of_nodes = 1
    while True:
        path = dfs(initial_state, [], 0, threshold)
        if isinstance(path, list):
            return path
        if path == float('inf'):
            print('No goal is reachable; ', number_of_nodes)
            return None
        threshold = path


