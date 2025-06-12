
# import pygame

# #Constant variables
# white = (255, 255, 255)
# black = (0, 0, 0)

# width = 600
# height = 600

# pygame.init()
# game_font = pygame.font.SysFont('Ubuntu', 40)

# delay = 30

# paddle_speed = 20

# paddle_width = 10
# paddle_height = 100

# p1_x_pos = 10
# p1_y_pos = height / 2 - paddle_height / 2

# p2_x_pos = width - paddle_width - 10
# p2_y_pos = height / 2 - paddle_height / 2

# p1_score = 0
# p2_score = 0

# p1_up = False
# p1_down = False
# p2_up = False
# p2_down = False

# ball_x_pos = width/2
# ball_y_pos = height/2
# ball_width = 8
# ball_x_vel = -10
# ball_y_vel = 0

# screen = pygame.display.set_mode((width, height))

# #drawing objects
# def draw_objects():
#     pygame.draw.rect(screen, white, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
#     pygame.draw.rect(screen, white, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
#     pygame.draw.circle(screen, white, (ball_x_pos, ball_y_pos), ball_width)
#     score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, white)
#     screen.blit(score, (width / 2, 30))

# def apply_player_movement():
#     global p1_y_pos
#     global p2_y_pos

#     if p1_up:
#         p1_y_pos = max(p1_y_pos - paddle_speed, 0)
#     elif p1_down:
#         p1_y_pos = min(p1_y_pos + paddle_speed, height)
#     if p2_up:
#         p2_y_pos = max(p2_y_pos - paddle_speed, 0)
#     elif p2_down:
#         p2_y_pos = min(p2_y_pos + paddle_speed, height)


# def apply_ball_movement():
#     global ball_x_pos
#     global ball_y_pos
#     global ball_x_vel
#     global ball_y_vel
#     global p1_score
#     global p2_score

#     if (ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (p1_y_pos < ball_y_pos + ball_y_vel + ball_width < p1_y_pos + paddle_height):
#         ball_x_vel = -ball_x_vel
#         ball_y_vel = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 15
#         ball_y_vel = -ball_y_vel
#     elif ball_x_pos + ball_x_vel < 0:
#         p2_score += 1
#         ball_x_pos = width / 2
#         ball_y_pos = height / 2
#         ball_x_vel = 10
#         ball_y_vel = 0
#     if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_vel + ball_width < p2_y_pos + paddle_height):
#         ball_x_vel = -ball_x_vel
#         ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 2
#         ball_y_vel = -ball_y_vel
#     elif ball_x_pos + ball_x_vel > height:
#         p1_score += 1
#         ball_x_pos = width / 2
#         ball_y_pos = height / 2
#         ball_x_vel = -10
#         ball_y_vel = 0
#     if ball_y_pos + ball_y_vel > height or ball_y_pos + ball_y_vel < 0:
#         ball_y_vel = -ball_y_vel

#     ball_x_pos += ball_x_vel
#     ball_y_pos += ball_y_vel

# pygame.display.set_caption("Ping Pong")
# screen.fill(black)
# pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
#             if event.key == pygame.K_w:
#                 p1_up = True
#             if event.key == pygame.K_s:
#                 p1_down = True
#             if event.key == pygame.K_UP:
#                 p2_up = True
#             if event.key == pygame.K_DOWN:
#                 p2_down = True
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_w:
#                 p1_up = False
#             if event.key == pygame.K_s:
#                 p1_down = False
#             if event.key == pygame.K_UP:
#                 p2_up = False
#             if event.key == pygame.K_DOWN:
#                 p2_down = False
#     screen.fill(black)
#     apply_player_movement()
#     apply_ball_movement()
#     draw_objects()
#     pygame.display.flip()
#     pygame.time.wait(delay)











import pygame
import random

# Initialize Pygame
pygame.init()

# Constant variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

WIDTH = 600
HEIGHT = 600
GAME_FONT = pygame.font.SysFont('Ubuntu', 40)

DELAY = 30
PADDLE_SPEED = 10
THRESHOLD = 10

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_WIDTH = 8

# Initial positions
p1_x_pos = 10
p1_y_pos = HEIGHT / 2 - PADDLE_HEIGHT / 2
p2_x_pos = WIDTH - PADDLE_WIDTH - 10
p2_y_pos = HEIGHT / 2 - PADDLE_HEIGHT / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = WIDTH / 2
ball_y_pos = HEIGHT / 2
ball_x_vel = -10
ball_y_vel = 0

# Difficulty settings (0 = Easy, 1 = Medium, 2 = Hard)
difficulty = 0  # Default to Easy
AI_SPEEDS = [5, 10, 15]  # Paddle speeds for Easy, Medium, Hard
AI_ACCURACY = [0.5, 0.3, 0.1]  # Prediction error margins, increased for easier gameplay
# Adjust AI_ACCURACY to make the AI less accurate if needed, e.g., [0.6, 0.4, 0.2]

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Ping Pong")

# Load sound effects (replace with your own file paths)
hit_sound = pygame.mixer.Sound('hit.wav')
bounce_sound = pygame.mixer.Sound('bounce.mp3')
score_sound = pygame.mixer.Sound('score.mp3')

# Drawing objects with enhanced visuals
def draw_objects():
    # Gradient background
    for y in range(HEIGHT):
        color = (0, y * 255 // HEIGHT, 50)  # Black to greenish tint
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))
    
    # Dashed center line
    for y in range(0, HEIGHT, 20):
        pygame.draw.line(screen, GRAY, (WIDTH // 2, y), (WIDTH // 2, y + 10), 2)
    
    # Paddles and ball
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos), int(p1_y_pos), PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (int(p2_x_pos), int(p2_y_pos), PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(screen, WHITE, (int(ball_x_pos), int(ball_y_pos)), BALL_WIDTH)
    
    # Score display
    score = GAME_FONT.render(f"{p1_score} - {p2_score}", False, WHITE)
    screen.blit(score, (WIDTH // 2 - score.get_width() // 2, 30))

# Player movement
def apply_player_movement():
    global p1_y_pos, p2_y_pos
    ai_speed = AI_SPEEDS[difficulty]
    
    if p1_up:
        p1_y_pos = max(p1_y_pos - PADDLE_SPEED, 0)
    elif p1_down:
        p1_y_pos = min(p1_y_pos + PADDLE_SPEED, HEIGHT - PADDLE_HEIGHT)
    if p2_up:
        p2_y_pos = max(p2_y_pos - ai_speed, 0)
    elif p2_down:
        p2_y_pos = min(p2_y_pos + ai_speed, HEIGHT - PADDLE_HEIGHT)

# Predict ball's future y-position for AI
def predict_ball_y():
    temp_x = ball_x_pos
    temp_y = ball_y_pos
    temp_x_vel = ball_x_vel
    temp_y_vel = ball_y_vel
    
    while temp_x < p2_x_pos:
        temp_x += temp_x_vel
        temp_y += temp_y_vel
        if temp_y > HEIGHT - BALL_WIDTH or temp_y < BALL_WIDTH:
            temp_y_vel = -temp_y_vel
            temp_y = max(BALL_WIDTH, min(HEIGHT - BALL_WIDTH, temp_y))
    # Add randomness based on difficulty
    error = random.uniform(-AI_ACCURACY[difficulty] * HEIGHT, AI_ACCURACY[difficulty] * HEIGHT)
    return temp_y + error

# Ball movement with sound effects
def apply_ball_movement():
    global ball_x_pos, ball_y_pos, ball_x_vel, ball_y_vel, p1_score, p2_score
    
    next_x = ball_x_pos + ball_x_vel
    next_y = ball_y_pos + ball_y_vel
    
    # Paddle collisions with improved detection
    if (next_x - BALL_WIDTH < p1_x_pos + PADDLE_WIDTH and 
        next_x + BALL_WIDTH > p1_x_pos and
        next_y - BALL_WIDTH < p1_y_pos + PADDLE_HEIGHT and 
        next_y + BALL_WIDTH > p1_y_pos):
        ball_x_vel = -ball_x_vel
        ball_y_vel = -(p1_y_pos + PADDLE_HEIGHT / 2 - next_y) / 15
        hit_sound.play()
    elif next_x < 0:
        p2_score += 1
        score_sound.play()
        reset_ball()
    
    if (next_x + BALL_WIDTH > p2_x_pos and 
        next_x - BALL_WIDTH < p2_x_pos + PADDLE_WIDTH and
        next_y - BALL_WIDTH < p2_y_pos + PADDLE_HEIGHT and 
        next_y + BALL_WIDTH > p2_y_pos):
        ball_x_vel = -ball_x_vel
        ball_y_vel = -(p2_y_pos + PADDLE_HEIGHT / 2 - next_y) / 15
        hit_sound.play()
    elif next_x > WIDTH:
        p1_score += 1
        score_sound.play()
        reset_ball()
    
    # Wall bounces
    if next_y > HEIGHT - BALL_WIDTH or next_y < BALL_WIDTH:
        ball_y_vel = -ball_y_vel
        bounce_sound.play()
    
    ball_x_pos += ball_x_vel
    ball_y_pos += ball_y_vel

# Reset ball to center
def reset_ball():
    global ball_x_pos, ball_y_pos, ball_x_vel, ball_y_vel
    ball_x_pos = WIDTH / 2
    ball_y_pos = HEIGHT / 2
    ball_x_vel = random.choice([-10, 10])  # Random direction
    ball_y_vel = random.uniform(-5, 5)     # Random vertical velocity

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1_up = True
            elif event.key == pygame.K_s:
                p1_down = True
            elif event.key == pygame.K_1:
                difficulty = 0  # Easy
            elif event.key == pygame.K_2:
                difficulty = 1  # Medium
            elif event.key == pygame.K_3:
                difficulty = 2  # Hard
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_up = False
            elif event.key == pygame.K_s:
                p1_down = False
    
    # AI logic with trajectory prediction
    if ball_x_vel > 0:  # Ball moving toward AI
        target_y = predict_ball_y()
        current_center = p2_y_pos + PADDLE_HEIGHT / 2
        if target_y < current_center - THRESHOLD:
            p2_up = True
            p2_down = False
        elif target_y > current_center + THRESHOLD:
            p2_up = False
            p2_down = True
        else:
            p2_up = p2_down = False
    else:  # Ball moving away, return to center
        center_y = HEIGHT / 2
        current_center = p2_y_pos + PADDLE_HEIGHT / 2
        if current_center < center_y - THRESHOLD:
            p2_up = False
            p2_down = True
        elif current_center > center_y + THRESHOLD:
            p2_up = True
            p2_down = False
        else:
            p2_up = p2_down = False
    
    apply_player_movement()
    apply_ball_movement()
    draw_objects()
    pygame.display.flip()
    pygame.time.wait(DELAY)

pygame.quit()