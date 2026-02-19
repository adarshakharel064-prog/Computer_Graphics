import pygame
import random
import sys

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Improved Physics")

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
SKY = (135, 206, 235)

# Bird
bird_width, bird_height = 34, 24
bird_x = 50
bird_y = SCREEN_HEIGHT // 2
bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

gravity = 0.4          # smoother gravity
jump_strength = -6.5   # reduced jump height
bird_movement = 0

# Pipes
pipe_list = []
pipe_speed = 3
pipe_gap = 160   # slightly bigger gap for smoother gameplay
pipe_width = 70

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1500)

# Ground
ground_height = 100
ground_scroll = 0

# Background scroll
background_scroll = 0
background_speed = 1

# Score
score = 0
high_score = 0
font = pygame.font.SysFont(None, 40)

# Particle effects
particles = []

# Game states
game_active = True
game_paused = False

# Sounds
try:
    jump_sound = pygame.mixer.Sound("jump.wav")
    hit_sound = pygame.mixer.Sound("hit.wav")
except:
    jump_sound = None
    hit_sound = None

# Load Images
try:
    background_img = pygame.image.load("background.png").convert()
    background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
except:
    background_img = None

bird_img = pygame.image.load("bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img, (bird_width, bird_height))

pipe_img = pygame.image.load("pipe.png").convert_alpha()

ground_img = pygame.image.load("ground.png").convert_alpha()
ground_img = pygame.transform.scale(ground_img, (SCREEN_WIDTH, ground_height))


# FUNCTIONS
def draw_bird():
    screen.blit(bird_img, bird_rect)

def draw_pipes(pipes):
    for pipe in pipes:
        pipe_height = abs(pipe['rect'].height)
        pipe_surface = pygame.transform.scale(pipe_img, (pipe_width, pipe_height))
        if pipe['top']:
            pipe_surface = pygame.transform.flip(pipe_surface, False, True)
        screen.blit(pipe_surface, (pipe['rect'].x, pipe['rect'].y))

def move_pipes(pipes):
    for pipe in pipes:
        pipe['rect'].x -= pipe_speed
    return [pipe for pipe in pipes if pipe['rect'].x + pipe_width > 0]

def check_collision(pipes):
    global game_active
    for pipe in pipes:
        if bird_rect.colliderect(pipe['rect']):
            if hit_sound: hit_sound.play()
            create_particles(bird_rect.center)
            return False

    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT - ground_height:
        if hit_sound: hit_sound.play()
        create_particles(bird_rect.center)
        return False

    return True

def display_score(score_val):
    score_surface = font.render(f"Score: {int(score_val)}", True, WHITE)
    screen.blit(score_surface, (10, 10))

def create_particles(position):
    for _ in range(15):
        particles.append([
            list(position),
            [random.randint(0,255),random.randint(0,255),random.randint(0,255)],
            random.randint(2,5),
            random.randint(20,40)
        ])

def reset_game():
    global pipe_list, bird_movement, score, particles, game_active
    pipe_list.clear()
    bird_rect.centery = SCREEN_HEIGHT // 2
    bird_movement = 0
    score = 0
    particles.clear()
    game_active = True


# GAME LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            # Jump
            if event.key == pygame.K_SPACE and game_active and not game_paused:
                bird_movement = jump_strength
                if jump_sound: jump_sound.play()

            # Pause
            if event.key == pygame.K_p:
                game_paused = not game_paused

            # Restart
            if event.key == pygame.K_r:
                reset_game()

            # Restart after game over
            if event.key == pygame.K_SPACE and not game_active:
                reset_game()

        # Spawn Pipes
        if event.type == SPAWNPIPE and game_active and not game_paused:
            pipe_height = random.randint(150, 450)
            top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
            bottom_pipe = pygame.Rect(
                SCREEN_WIDTH,
                pipe_height + pipe_gap,
                pipe_width,
                SCREEN_HEIGHT - pipe_height - pipe_gap - ground_height
            )

            pipe_list.append({'rect': top_pipe, 'top': True, 'passed': False})
            pipe_list.append({'rect': bottom_pipe, 'top': False, 'passed': False})


    # Background
    if background_img:
        if not game_paused:
            background_scroll -= background_speed
            if abs(background_scroll) > SCREEN_WIDTH:
                background_scroll = 0

        screen.blit(background_img, (background_scroll, 0))
        screen.blit(background_img, (background_scroll + SCREEN_WIDTH, 0))
    else:
        screen.fill(SKY)


    if not game_paused:

        if game_active:
            # Bird physics
            bird_movement += gravity
            bird_rect.centery += bird_movement

            # Limit max falling speed (smooth control)
            if bird_movement > 8:
                bird_movement = 8

        if game_active:
            pipe_list = move_pipes(pipe_list)

        if game_active:
            game_active = check_collision(pipe_list)

        # Score system
        if game_active:
            for pipe in pipe_list:
                if not pipe['top'] and not pipe['passed']:
                    if bird_rect.left > pipe['rect'].right:
                        score += 1
                        pipe['passed'] = True
        else:
            high_score = max(high_score, score)


    draw_pipes(pipe_list)
    draw_bird()

    # Ground
    if not game_paused:
        ground_scroll -= pipe_speed
        if abs(ground_scroll) > SCREEN_WIDTH:
            ground_scroll = 0

    screen.blit(ground_img, (ground_scroll, SCREEN_HEIGHT - ground_height))
    screen.blit(ground_img, (ground_scroll + SCREEN_WIDTH, SCREEN_HEIGHT - ground_height))


    # Particles
    for p in particles:
        pygame.draw.circle(screen, p[1], (int(p[0][0]), int(p[0][1])), p[2])
        p[3] -= 1
        p[0][1] -= 1

    particles = [p for p in particles if p[3] > 0]


    # UI
    if game_paused:
        pause_surface = font.render("PAUSED - Press P to Resume", True, WHITE)
        screen.blit(pause_surface, (30, SCREEN_HEIGHT // 2 - 20))

    elif not game_active:
        game_over_surface = font.render("Game Over! Press SPACE or R", True, WHITE)
        screen.blit(game_over_surface, (40, SCREEN_HEIGHT // 2 - 20))

        high_score_surface = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(high_score_surface, (120, SCREEN_HEIGHT // 2 + 20))

    else:
        display_score(score)

    pygame.display.update()
    clock.tick(FPS)














