

def dfs(grid, initial_state, goal_states):
    stack = [(initial_state, [])]
    visited = set()
    number_of_nodes = 1

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)][::-1]
    movement_names = ['up', 'left', 'down', 'right'][::-1]

    while stack:
        current, path = stack.pop()
        if current in visited:
            continue

        visited.add(current)

        if current in goal_states:
            return current, number_of_nodes, path

        for i in range(4):
            neighbor = (current[0] + directions[i][0], current[1] + directions[i][1])

            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid) and \
               grid[neighbor[1]][neighbor[0]] != 1 and neighbor not in visited:
                stack.append((neighbor, path + [movement_names[i]]))
                number_of_nodes += 1

    return None, number_of_nodes, None
