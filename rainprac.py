import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain Scene with Proper Clouds")
clock = pygame.time.Clock()

RAIN=(173, 216, 230)
SKY=(30, 30, 50)

#raindrops ko starting position milako
raindrops=[]
for _ in range(200):
    raindrops.append([
        random.randint(0,WIDTH), #starting x position
        random.randint(-HEIGHT,HEIGHT), #starting y position
        random.randint(5,10) #speed
    ])
# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(SKY)  #set background colour
    for drop in raindrops:
        drop[1] += drop[2] #resets position of drop to show movemrnt
        if drop[1] > HEIGHT:#reappring and random apperance of drop
            drop[0] = random.randint(0, WIDTH)
            drop[1] = random.randint(-100, 0)

        pygame.draw.line(screen,RAIN,(drop[0], drop[1]),(drop[0], drop[1] + 10),2
        )
    pygame.display.flip()
    clock.tick(80)

pygame.quit()



