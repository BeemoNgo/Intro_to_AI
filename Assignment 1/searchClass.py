class SearchAlgorithm:
    def __init__(self, grid, initial_state, goal_states):
        self.grid = grid
        self.initial_state = initial_state
        self.goal_states = goal_states
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.movement_names = ['up', 'left', 'down', 'right']
        self.number_of_nodes = 1
    def find_path(self):
        """
        This method should be overridden by the child classes to implement
        the specific search algorithm.
        """
        raise NotImplementedError("The find_path method must be implemented by the child class.")

    def is_valid_neighbor(self, current, neighbor):
        """
        Helper method to check if a neighbor is valid.
        """
        return (
            0 <= neighbor[0] < len(self.grid[0])
            and 0 <= neighbor[1] < len(self.grid)
            and self.grid[neighbor[1]][neighbor[0]] != 1
        )

    def get_neighbors(self, current, visited):
        """
        Helper method to get valid neighbors of a given state.
        """
        neighbors = []
        for i in range(4):
            neighbor = (current[0] + self.directions[i][0], current[1] + self.directions[i][1])
            if self.is_valid_neighbor(current, neighbor) and neighbor not in visited:
                neighbors.append((neighbor, self.movement_names[i]))
        return neighbors