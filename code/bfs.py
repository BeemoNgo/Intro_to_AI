
def bfs(grid, initial_state, goal_states):
    queue = [(initial_state, [])]  # Store the state and its corresponding path
    visited = set()
    number_of_nodes = 1

    # Directions for moving up, left, down, and right
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    movement_names = ['up', 'left', 'down', 'right']

    while queue:
        # draw_grid(grid, path=None, visited=visited)
        # pygame.time.delay(100)  # Delay to visualize the search process
        current, path = queue.pop(0)

        visited.add(current)

        if current in goal_states:
            return current, number_of_nodes, path

        for i in range(4):
            neighbor = (current[0] + directions[i][0], current[1] + directions[i][1])

            # Check if the neighbor is within the grid bounds and not visited
            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid) and \
               grid[neighbor[1]][neighbor[0]] != 1 and neighbor not in visited:
                queue.append((neighbor, path + [movement_names[i]]))
                visited.add(neighbor)
                number_of_nodes += 1


    return None, number_of_nodes, None
