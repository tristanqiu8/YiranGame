import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Window settings
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Mathematical Curves Explorer")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Clock
clock = pygame.time.Clock()

class CurveExplorer:
    def __init__(self):
        self.curves = {
            '1': {
                'name': 'Heart',
                'func': self.heart_curve,
                'range': (0, 2 * math.pi),
                'scale': 10,
                'color': RED
            },
            '2': {
                'name': 'Rose (4 petals)',
                'func': self.rose_curve,
                'range': (0, 2 * math.pi),
                'scale': 150,
                'color': PURPLE
            },
            '3': {
                'name': 'Lissajous',
                'func': self.lissajous_curve,
                'range': (0, 2 * math.pi),
                'scale': 200,
                'color': BLUE
            },
            '4': {
                'name': 'Spiral',
                'func': self.spiral_curve,
                'range': (0, 8 * math.pi),
                'scale': 5,
                'color': GREEN
            },
            '5': {
                'name': 'Infinity',
                'func': self.infinity_curve,
                'range': (0, 2 * math.pi),
                'scale': 200,
                'color': ORANGE
            }
        }
        
        self.current_curve = '1'
        self.trail = []
        self.t = 0
        self.speed = 0.02
        self.turtle_x = WINDOW_WIDTH // 2
        self.turtle_y = WINDOW_HEIGHT // 2
        
    def heart_curve(self, t, scale):
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        return x * scale, y * scale
    
    def rose_curve(self, t, scale):
        # Rose curve with k=4 (4 petals)
        r = math.cos(4 * t)
        x = r * math.cos(t)
        y = r * math.sin(t)
        return x * scale, y * scale
    
    def lissajous_curve(self, t, scale):
        # Lissajous curve A=3, B=2
        x = math.sin(3 * t)
        y = math.sin(2 * t)
        return x * scale, y * scale
    
    def spiral_curve(self, t, scale):
        # Archimedean spiral
        r = t
        x = r * math.cos(t)
        y = r * math.sin(t)
        return x * scale, y * scale
    
    def infinity_curve(self, t, scale):
        # Figure-eight / Lemniscate approximation
        x = math.cos(t)
        y = math.sin(2 * t) / 2
        return x * scale, y * scale
    
    def update(self, paused):
        if not paused:
            curve = self.curves[self.current_curve]
            if self.t <= curve['range'][1]:
                x, y = curve['func'](self.t, curve['scale'])
                self.turtle_x = x + WINDOW_WIDTH // 2
                self.turtle_y = y + WINDOW_HEIGHT // 2
                self.trail.append((self.turtle_x, self.turtle_y))
                self.t += self.speed
                
                # Limit trail length
                if len(self.trail) > 2000:
                    self.trail.pop(0)
    
    def reset(self):
        self.trail.clear()
        self.t = 0
    
    def draw(self, screen):
        # Draw trail
        if len(self.trail) > 1:
            curve_color = self.curves[self.current_curve]['color']
            for i in range(1, len(self.trail)):
                alpha = i / len(self.trail)
                color = tuple(int(c * alpha) for c in curve_color)
                pygame.draw.line(screen, color, self.trail[i-1], self.trail[i], 2)
        
        # Draw turtle
        pygame.draw.circle(screen, GREEN, (int(self.turtle_x), int(self.turtle_y)), 10)
        pygame.draw.circle(screen, BLACK, (int(self.turtle_x), int(self.turtle_y)), 10, 2)

def draw_text(screen, text, x, y, size=24, color=BLACK):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    explorer = CurveExplorer()
    paused = False
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    explorer.reset()
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                    # Switch curves
                    new_curve = chr(event.key)
                    if new_curve in explorer.curves:
                        explorer.current_curve = new_curve
                        explorer.reset()
        
        # Update
        explorer.update(paused)
        
        # Draw
        screen.fill(WHITE)
        explorer.draw(screen)
        
        # UI
        current = explorer.curves[explorer.current_curve]
        draw_text(screen, f"Current: {current['name']}", 10, 10, 36, BLACK)
        
        draw_text(screen, "Select Curve:", 10, 60, 24, BLACK)
        y_offset = 90
        for key, curve in explorer.curves.items():
            color = BLACK if key != explorer.current_curve else curve['color']
            draw_text(screen, f"{key} - {curve['name']}", 10, y_offset, 20, color)
            y_offset += 25
        
        draw_text(screen, "Controls:", 10, 250, 24, BLACK)
        draw_text(screen, "1-5 - Select curve", 10, 280, 20, BLACK)
        draw_text(screen, "SPACE - Pause/Resume", 10, 305, 20, BLACK)
        draw_text(screen, "R - Reset", 10, 330, 20, BLACK)
        
        # Progress
        curve_range = current['range']
        progress = min((explorer.t - curve_range[0]) / (curve_range[1] - curve_range[0]), 1.0) * 100
        draw_text(screen, f"Progress: {progress:.1f}%", 10, 370, 24, BLACK)
        
        if paused:
            draw_text(screen, "PAUSED", WINDOW_WIDTH // 2 - 50, 50, 36, RED)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()