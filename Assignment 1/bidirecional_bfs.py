def cus1(grid, initial_state, goal_states):
    forward_queue = [(initial_state, [])]
    backward_queue = [(goal_state, []) for goal_state in goal_states]
    forward_visited = set()
    backward_visited = set()
    number_of_nodes = 1

    # Directions for moving up, left, down, and right
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    movement_names = ['up', 'left', 'down', 'right']

    while forward_queue and backward_queue:
        current_forward, path_forward = forward_queue.pop(0)
        current_backward, path_backward = backward_queue.pop(0)

        if current_forward in backward_visited:
            print("Node: ", current_forward)
            print(number_of_nodes)
            return path_forward + path_backward[::-1]
        if current_backward in forward_visited:
            print("Node: ", current_backward)
            print(number_of_nodes)
            return path_forward + path_backward[::-1]

        forward_visited.add(current_forward)
        backward_visited.add(current_backward)

        for i in range(4):
            forward_neighbor = (current_forward[0] + directions[i][0], current_forward[1] + directions[i][1])
            backward_neighbor = (current_backward[0] + directions[i][0], current_backward[1] + directions[i][1])

            if 0 <= forward_neighbor[0] < len(grid[0]) and 0 <= forward_neighbor[1] < len(grid) and \
                    grid[forward_neighbor[1]][forward_neighbor[0]] != 1 and forward_neighbor not in forward_visited:
                forward_queue.append((forward_neighbor, path_forward + [movement_names[i]]))
                forward_visited.add(forward_neighbor)
                number_of_nodes += 1

            if 0 <= backward_neighbor[0] < len(grid[0]) and 0 <= backward_neighbor[1] < len(grid) and \
                    grid[backward_neighbor[1]][backward_neighbor[0]] != 1 and backward_neighbor not in backward_visited:
                backward_queue.append((backward_neighbor, path_backward + [movement_names[i]]))
                backward_visited.add(backward_neighbor)
                number_of_nodes += 1

    return None, number_of_nodes, None
