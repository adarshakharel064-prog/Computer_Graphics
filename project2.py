import pygame
import sys
import math
import random

pygame.init()


WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Realistic Basketball Hooping Game")
clock = pygame.time.Clock()


WHITE = (245, 245, 245)
ORANGE = (240, 130, 40)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

SKY_TOP = (135, 206, 250)
SKY_BOTTOM = (200, 230, 255)
SUN_COLOR = (255, 220, 120)

GROUND_LIGHT = (222, 184, 135)
GROUND_DARK = (205, 170, 125)

POLE_COLOR = (120, 120, 120)


gravity = 0.5
air_resistance = 0.995
bounce_loss = 0.75

#  TIMER 
game_duration = 60
start_ticks = pygame.time.get_ticks()

#  BALL 
ball_radius = 18
ball_x = 150
ball_y = HEIGHT - 120
ball_vx = 0
ball_vy = 0
thrown = False

dragging = False
drag_start = (0, 0)

# HOOP 
rim_x = 650
rim_y = 260
rim_width = 70
rim_height = 8

# BACKBOARD 
board_x = rim_x + rim_width - 5
board_y = rim_y - 70
board_width = 12
board_height = 140

#  POLE ko data 
pole_width = 18
pole_x = board_x + board_width//2 - pole_width//2
pole_y = rim_y + rim_height
pole_height = HEIGHT - pole_y

#  CLOUDS banaiyo
clouds = []
for i in range(5):
    clouds.append([random.randint(0, WIDTH), random.randint(40, 200), random.uniform(0.2, 0.6)])

# GAME STATE 
score = 0
game_over = False
shake_timer = 0
shake_intensity = 8

shots_taken = 0
shots_made = 0
end_time = 0

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 60)

#  FUNCTIONS 
def reset_ball():
    global ball_x, ball_y, ball_vx, ball_vy, thrown
    ball_x = 150
    ball_y = HEIGHT - 120
    ball_vx = 0
    ball_vy = 0
    thrown = False

def restart_game():
    global score, game_over, start_ticks, shots_taken, shots_made, end_time
    score = 0
    shots_taken = 0
    shots_made = 0
    end_time = 0
    game_over = False
    start_ticks = pygame.time.get_ticks()
    reset_ball()

def check_ball_reset():
    if ball_x < -50 or ball_x > WIDTH + 50:
        reset_ball()
    if ball_y > HEIGHT + 50:
        reset_ball()
    if abs(ball_vx) < 0.2 and abs(ball_vy) < 0.2 and ball_y >= HEIGHT - ball_radius - 1:
        reset_ball()

def draw_sky(surface):
    for i in range(HEIGHT):
        ratio = i / HEIGHT
        r = SKY_TOP[0] * (1 - ratio) + SKY_BOTTOM[0] * ratio
        g = SKY_TOP[1] * (1 - ratio) + SKY_BOTTOM[1] * ratio
        b = SKY_TOP[2] * (1 - ratio) + SKY_BOTTOM[2] * ratio
        pygame.draw.line(surface, (int(r), int(g), int(b)), (0, i), (WIDTH, i))

def draw_sun(surface):
    pygame.draw.circle(surface, SUN_COLOR, (120, 100), 50)
    pygame.draw.circle(surface, (255, 240, 170), (120, 100), 40)

def draw_cloud(surface, x, y):
    pygame.draw.circle(surface, WHITE, (int(x), int(y)), 25)
    pygame.draw.circle(surface, WHITE, (int(x+25), int(y+10)), 30)
    pygame.draw.circle(surface, WHITE, (int(x-25), int(y+10)), 30)
    pygame.draw.circle(surface, WHITE, (int(x+5), int(y-10)), 28)

def draw_ground(surface):
    pygame.draw.rect(surface, GROUND_LIGHT, (0, HEIGHT - 90, WIDTH, 90))
    for i in range(0, WIDTH, 40):
        pygame.draw.line(surface, GROUND_DARK, (i, HEIGHT - 90), (i, HEIGHT), 2)

def draw_shadow(surface, x, y, radius):
    ground_y = HEIGHT - 90
    distance = min(abs(ground_y - y), 300)
    scale = max(0.3, 1 - distance / 400)      #kati le change vayo ta
    w = int(radius * 2 * scale)
    h = int(radius * 0.8 * scale)
    shadow = pygame.Surface((w, h), pygame.SRCALPHA)     #allows transparancy
    pygame.draw.ellipse(shadow, (0, 0, 0, 80), (0, 0, w, h))
    surface.blit(shadow, (x - w // 2, ground_y - h // 2))

def draw_ball(surface, x, y, r):
    pygame.draw.circle(surface, ORANGE, (int(x), int(y)), r)
    pygame.draw.circle(surface, BLACK, (int(x), int(y)), r, 2)

def draw_trajectory(surface):
    if not dragging:
        return
    mx, my = pygame.mouse.get_pos()
    preview_vx = (drag_start[0] - mx) * 0.18
    preview_vy = (drag_start[1] - my) * 0.18
    temp_x = ball_x
    temp_y = ball_y
    temp_vx = preview_vx
    temp_vy = preview_vy
    for i in range(30):
        temp_vy += gravity
        temp_vx *= air_resistance
        temp_x += temp_vx
        temp_y += temp_vy
        pygame.draw.circle(surface, (100, 100, 100), (int(temp_x), int(temp_y)), 4)

# MAIN LOOP 
running = True
while running:
    clock.tick(60)
    offset_x = offset_y = 0
    if shake_timer > 0:
        offset_x = random.randint(-shake_intensity, shake_intensity)
        offset_y = random.randint(-shake_intensity, shake_intensity)
        shake_timer -= 1

    temp = pygame.Surface((WIDTH, HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = event.pos
            if math.hypot(mx - ball_x, my - ball_y) <= ball_radius:
                dragging = True
                drag_start = event.pos

        if event.type == pygame.MOUSEBUTTONUP and dragging:  #shows projectile motion off basketball after release
            mx, my = event.pos
            ball_vx = (drag_start[0] - mx) * 0.18
            ball_vy = (drag_start[1] - my) * 0.18
            thrown = True
            dragging = False
            shots_taken += -1

    seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
    time_left = max(0, game_duration - int(seconds_passed))

    if score >= 15 and not game_over:
        game_over = True
        end_time = seconds_passed

    if time_left <= 0 and not game_over:
        game_over = True
        end_time = seconds_passed

    if thrown and not game_over:
        ball_vy += gravity
        ball_vx *= air_resistance
        ball_x += ball_vx
        ball_y += ball_vy

    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_vy = -ball_vy * bounce_loss
        ball_vx *= 0.9

    # BOARD MA COLLISION
    if (board_x < ball_x + ball_radius < board_x + board_width and
        board_y < ball_y < board_y + board_height):
        ball_x = board_x - ball_radius
        ball_vx = -ball_vx * bounce_loss
        shake_timer = 5

    # POLE MA COLLISION
    if (pole_x < ball_x + ball_radius < pole_x + pole_width and
        pole_y < ball_y < pole_y + pole_height):
        ball_x = pole_x - ball_radius
        ball_vx = -ball_vx * bounce_loss

    # SCORING
    if (rim_x + 10 < ball_x < rim_x + rim_width - 10 and
        rim_y < ball_y < rim_y + 45):
        score += 3
        shots_made += 1
        reset_ball()

    if not game_over:
        check_ball_reset()

    # DRAWING
    draw_sky(temp)
    draw_sun(temp)

    for cloud in clouds:
        cloud[0] += cloud[2]  #CLOUD[2] chai speed ho hai
        if cloud[0] > WIDTH + 50:  #reset cloud to left after reaching right corner
            cloud[0] = -50
        draw_cloud(temp, cloud[0], cloud[1])

    draw_ground(temp)

    # DRAW of POLE
    pygame.draw.rect(temp, POLE_COLOR, (pole_x, pole_y, pole_width, pole_height))
    pygame.draw.rect(temp, GRAY, (board_x, board_y, board_width, board_height))
    pygame.draw.rect(temp, RED, (rim_x, rim_y, rim_width, rim_height))

    draw_shadow(temp, ball_x, ball_y, ball_radius)
    draw_trajectory(temp)
    draw_ball(temp, ball_x, ball_y, ball_radius)

    temp.blit(font.render(f"Score: {score}", True, BLACK), (20, 20))
    temp.blit(font.render(f"Time: {time_left}s", True, BLACK), (20, 55))

    if game_over:
        accuracy = (shots_made / shots_taken * 100) if shots_taken > 0 else 0
        stats = [
            f"FINAL SCORE: {score}",
            f"TOTAL TIME: {round(end_time,1)}s",
            f"SHOTS TAKEN: {shots_taken}",
            f"SHOTS MADE: {shots_made}",
            f"ACCURACY: {round(accuracy,1)}%"
        ]
        for i, line in enumerate(stats):
            text = big_font.render(line, True, RED)
            temp.blit(text, (WIDTH//2 - text.get_width()//2, 150 + i*60))
        restart_text = font.render("Press R to Restart", True, RED)
        temp.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, 150 + len(stats)*60))

    screen.blit(temp, (offset_x, offset_y))
    pygame.display.update()

pygame.quit()
sys.exit()










# import pygame
# import math
# import random
# import sys

# pygame.init()

# WIDTH, HEIGHT = 1000, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("City Day & Night Cycle")

# clock = pygame.time.Clock()
# time_passed = 0

# # Generate buildings
# buildings = []
# for i in range(8):
#     width = random.randint(80, 130)
#     height = random.randint(200, 350)
#     x = i * 130 + 20
#     y = HEIGHT - height - 150
#     buildings.append((x, y, width, height))

# # Generate stars
# stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT//2)) for _ in range(100)]

# def draw_gradient(color1, color2):
#     for y in range(HEIGHT):
#         ratio = y / HEIGHT
#         r = color1[0] * (1 - ratio) + color2[0] * ratio
#         g = color1[1] * (1 - ratio) + color2[1] * ratio
#         b = color1[2] * (1 - ratio) + color2[2] * ratio
#         pygame.draw.line(screen, (int(r), int(g), int(b)), (0, y), (WIDTH, y))

# running = True
# while running:
#     clock.tick(60)
#     time_passed += 0.002

#     cycle = (math.sin(time_passed) + 1) / 2  # 0 to 1

#     # Sky colors
#     day_top = (135, 206, 250)
#     day_bottom = (255, 180, 120)
#     night_top = (10, 10, 40)
#     night_bottom = (40, 40, 80)

#     sky_top = [day_top[i] * cycle + night_top[i] * (1 - cycle) for i in range(3)]
#     sky_bottom = [day_bottom[i] * cycle + night_bottom[i] * (1 - cycle) for i in range(3)]

#     draw_gradient(sky_top, sky_bottom)

#     # Stars at night
#     if cycle < 0.4:
#         for star in stars:
#             pygame.draw.circle(screen, (255, 255, 255), star, 2)

#     # Sun / Moon path
#     angle = time_passed
#     celestial_x = WIDTH // 2 + math.cos(angle) * 350
#     celestial_y = 250 - math.sin(angle) * 200

#     if cycle > 0.5:
#         pygame.draw.circle(screen, (255, 223, 0), (int(celestial_x), int(celestial_y)), 45)
#     else:
#         pygame.draw.circle(screen, (230, 230, 255), (int(celestial_x), int(celestial_y)), 35)

#     # Draw buildings
#     for b in buildings:
#         building_color = (40 * cycle + 20, 40 * cycle + 20, 60 * cycle + 40)
#         pygame.draw.rect(screen, building_color, b)

#         # Windows
#         for i in range(3):
#             for j in range(6):
#                 wx = b[0] + 15 + i * 30
#                 wy = b[1] + 20 + j * 40
#                 if cycle < 0.4:
#                     pygame.draw.rect(screen, (255, 255, 120), (wx, wy, 15, 20))
#                 else:
#                     pygame.draw.rect(screen, (180, 220, 255), (wx, wy, 15, 20))

#     # Road
#     pygame.draw.rect(screen, (60, 60, 60), (0, HEIGHT - 120, WIDTH, 120))
#     pygame.draw.line(screen, (255, 255, 0), (0, HEIGHT - 60), (WIDTH, HEIGHT - 60), 4)

#     # Street lights
#     for i in range(5):
#         x = 150 + i * 170
#         pygame.draw.rect(screen, (80, 80, 80), (x, HEIGHT - 200, 10, 80))
#         if cycle < 0.4:
#             pygame.draw.circle(screen, (255, 255, 180), (x + 5, HEIGHT - 200), 15)

#     # Parked car
#     pygame.draw.rect(screen, (200, 0, 0), (700, HEIGHT - 160, 140, 40))
#     pygame.draw.circle(screen, (0, 0, 0), (730, HEIGHT - 120), 20)
#     pygame.draw.circle(screen, (0, 0, 0), (800, HEIGHT - 120), 20)

#     # Headlights at night
#     if cycle < 0.4:
#         pygame.draw.circle(screen, (255, 255, 180), (840, HEIGHT - 145), 12)

#     pygame.display.flip()

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()



