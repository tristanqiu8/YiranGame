import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Window settings
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Spaceship Assembly Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
DARK_BLUE = (0, 0, 139)
SPACE_BLACK = (10, 10, 30)

# Clock
clock = pygame.time.Clock()

# Game states
COMPONENT_INTRO = "intro"
ASSEMBLY = "assembly" 
LAUNCH = "launch"

class SpaceshipComponent:
    def __init__(self, name, description, color, size, position):
        self.name = name
        self.description = description
        self.color = color
        self.size = size
        self.position = position
        self.target_position = position
        self.is_assembled = False
        self.intro_shown = False
        
    def move_to_target(self, speed=2):
        dx = self.target_position[0] - self.position[0]
        dy = self.target_position[1] - self.position[1]
        distance = math.sqrt(dx*dx + dy*dy)
        
        if distance > speed:
            self.position = (
                self.position[0] + (dx/distance) * speed,
                self.position[1] + (dy/distance) * speed
            )
            return False
        else:
            self.position = self.target_position
            return True
    
    def draw(self, screen):
        x, y = int(self.position[0]), int(self.position[1])
        
        if self.name == "Command Module":
            # Command module - rounded rectangle
            pygame.draw.ellipse(screen, self.color, (x-40, y-20, 80, 40))
            pygame.draw.circle(screen, BLUE, (x, y-5), 8)  # Window
            
        elif self.name == "Main Engine":
            # Main engine - cone shape
            points = [(x-30, y+20), (x+30, y+20), (x+15, y-20), (x-15, y-20)]
            pygame.draw.polygon(screen, self.color, points)
            # Engine flames when assembled
            if self.is_assembled:
                flame_points = [(x-15, y+20), (x+15, y+20), (x, y+40)]
                pygame.draw.polygon(screen, ORANGE, flame_points)
                
        elif self.name == "Fuel Tank":
            # Fuel tank - cylindrical
            pygame.draw.rect(screen, self.color, (x-25, y-30, 50, 60))
            pygame.draw.ellipse(screen, self.color, (x-25, y-35, 50, 10))
            pygame.draw.ellipse(screen, self.color, (x-25, y+25, 50, 10))
            
        elif self.name == "Solar Panels":
            # Solar panels - rectangular with grid
            pygame.draw.rect(screen, self.color, (x-60, y-15, 120, 30))
            # Draw grid pattern
            for i in range(0, 120, 20):
                pygame.draw.line(screen, BLACK, (x-60+i, y-15), (x-60+i, y+15), 1)
            for i in range(0, 30, 10):
                pygame.draw.line(screen, BLACK, (x-60, y-15+i), (x+60, y-15+i), 1)
                
        elif self.name == "Communication Antenna":
            # Communication antenna
            pygame.draw.rect(screen, self.color, (x-5, y-20, 10, 40))
            pygame.draw.circle(screen, self.color, (x, y-25), 8)
            # Antenna lines
            for angle in range(0, 360, 45):
                end_x = x + 15 * math.cos(math.radians(angle))
                end_y = y - 25 + 15 * math.sin(math.radians(angle))
                pygame.draw.line(screen, self.color, (x, y-25), (end_x, end_y), 2)
                
        elif self.name == "Landing Module":
            # Landing module
            pygame.draw.rect(screen, self.color, (x-20, y-15, 40, 30))
            # Landing legs
            pygame.draw.line(screen, BLACK, (x-20, y+15), (x-30, y+25), 3)
            pygame.draw.line(screen, BLACK, (x+20, y+15), (x+30, y+25), 3)
            pygame.draw.line(screen, BLACK, (x, y+15), (x, y+25), 3)

class SpaceshipGame:
    def __init__(self):
        self.state = COMPONENT_INTRO
        self.current_component_index = 0
        self.assembly_progress = 0
        self.current_assembly_component = 0  # Track which component is being assembled
        self.assembly_complete = False
        self.spaceship_y = WINDOW_HEIGHT // 2
        self.stars = self.generate_stars()
        
        # Define spaceship components
        self.components = [
            SpaceshipComponent("Command Module", "Where astronauts live and control the ship", SILVER, (80, 40), (200, 200)),
            SpaceshipComponent("Main Engine", "Provides powerful thrust for the spaceship", RED, (60, 40), (200, 300)),
            SpaceshipComponent("Fuel Tank", "Stores rocket fuel for the journey", BLUE, (50, 60), (200, 400)),
            SpaceshipComponent("Solar Panels", "Collect solar energy to power the ship", DARK_BLUE, (120, 30), (200, 500)),
            SpaceshipComponent("Communication Antenna", "Communicates with ground control", YELLOW, (30, 50), (200, 600)),
            SpaceshipComponent("Landing Module", "Used for landing on other planets", GRAY, (40, 30), (200, 700))
        ]
        
        # Set assembly target positions - assemble in logical order
        center_x, center_y = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        
        # Reorder components for assembly sequence
        self.assembly_order = [2, 1, 5, 0, 3, 4]  # Fuel tank, engine, landing, command, solar, antenna
        
        self.components[0].target_position = (center_x, center_y - 60)      # Command module top
        self.components[1].target_position = (center_x, center_y + 80)      # Engine bottom
        self.components[2].target_position = (center_x, center_y)           # Fuel tank center
        self.components[3].target_position = (center_x, center_y - 30)      # Solar panels
        self.components[4].target_position = (center_x, center_y - 90)      # Antenna top
        self.components[5].target_position = (center_x, center_y + 40)      # Landing module
        
    def generate_stars(self):
        import random
        stars = []
        for _ in range(100):
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            brightness = random.randint(100, 255)
            stars.append((x, y, brightness))
        return stars
    
    def draw_text(self, text, x, y, size=24, color=BLACK):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        screen.blit(text_surface, (x, y))
    
    def draw_intro_phase(self):
        screen.fill(WHITE)
        
        # Draw title
        self.draw_text("Spaceship Components Introduction", WINDOW_WIDTH // 2 - 250, 50, 48, BLACK)
        
        if self.current_component_index < len(self.components):
            component = self.components[self.current_component_index]
            
            # Draw component in center
            component.position = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            component.draw(screen)
            
            # Draw component info
            self.draw_text(f"Component {self.current_component_index + 1}: {component.name}", 
                          50, 150, 36, BLACK)
            self.draw_text(f"Function: {component.description}", 
                          50, 200, 24, BLACK)
            
            # Draw progress
            progress = (self.current_component_index + 1) / len(self.components) * 100
            self.draw_text(f"Progress: {progress:.0f}%", 50, 250, 24, BLACK)
            
            # Instructions
            self.draw_text("Press SPACE to continue to next component", 50, WINDOW_HEIGHT - 100, 24, BLUE)
            self.draw_text("Press A to start assembly", 50, WINDOW_HEIGHT - 70, 24, GREEN)
        
    def draw_assembly_phase(self):
        screen.fill(WHITE)
        
        # Draw title
        self.draw_text("Spaceship Assembly in Progress...", WINDOW_WIDTH // 2 - 200, 50, 36, BLACK)
        
        # Update component positions - one at a time in assembly order
        if self.current_assembly_component < len(self.assembly_order):
            current_idx = self.assembly_order[self.current_assembly_component]
            current_comp = self.components[current_idx]
            
            # Move current component
            if current_comp.move_to_target(speed=3):
                current_comp.is_assembled = True
                self.current_assembly_component += 1
                
                # Add a delay effect by resetting position slightly
                if self.current_assembly_component < len(self.assembly_order):
                    next_idx = self.assembly_order[self.current_assembly_component]
                    next_comp = self.components[next_idx]
                    # Make the next component start from further away for dramatic effect
                    if next_comp.position[0] < WINDOW_WIDTH // 2:
                        next_comp.position = (50, next_comp.position[1])
                    else:
                        next_comp.position = (WINDOW_WIDTH - 50, next_comp.position[1])
        
        # Check if all assembled
        if self.current_assembly_component >= len(self.components):
            self.assembly_complete = True
        
        # Draw all components
        for i, component in enumerate(self.components):
            component.draw(screen)
            
            # Draw component status
            if component.is_assembled:
                self.draw_text("✓", int(component.position[0]) + 70, int(component.position[1]) - 10, 24, GREEN)
            elif self.current_assembly_component < len(self.assembly_order) and i == self.assembly_order[self.current_assembly_component]:
                # Highlight current component being assembled
                pygame.draw.circle(screen, ORANGE, (int(component.position[0]), int(component.position[1])), 
                                 max(component.size) + 10, 3)
        
        # Draw assembly progress
        assembled_count = sum(1 for c in self.components if c.is_assembled)
        progress = assembled_count / len(self.components) * 100
        self.draw_text(f"Assembly Progress: {progress:.0f}%", 50, 150, 32, BLACK)
        
        # Show current component being assembled
        if self.current_assembly_component < len(self.assembly_order):
            current_idx = self.assembly_order[self.current_assembly_component]
            current_name = self.components[current_idx].name
            self.draw_text(f"Installing: {current_name}", 50, 200, 28, ORANGE)
        
        # Draw component list with status in assembly order
        y_offset = 250
        self.draw_text("Assembly Sequence:", 50, y_offset - 30, 24, BLACK)
        for idx in self.assembly_order:
            comp = self.components[idx]
            is_current = self.current_assembly_component < len(self.assembly_order) and idx == self.assembly_order[self.current_assembly_component]
            color = GREEN if comp.is_assembled else (ORANGE if is_current else BLACK)
            status = "✓ Installed" if comp.is_assembled else ("→ Installing..." if is_current else "⋯ Waiting")
            self.draw_text(f"{status} {comp.name}", 50, y_offset, 20, color)
            y_offset += 30
        
        # Instructions
        if self.assembly_complete:
            self.draw_text("Assembly Complete! Press L to launch rocket", 50, WINDOW_HEIGHT - 70, 24, GREEN)
        else:
            self.draw_text("Components are assembling one by one...", 50, WINDOW_HEIGHT - 70, 24, BLUE)
    
    def draw_launch_phase(self):
        # Space background with moving stars
        screen.fill(SPACE_BLACK)
        
        # Draw moving stars
        for i, (x, y, brightness) in enumerate(self.stars):
            new_y = (y + 2) % WINDOW_HEIGHT
            self.stars[i] = (x, new_y, brightness)
            color = (brightness, brightness, brightness)
            pygame.draw.circle(screen, color, (x, new_y), 1)
        
        # Move spaceship up
        self.spaceship_y -= 3
        if self.spaceship_y < -200:
            self.spaceship_y = WINDOW_HEIGHT + 200
        
        # Draw assembled spaceship
        center_x = WINDOW_WIDTH // 2
        for component in self.components:
            component.position = (
                center_x + (component.target_position[0] - WINDOW_WIDTH // 2),
                self.spaceship_y + (component.target_position[1] - WINDOW_HEIGHT // 2)
            )
            component.draw(screen)
        
        # Draw launch effects
        flame_y = self.spaceship_y + 80
        for i in range(5):
            flame_points = [
                (center_x - 15 + i*7, flame_y),
                (center_x - 10 + i*7, flame_y + 30 + i*5),
                (center_x - 5 + i*7, flame_y)
            ]
            colors = [ORANGE, RED, YELLOW]
            pygame.draw.polygon(screen, colors[i % 3], flame_points)
        
        # Draw title and info
        self.draw_text("Flying to Space!", WINDOW_WIDTH // 2 - 120, 50, 36, WHITE)
        self.draw_text("Mission Success! Spaceship is heading to space", WINDOW_WIDTH // 2 - 250, 100, 24, WHITE)
        self.draw_text("Press R to restart", 50, WINDOW_HEIGHT - 50, 24, WHITE)
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.state == COMPONENT_INTRO:
                if event.key == pygame.K_SPACE:
                    self.current_component_index += 1
                    if self.current_component_index >= len(self.components):
                        self.current_component_index = 0
                elif event.key == pygame.K_a:
                    self.state = ASSEMBLY
                    
            elif self.state == ASSEMBLY:
                if event.key == pygame.K_l:
                    if self.assembly_complete:
                        self.state = LAUNCH
                        
            elif self.state == LAUNCH:
                if event.key == pygame.K_r:
                    self.__init__()  # Restart game
    
    def update(self):
        pass
    
    def draw(self):
        if self.state == COMPONENT_INTRO:
            self.draw_intro_phase()
        elif self.state == ASSEMBLY:
            self.draw_assembly_phase()
        elif self.state == LAUNCH:
            self.draw_launch_phase()

def main():
    game = SpaceshipGame()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event)
        
        game.update()
        game.draw()
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()