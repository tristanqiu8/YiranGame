import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 设置游戏窗口
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Duck Collection Game")

# 颜色定义
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 100, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 游戏时钟
clock = pygame.time.Clock()

# 音效系统
sounds_enabled = True
try:
    pygame.mixer.init()
    # 预留音效加载位置
    collect_sound = None
    background_music = None
    
    # 尝试加载音效文件
    try:
        # collect_sound = pygame.mixer.Sound("sounds/collect.wav")
        # collect_sound.set_volume(0.5)
        pass
    except:
        print("Warning: Could not load collect sound")
    
    # 尝试加载背景音乐
    try:
        # pygame.mixer.music.load("sounds/background.mp3")
        # pygame.mixer.music.set_volume(0.3)
        # pygame.mixer.music.play(-1)  # -1 表示循环播放
        pass
    except:
        print("Warning: Could not load background music")
except:
    sounds_enabled = False
    print("Warning: Sound system could not be initialized")

class Duck:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.base_size = 45  # 基础鸭子尺寸
        self.size = 45  # 当前鸭子尺寸
        self.speed = 5
        self.has_straw = False  # 是否有吸管
    
    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.size:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WINDOW_WIDTH - self.size:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > self.size:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < WINDOW_HEIGHT - self.size:
            self.y += self.speed
    
    def draw(self, screen):
        # 画小鸭子身体
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.size)
        # 画小鸭子嘴巴
        beak_x = int(self.x + self.size * 0.67)
        beak_y = int(self.y - self.size * 0.18)
        beak_size = int(self.size * 0.27)
        pygame.draw.circle(screen, ORANGE, (beak_x, beak_y), beak_size)
        # 画小鸭子眼睛
        eye_offset_x = int(self.size * 0.33)
        eye_offset_y1 = int(self.size * 0.33)
        eye_offset_y2 = int(self.size * 0.18)
        eye_size = int(self.size * 0.11)
        pygame.draw.circle(screen, BLACK, (self.x + eye_offset_x, self.y - eye_offset_y1), eye_size)
        pygame.draw.circle(screen, BLACK, (self.x + eye_offset_x, self.y + eye_offset_y2), eye_size)
        
        # 画吸管（如果有）
        if self.has_straw:
            straw_length = 80
            straw_width = 8
            # 吸管起点（嘴巴位置）
            straw_start_x = beak_x + beak_size
            straw_start_y = beak_y
            # 吸管终点
            straw_end_x = straw_start_x + straw_length
            straw_end_y = straw_start_y
            # 画吸管
            pygame.draw.line(screen, (150, 75, 0), (straw_start_x, straw_start_y), 
                            (straw_end_x, straw_end_y), straw_width)
            # 画吸管末端
            pygame.draw.circle(screen, (150, 75, 0), (straw_end_x, straw_end_y), straw_width // 2)

class Food:
    def __init__(self):
        self.x = random.randint(40, WINDOW_WIDTH - 40)
        self.y = random.randint(40, WINDOW_HEIGHT - 40)
        self.size = 20  # 增大豆子大小
        self.score = random.randint(1, 10)  # 随机分数1-10
        # 速度根据分数设定：分数越高速度越快
        base_speed = 1 + (self.score - 1) * 0.3  # 速度范围: 1.0 到 3.7
        self.vx = random.choice([-1, 1]) * base_speed
        self.vy = random.choice([-1, 1]) * base_speed
    
    def update(self):
        # 更新位置
        self.x += self.vx
        self.y += self.vy
        
        # 碰到边界反弹
        if self.x <= self.size or self.x >= WINDOW_WIDTH - self.size:
            self.vx = -self.vx
        if self.y <= self.size or self.y >= WINDOW_HEIGHT - self.size:
            self.vy = -self.vy
        
        # 确保不越界
        self.x = max(self.size, min(WINDOW_WIDTH - self.size, self.x))
        self.y = max(self.size, min(WINDOW_HEIGHT - self.size, self.y))
    
    def draw(self, screen):
        # 画食物（红色圆点）
        pygame.draw.circle(screen, RED, (self.x, self.y), self.size)
        # 显示分数
        font = pygame.font.Font(None, 28)  # 增大字体
        text = font.render(str(self.score), True, WHITE)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)

def check_collision(duck, food):
    # 检查鸭子身体碰撞
    distance = ((duck.x - food.x) ** 2 + (duck.y - food.y) ** 2) ** 0.5
    if distance < duck.size + food.size:
        return True
    
    # 如果有吸管，检查吸管碰撞
    if duck.has_straw:
        # 吸管参数
        beak_x = int(duck.x + duck.size * 0.67)
        beak_y = int(duck.y - duck.size * 0.18)
        beak_size = int(duck.size * 0.27)
        straw_start_x = beak_x + beak_size
        straw_end_x = straw_start_x + 80
        
        # 检查食物是否在吸管范围内
        if (straw_start_x <= food.x <= straw_end_x and 
            abs(food.y - beak_y) < food.size + 8):
            return True
    
    return False

def draw_text(screen, text, x, y, size=36, color=BLACK):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    # 创建游戏对象
    duck = Duck()
    foods = []
    score = 0
    last_milestone = 0  # 上一个里程碑分数
    milestone_message = ""  # 里程碑消息
    milestone_timer = 0  # 消息显示计时器
    
    # 创建初始食物
    for _ in range(5):
        foods.append(Food())
    
    # 游戏主循环
    running = True
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 获取按键状态
        keys = pygame.key.get_pressed()
        
        # 更新游戏对象
        duck.move(keys)
        
        # 更新食物位置
        for food in foods:
            food.update()
        
        # 检查碰撞
        for food in foods[:]:  # 使用切片复制列表来安全地删除元素
            if check_collision(duck, food):
                foods.remove(food)
                score += food.score  # 使用食物的分数
                
                # 检查里程碑
                if score >= 100 and score // 100 > last_milestone:
                    last_milestone = score // 100
                    # 增大鸭子尺寸10%
                    duck.size = int(duck.base_size * (1 + 0.1 * last_milestone))
                    milestone_message = f"Milestone! {last_milestone * 100} points! Duck grows bigger!"
                    milestone_timer = 180  # 显示3秒（60帧/秒）
                
                # 500分时获得吸管
                if score >= 500 and not duck.has_straw:
                    duck.has_straw = True
                    milestone_message = "500 points! You got a long straw!"
                    milestone_timer = 180
                
                # 播放收集音效
                if sounds_enabled and collect_sound:
                    collect_sound.play()
                # 添加新食物
                foods.append(Food())
        
        # 绘制游戏画面
        screen.fill(BLUE)  # 天空蓝色背景
        
        # 画云朵装饰
        pygame.draw.circle(screen, WHITE, (100, 100), 30)
        pygame.draw.circle(screen, WHITE, (120, 100), 25)
        pygame.draw.circle(screen, WHITE, (140, 100), 30)
        
        pygame.draw.circle(screen, WHITE, (600, 150), 25)
        pygame.draw.circle(screen, WHITE, (620, 150), 30)
        pygame.draw.circle(screen, WHITE, (640, 150), 25)
        
        # 画太阳
        pygame.draw.circle(screen, YELLOW, (700, 80), 40)
        
        # 画池塘边界
        pygame.draw.rect(screen, GREEN, (50, WINDOW_HEIGHT - 150, WINDOW_WIDTH-100, 100))
        
        # 绘制游戏对象
        duck.draw(screen)
        for food in foods:
            food.draw(screen)
        
        # 绘制分数
        draw_text(screen, f"Score: {score}", 10, 10, 48, WHITE)
        
        # 绘制里程碑消息
        if milestone_timer > 0:
            # 创建闪烁效果
            if milestone_timer % 20 < 15:  # 闪烁
                draw_text(screen, milestone_message, WINDOW_WIDTH // 2 - 200, 
                         WINDOW_HEIGHT // 2 - 100, 48, YELLOW)
            milestone_timer -= 1
        
        # 绘制说明
        draw_text(screen, "Use arrow keys to move the duck and collect red food!", 10, WINDOW_HEIGHT - 40, 24, WHITE)
        
        # 更新显示
        pygame.display.flip()
        clock.tick(60)  # 60帧每秒
    
    # 退出游戏
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()