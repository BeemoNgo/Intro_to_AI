import pygame
import time
# Define colors
BLACK = (12, 53, 158) #wall
WHITE = (255, 255, 255) #
GREEN = (155, 207, 83)  #goal_state
RED = (251, 136, 180) #initial_state
BLUE = (145, 149, 246) #path
YELLOW = (255, 255, 0) #visited
GRAY = (255, 190, 152) #frontier
LIGHT_GRAY = (200, 200, 200) #toggle button

def delay(time_in_ms):
    pygame.time.delay(time_in_ms)
class GUI:
    def __init__(self, grid, initial_state, goal_states, path_finder):
        self.path_finder = path_finder
        self.grid = grid
        self.initial_state = initial_state
        self.goal_states = goal_states
        self.width = len(grid[0])
        self.height = len(grid)
        self.block_size = 40
        self.padding = 2
        self.border = 1
        
        # Calculate the minimum window width and height based on grid and buttons
        min_window_width = self.width * (self.block_size + self.padding)+300
        min_window_height = self.height * (self.block_size + self.padding) + 200
        
        self.window_width = max(min_window_width, self.width * (self.block_size + self.padding) * 1.5)
        self.window_height = max(min_window_height, self.height * (self.block_size + self.padding) + 200)
        
        self.window_size = (self.window_width, self.window_height)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Path Finding Visualization")
        self.buttons = self.create_buttons()  # Initialize self.buttons here
        self.selected_algorithm = None
        self.visited = []
        self.frontier = []
        self.path = []
        self.solution = []
        self.finding_state = False
        self.solution_index = 0  # To track where we are in the solution list
        self.last_update_time = time.time()  # Last time the screen was updated
        self.update_interval = 0.05  # Time
        pygame.font.init()
    
    def reset(self):
        self.path = []
        self.frontier = []
        self.visited = []
        self.last_update_time = time.time()
        self.solution_index = 0
        self.finding_state = False

    def create_buttons(self):
        buttons = []
        button_width = 120
        button_height = 50
        button_spacing_x = 20
        button_spacing_y = 10
        
        algorithms = ["BFS", "DFS", "GBFS", "AS", "CUS1", "CUS2"]
        total_buttons = len(algorithms)
        buttons_per_row = 3
        
        # Calculate the total width of the buttons and spacing in a row
        total_row_width = (button_width * buttons_per_row) + (button_spacing_x * (buttons_per_row - 1))
        
        # Calculate the starting x-coordinate to center the buttons in a row
        start_x = (self.window_width - total_row_width) // 2
        
        # Set the starting y-coordinate for the first row of buttons
        start_y = self.window_height - (button_height * 2) - (button_spacing_y * 3)
        
        for i, algorithm in enumerate(algorithms):
            row = i // buttons_per_row
            col = i % buttons_per_row
            
            x = start_x + (col * (button_width + button_spacing_x))
            y = start_y + (row * (button_height + button_spacing_y))
            
            button_rect = pygame.Rect(x, y, button_width, button_height)
            buttons.append((button_rect, algorithm))
        
        return buttons
    
    def run_pathfinding(self):
        if self.selected_algorithm:
            method = self.selected_algorithm.lower()
            goal, number_of_nodes, path, node_states = self.path_finder.find_path(method)
            # self.visited = visited
            # self.frontier = frontier
            # print(node_states)
            self.solution = node_states
            self.finding_state = True
            # self.path = path
            # self.draw_grid(path=path, visited=visited, frontier=frontier)

    def draw_grid(self, path=None, visited=None, frontier=None):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(col * (self.block_size + self.padding) + self.padding, row * (self.block_size + self.padding) + self.padding, self.block_size, self.block_size)
                if self.grid[row][col] == 1:
                    pygame.draw.rect(self.screen, BLACK, rect)
                elif (col, row) == self.initial_state:
                    pygame.draw.rect(self.screen, RED, rect)
                    pygame.draw.rect(self.screen, BLACK, rect, self.border)
                elif (col, row) in self.goal_states:
                    pygame.draw.rect(self.screen, GREEN, rect)
                    pygame.draw.rect(self.screen, BLACK, rect, self.border)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect)
                    pygame.draw.rect(self.screen, BLACK, rect, self.border)


        current_time = time.time()
        if self.finding_state and current_time - self.last_update_time > self.update_interval:
            if self.solution_index < len(self.solution):
                item = self.solution[self.solution_index]
                for node, state in item.items():
                    x,y = node
                    if state == "frontier" and not self.check_special(node):
                        self.frontier.append(node)
                    elif state == "visited" and not self.check_special(node):
                        self.visited.append(node)
                        rect = pygame.Rect(x * (self.block_size + self.padding) + self.padding, y * (self.block_size + self.padding) + self.padding, self.block_size, self.block_size)
                        pygame.draw.rect(self.screen, YELLOW, rect)
                        pygame.draw.rect(self.screen, BLACK, rect, self.border)
                    elif state == "path" and not self.check_special(node):
                        self.path.append(node)
                        rect = pygame.Rect(x * (self.block_size + self.padding) + self.padding, y * (self.block_size + self.padding) + self.padding, self.block_size, self.block_size)
                        pygame.draw.rect(self.screen, BLUE, rect)
                        pygame.draw.rect(self.screen, BLACK, rect, self.border)
                self.last_update_time = current_time
                self.solution_index += 1
                if self.solution_index >= len(self.solution):
                    self.finding_state= False
                    

        for node in self.frontier:
            if self.check_special(node):
                continue
            x, y = node
            rect = pygame.Rect(x * (self.block_size + self.padding) + self.padding, y * (self.block_size + self.padding) + self.padding, self.block_size, self.block_size)
            pygame.draw.rect(self.screen, GRAY, rect)
            pygame.draw.rect(self.screen, BLACK, rect, self.border)

        for node in self.visited:
            if self.check_special(node):
                continue
            x, y = node
            rect = pygame.Rect(x * (self.block_size + self.padding) + self.padding, y * (self.block_size + self.padding) + self.padding, self.block_size, self.block_size)
            pygame.draw.rect(self.screen, YELLOW, rect)
            pygame.draw.rect(self.screen, BLACK, rect, self.border)
   
        for node in self.path:
            if self.check_special(node):
                continue
            x, y = node
            rect = pygame.Rect(x * (self.block_size + self.padding) + self.padding, y * (self.block_size + self.padding) + self.padding, self.block_size, self.block_size)
            pygame.draw.rect(self.screen, BLUE, rect)
            pygame.draw.rect(self.screen, BLACK, rect, self.border)

        for button_rect, algorithm in self.buttons:
            button_color = LIGHT_GRAY if self.selected_algorithm == algorithm else GRAY
            pygame.draw.rect(self.screen, button_color, button_rect)
            text = pygame.font.Font(None, 24).render(algorithm, True, BLACK)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)

        pygame.display.flip()
    
    def check_special(self, node):
        if node == self.initial_state or node in self.goal_states:
            return True
        return False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button_rect, algorithm in self.buttons:
                        if not self.finding_state and button_rect.collidepoint(mouse_pos):
                            self.reset()
                            self.selected_algorithm = algorithm
                            print(f"Selected algorithm: {algorithm}")
                            self.run_pathfinding()
                            # Run the selected algorithm here
                            break

            self.screen.fill(WHITE)
            self.draw_grid()
            pygame.display.flip()

        pygame.quit()
        