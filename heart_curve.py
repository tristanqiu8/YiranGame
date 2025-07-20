import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Window settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mathematical Heart Curve with Turtle")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)

# Clock
clock = pygame.time.Clock()

class Turtle:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.angle = 0
        self.size = 15
        self.trail = []  # Store trail points
        self.color = GREEN
        
    def move_to(self, x, y):
        # Calculate angle for turtle orientation
        if len(self.trail) > 0:
            dx = x - self.x
            dy = y - self.y
            self.angle = math.atan2(dy, dx)
        
        self.x = x
        self.y = y
        self.trail.append((x, y))
        
        # Limit trail length for performance
        if len(self.trail) > 1000:
            self.trail.pop(0)
    
    def draw(self, screen):
        # Draw trail
        if len(self.trail) > 1:
            for i in range(1, len(self.trail)):
                # Gradient effect for trail
                alpha = i / len(self.trail)
                color = (
                    int(RED[0] * alpha + PINK[0] * (1 - alpha)),
                    int(RED[1] * alpha + PINK[1] * (1 - alpha)),
                    int(RED[2] * alpha + PINK[2] * (1 - alpha))
                )
                pygame.draw.line(screen, color, self.trail[i-1], self.trail[i], 3)
        
        # Draw turtle body
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        
        # Draw turtle head (shows direction)
        head_x = self.x + self.size * 0.8 * math.cos(self.angle)
        head_y = self.y + self.size * 0.8 * math.sin(self.angle)
        pygame.draw.circle(screen, BLACK, (int(head_x), int(head_y)), 5)

def heart_curve(t, scale=5):
    """
    Heart curve parametric equations
    t: parameter from 0 to 2*pi
    scale: size multiplier
    """
    x = 16 * (math.sin(t) ** 3)
    y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
    
    # Scale and center
    x = x * scale + WINDOW_WIDTH // 2
    y = y * scale + WINDOW_HEIGHT // 2 - 100  # Offset up a bit
    
    return x, y

def draw_text(screen, text, x, y, size=24, color=BLACK):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    turtle = Turtle()
    t = 0  # Parameter for curve
    speed = 0.02  # How fast to draw
    scale = 10  # Size of heart
    paused = False
    show_equation = True
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    # Reset
                    turtle.trail.clear()
                    t = 0
                elif event.key == pygame.K_UP:
                    scale = min(scale + 1, 20)
                elif event.key == pygame.K_DOWN:
                    scale = max(scale - 1, 3)
                elif event.key == pygame.K_e:
                    show_equation = not show_equation
        
        # Update
        if not paused and t <= 2 * math.pi:
            x, y = heart_curve(t, scale)
            turtle.move_to(x, y)
            t += speed
        
        # Draw
        screen.fill(WHITE)
        
        # Draw turtle and trail
        turtle.draw(screen)
        
        # Draw instructions
        draw_text(screen, "Heart Curve Animation", 10, 10, 36, BLACK)
        draw_text(screen, "Controls:", 10, 60, 24, BLACK)
        draw_text(screen, "SPACE - Pause/Resume", 10, 90, 20, BLACK)
        draw_text(screen, "R - Reset", 10, 115, 20, BLACK)
        draw_text(screen, "UP/DOWN - Change size", 10, 140, 20, BLACK)
        draw_text(screen, "E - Toggle equation", 10, 165, 20, BLACK)
        
        # Draw progress
        progress = min(t / (2 * math.pi), 1.0) * 100
        draw_text(screen, f"Progress: {progress:.1f}%", 10, 200, 24, BLACK)
        draw_text(screen, f"Scale: {scale}", 10, 230, 24, BLACK)
        
        # Show equation if enabled
        if show_equation:
            draw_text(screen, "Parametric Equations:", WINDOW_WIDTH - 400, 10, 24, BLACK)
            draw_text(screen, "x = 16 * sin^3(t)", WINDOW_WIDTH - 400, 40, 20, RED)
            draw_text(screen, "y = 13*cos(t) - 5*cos(2t) - 2*cos(3t) - cos(4t)", WINDOW_WIDTH - 400, 65, 20, RED)
            draw_text(screen, "t in [0, 2*pi]", WINDOW_WIDTH - 400, 90, 20, RED)
        
        # Show status
        if paused:
            draw_text(screen, "PAUSED", WINDOW_WIDTH // 2 - 50, 50, 36, RED)
        elif t > 2 * math.pi:
            draw_text(screen, "COMPLETE! Press R to restart", WINDOW_WIDTH // 2 - 150, 50, 36, GREEN)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()