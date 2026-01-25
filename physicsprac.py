
import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

x = 400
y = 0
radius = 15

vx = 3
vy = 0
gravity = 0.8
bounce = 0.9

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    vy += gravity
    x += vx
    y += vy

    #yaa chai ground ma xuda bounce back hune concept use vaa xa
    if y + radius >= height:
        y = height - radius
        vy = -vy * bounce

    #yaa chai left or right bounadry ,a xuda farkine concept use vaa xa
    if x - radius <= 0 or x + radius >= width:
        vx = -vx

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()




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

#     # Stop when ball hits the ground
#     if y + radius >= height:
#         y = height - radius
#         running = False

#     #bounces back when ball hits the horizontal ball
#     if x - radius <= 0 or x + radius >= width:
#         vx = -vx

#     # Drawing
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), radius)
#     pygame.draw.line(screen, (100, 100, 100), (0, height-1), (width, height-1), 2)
#     pygame.display.flip()

#     clock.tick(30)

# pygame.quit()


































































