# import pygame

# pygame.init()

# width = 800
# height = 600
# screen = pygame.display.set_mode((width, height))
# clock = pygame.time.Clock()

# x = 400
# y = 0
# radius = 15

# vx = 3
# vy = 0
# gravity = 0.8
# bounce = 0.9

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     vy += gravity
#     x += vx
#     y += vy

#     #yaa chai ground ma xuda bounce back hune concept use vaa xa
#     if y + radius >= height:
#         y = height - radius
#         vy = -vy * bounce

#     #yaa chai left or right bounadry ,a xuda farkine concept use vaa xa
#     if x - radius <= 0 or x + radius >= width:
#         vx = -vx*bounce

#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)
#     pygame.display.flip()

#     clock.tick(60)

# pygame.quit()




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from mpl_toolkits.mplot3d import Axes3D

# # Physics parameters
# u = 25        # initial velocity (m/s)
# theta = 45    # vertical angle (degrees)
# phi = 30      # horizontal angle (degrees)
# g = 9.8       # gravity (m/s^2)

# # Convert to radians
# theta = np.radians(theta)
# phi = np.radians(phi)

# # Time of flight
# T = (2 * u * np.sin(theta)) / g
# t = np.linspace(0, T, 300)

# # 3D motion equations
# x = u * np.cos(theta) * np.cos(phi) * t
# y = u * np.cos(theta) * np.sin(phi) * t
# z = u * np.sin(theta) * t - 0.5 * g * t**2

# # Create 3D figure
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# ax.set_xlim(0, max(x) + 2)
# ax.set_ylim(0, max(y) + 2)
# ax.set_zlim(0, max(z) + 2)

# ax.set_xlabel("X (meters)")
# ax.set_ylabel("Y (meters)")
# ax.set_zlabel("Z (height in meters)")
# ax.set_title("3D Projectile Motion of a Ball")

# ball, = ax.plot([], [], [], marker='o')
# trail, = ax.plot([], [], [])

# # Initialization
# def init():
#     ball.set_data([], [])
#     ball.set_3d_properties([])
#     trail.set_data([], [])
#     trail.set_3d_properties([])
#     return ball, trail

# # Animation update
# def update(frame):
#     ball.set_data(x[frame], y[frame])
#     ball.set_3d_properties(z[frame])
#     trail.set_data(x[:frame], y[:frame])
#     trail.set_3d_properties(z[:frame])
#     return ball, trail

# ani = FuncAnimation(fig, update, frames=len(t),
#                     init_func=init, interval=30, blit=True)

# plt.show()

# import pygame
# import math

# pygame.init()

# # Screen setup
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Projectile Motion - Ball")
# clock = pygame.time.Clock()

# # Ball properties
# radius = 12
# x = 100
# y = height - 100

# # Physics parameters
# speed = 20              # initial speed
# angle = 45              # launch angle (degrees)
# gravity = 0.5
# bounce=0.8

# # Convert angle to radians
# angle_rad = math.radians(angle)

# # Velocity components
# vx = speed * math.cos(angle_rad)
# vy = -speed * math.sin(angle_rad)  # negative because screen y increases downward

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Apply physics
#     vy += gravity
#     x += vx
#     y += vy


#     #bounces back when ball hits the horizontal ball
#     if x - radius <= 0 or x + radius >= width:
#         vx = -vx

#     # yaa chai ground ma xuda bounce back hune concept use vaa xa
#     if y + radius >= height:
#         y = height - radius
#         vy = -vy * bounce

#     # Stop when ball hits the ground
#     if y + radius >= height:
#         y = height - radius
       

  
        
#     # Drawing
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)
#     pygame.draw.line(screen, (100, 100, 100), (0, height-1), (width, height-1), 2)
#     pygame.display.flip()

#     clock.tick(30)

# pygame.quit()

# import pygame
# import random

# pygame.init()

# # Screen setup
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Rainy Scene with Clouds")
# clock = pygame.time.Clock()

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (180, 180, 180)
# BLUE = (100, 100, 255)

# # Raindrop settings
# NUM_DROPS = 200
# raindrops = []

# for _ in range(NUM_DROPS):
#     x = random.randint(0, WIDTH)
#     y = random.randint(-HEIGHT, HEIGHT)
#     speed = random.randint(4, 10)
#     raindrops.append([x, y, speed])

# # Function to draw clouds
# def draw_cloud(x, y):
#     pygame.draw.circle(screen, GRAY, (x, y), 30)
#     pygame.draw.circle(screen, GRAY, (x + 30, y), 40)
#     pygame.draw.circle(screen, GRAY, (x + 70, y), 30)
#     pygame.draw.rect(screen, GRAY, (x - 10, y, 110, 40))

# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(BLACK)

#     # Draw clouds
#     draw_cloud(150, 80)
#     draw_cloud(400, 60)
#     draw_cloud(600, 90)

#     # Update and draw raindrops
#     for drop in raindrops:
#         drop[1] += drop[2]  # move down

#         if drop[1] > HEIGHT:
#             drop[0] = random.randint(0, WIDTH)
#             drop[1] = random.randint(-100, 0)
#             drop[2] = random.randint(4, 10)

#         pygame.draw.line(
#             screen,
#             BLUE,
#             (drop[0], drop[1]),
#             (drop[0], drop[1] + 10),
#             2
#         )

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()


import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Scene with Proper Clouds")
clock = pygame.time.Clock()

# Colors
SKY = (30, 30, 50)
CLOUD = (220, 220, 220)
RAIN = (173, 216, 230)

#  setting position for raindrops
raindrops = []
for _ in range(200):
    raindrops.append([
        random.randint(0, WIDTH), # x-position of raindrop anywhere horizontally
        random.randint(-HEIGHT, HEIGHT),#y-position of raindrop bellow or above screen(makes rain look continous)
        random.randint(5, 10)#speed of rain drop
        ])

#making cloud
def draw_cloud(x, y, scale=1):
    circles = [
        (x, y, int(35 * scale)),
        (x + 30 * scale, y - 20 * scale, int(45 * scale)),
        (x + 70 * scale, y - 10 * scale, int(40 * scale)),
        (x + 110 * scale, y, int(30 * scale)),
        (x + 50 * scale, y + 10 * scale, int(35 * scale))
    ]

    for cx, cy, r in circles:
        pygame.draw.circle(screen, CLOUD, (int(cx), int(cy)), r)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)  #set background colour

    # cloud banaiyo
    draw_cloud(100, 100, 1.2)
    draw_cloud(350, 80, 1.0)
    draw_cloud(600, 110, 1.3)

    # Rain
    for drop in raindrops:
        drop[1] += drop[2]
        if drop[1] > HEIGHT:
            drop[0] = random.randint(0, WIDTH)
            drop[1] = random.randint(-100, 0)

        pygame.draw.line(screen,RAIN,(drop[0], drop[1]),(drop[0], drop[1] + 10),2)
       

    pygame.display.flip()
    clock.tick(80)

pygame.quit()


# import numpy as np
# import matplotlib.pyplot as plt

# WIDTH = 400
# HEIGHT = 300
# MAX_DEPTH = 3

# camera = np.array([0, 0, -1])
# light = {
#     "position": np.array([5, 5, -10]),
#     "intensity": 1.5
# }

# background_color = np.array([0, 0, 0])

# spheres = [
#     {
#         "center": np.array([0, 0, 3]),
#         "radius": 1,
#         "color": np.array([1, 0, 0]),
#         "reflection": 0.5
#     },
#     {
#         "center": np.array([2, 0, 4]),
#         "radius": 1,
#         "color": np.array([0, 1, 0]),
#         "reflection": 0.3
#     }
# ]

# def normalize(v):
#     return v / np.linalg.norm(v)

# def intersect_sphere(origin, direction, sphere):
#     oc = origin - sphere["center"]
#     a = np.dot(direction, direction)
#     b = 2 * np.dot(oc, direction)
#     c = np.dot(oc, oc) - sphere["radius"]**2
#     discriminant = b**2 - 4*a*c

#     if discriminant < 0:
#         return None

#     t1 = (-b - np.sqrt(discriminant)) / (2*a)
#     t2 = (-b + np.sqrt(discriminant)) / (2*a)

#     t = min(t1, t2)
#     if t < 0:
#         t = max(t1, t2)
#     if t < 0:
#         return None

#     return t

# def trace_ray(origin, direction, depth):
#     if depth > MAX_DEPTH:
#         return background_color

#     nearest_t = float("inf")
#     nearest_sphere = None

#     for sphere in spheres:
#         t = intersect_sphere(origin, direction, sphere)
#         if t and t < nearest_t:
#             nearest_t = t
#             nearest_sphere = sphere

#     if nearest_sphere is None:
#         return background_color

#     hit_point = origin + nearest_t * direction
#     normal = normalize(hit_point - nearest_sphere["center"])
#     light_dir = normalize(light["position"] - hit_point)

#     # Shadow check
#     shadow_t = intersect_sphere(hit_point + 1e-5 * normal, light_dir, nearest_sphere)
#     if shadow_t:
#         return nearest_sphere["color"] * 0.1

#     # Diffuse shading
#     diffuse = max(np.dot(normal, light_dir), 0)
#     local_color = nearest_sphere["color"] * diffuse * light["intensity"]

#     # Reflection
#     reflection = nearest_sphere["reflection"]
#     reflected_dir = normalize(direction - 2 * np.dot(direction, normal) * normal)
#     reflected_color = trace_ray(hit_point + 1e-5 * normal, reflected_dir, depth + 1)

#     return (1 - reflection) * local_color + reflection * reflected_color

# image = np.zeros((HEIGHT, WIDTH, 3))

# for y in range(HEIGHT):
#     for x in range(WIDTH):
#         px = (2 * (x + 0.5) / WIDTH - 1) * WIDTH / HEIGHT
#         py = 1 - 2 * (y + 0.5) / HEIGHT
#         direction = normalize(np.array([px, py, 1]))

#         color = trace_ray(camera, direction, 0)
#         image[y, x] = np.clip(color, 0, 1)

# plt.imshow(image)
# plt.axis("off")
# plt.show()





























































