import heapq

def distance_hn(point_a, goal_states):
    min_distance = float('inf')
    for goal_state in goal_states:
        dist = abs(point_a[0] - goal_state[0]) + abs(point_a[1] - goal_state[1])
        min_distance = min(min_distance, dist)
    return min_distance

def a_star(grid, initial_state, goal_states):
    queue = [(0, 0, 0, initial_state, [])]
    visited = set()
    number_of_nodes = 1
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    movement_names = ['up', 'left', 'down', 'right']
    visited.add(initial_state)

    while queue:
        f_score, order, g_score, current, path = heapq.heappop(queue)
                    #origin to current
        if current in goal_states:
            return current, number_of_nodes, path

        for i in range(4):
            neighbor = (current[0] + directions[i][0], current[1] + directions[i][1])
            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid) and \
               grid[neighbor[1]][neighbor[0]] != 1 and neighbor not in visited:
                new_path = path + [movement_names[i]]
                g_score_new = g_score + 1
                h_score = distance_hn(neighbor, goal_states)
                f_score_new = g_score_new + h_score
                number_of_nodes += 1
                visited.add(neighbor)
                heapq.heappush(queue, (f_score_new, number_of_nodes, g_score_new, neighbor, new_path))

    return None, number_of_nodes, None
