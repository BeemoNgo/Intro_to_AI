# import pygame
# from bfs import bfs
# from dfs import dfs
# from gbfs import gbfs
# from a_star import a_star
# from bidirecional import cus1
# # from bidirectional_search import bidirectional_search
# # from ida_star import ida_star
# # from bidirectional_astar import bidirectional_astar

# def read_map(file_path):
#     with open(file_path, 'r') as file:
#         lines = [line.strip() for line in file.readlines()]
#         grid_size = tuple(map(int, lines[0][1:-1].split(',')))
#         initial_state = tuple(map(int, lines[1][1:-1].split(',')))
#         goal_states = [
#             tuple(int(num) for num in state.translate(str.maketrans('', '', '() ')).split(','))
#             for state in lines[2].split('|')
#         ]
#         walls = [tuple(map(int, wall[1:-1].split(','))) for wall in lines[3:]]
#         grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
#         grid[initial_state[1]][initial_state[0]] = 4
#         for x, y in goal_states:
#             grid[y][x] = 9
#         for x, y, w, h in walls:
#             for i in range(x, x + w):
#                 for j in range(y, y + h):
#                     grid[j][i] = 1
#         return grid, initial_state, goal_states

# # Pygame visualization
# def draw_grid(grid, path=None, visited=None):
#     window.fill(WHITE)
#     for row in range(len(grid)):
#         for col in range(len(grid[0])):
#             cell_rect = pygame.Rect(grid_offset[0] + col * cell_size, grid_offset[1] + row * cell_size, cell_size, cell_size)
#             if grid[row][col] == 1:
#                 pygame.draw.rect(window, BLACK, cell_rect)
#             elif grid[row][col] == 4:
#                 pygame.draw.rect(window, BLUE, cell_rect)
#             elif grid[row][col] == 9:
#                 pygame.draw.rect(window, RED, cell_rect)
#             else:
#                 pygame.draw.rect(window, GRAY, cell_rect, 1)
#             if visited and (col, row) in visited:
#                 pygame.draw.rect(window, YELLOW, cell_rect)
#             if path and (col, row) in path:
#                 pygame.draw.rect(window, GREEN, cell_rect)
#     pygame.display.flip()

# # Pygame setup
# pygame.init()
# window_size = (800, 600)
# window = pygame.display.set_mode(window_size)
# pygame.display.set_caption("Search Algorithm Visualization")
# clock = pygame.time.Clock()

# # Colors and dimensions
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GRAY = (128, 128, 128)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# cell_size = 50
# grid_offset = (100, 100)

# # Read map from file
# file_path = 'Map.txt'
# grid, initial_state, goal_states = read_map(file_path)

# # Perform search algorithms and visualize
# algorithms = [
#     ('BFS', bfs),
#     ('DFS', dfs),
#     ('Greedy Best-First Search', gbfs),
#     ('A*', a_star),
#     ('Custom Algorithm 1', cus1),
#     # ('Bidirectional Search', bidirectional_search),
#     # ('IDA*', ida_star),
#     # ('Bidirectional A*', bidirectional_astar)
# ]

# for name, algorithm in algorithms:
#     print(f"Running {name}...")
#     path, visited = algorithm(grid, initial_state, goal_states)
#     if path:
#         print(f"Path found by {name}: {path}")
#         path_coordinates = [initial_state] + [tuple(map(sum, zip(initial_state, direction))) for direction in path]
#         draw_grid(grid, path=path_coordinates, visited=visited)
#         pygame.display.set_caption(f"{name} - Path Found")
#     else:
#         print(f"No path found by {name}")
#         draw_grid(grid, path=None, visited=visited)
#         pygame.display.set_caption(f"{name} - No Path Found")
#     pygame.time.delay(3000)  # Delay between algorithms

# # Quit Pygame
# pygame.quit()
