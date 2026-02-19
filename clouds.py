#generating clouds

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Scene with Proper Clouds")
clock = pygame.time.Clock()


SKY = (30, 30, 50)
CLOUD = (220, 220, 220)
RAIN = (173, 216, 230)

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
   
    pygame.display.flip()

pygame.quit()