# import pygame
# import sys
# pygame.init()
# w,h=1000,1000
# screen=pygame.display.set_mode((w,h))

# white=(255,255,255)
# red=(255,0,0)

# black=(0,0,0)

# def translate(x1,y1,x2,y2,tx,ty):
#     pygame.draw.line(screen,white,(x1,y1),(x2,y2),2)
#     x1=x1+tx
#     y1=y1+ty
#     x2=x2+tx
#     y2=y2+ty
#     pygame.draw.line(screen,red,(x1,y1),(x2,y2),2)

# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         screen.fill(black)
        


#         translate(100,100,600,600,150,150)
        
        
#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()




# import pygame
# import sys
# pygame.init()
# w,h=800,800
# screen=pygame.display.set_mode((w,h))

# white=(255,255,255)
# red=(255,0,0)

# black=(0,0,0)

# def scale(x1,y1,x2,y2,sx,sy):
#     pygame.draw.line(screen,white,(x1,y1),(x2,y2),2)
#     x1=x1*sx
#     y1=y1*sy
#     x2=x2*sx
#     y2=y2*sy
#     pygame.draw.line(screen,red,(x1,y1),(x2,y2),2)

# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         screen.fill(black)
        


#         scale(100,100,600,600,1.5,1.2)
        
        
#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()

# import pygame
# import sys
# from math import radians
# from math import cos
# from math import sin
# pygame.init()
# w,h=800,800
# screen=pygame.display.set_mode((w,h))

# white=(255,255,255)
# red=(255,0,0)

# black=(0,0,0)

# def rotate(x1,y1,x2,y2):
#     angle=radians(30)
#     pygame.draw.line(screen,white,(x1,y1),(x2,y2),2)
#     x1=x1*cos(angle)-y1*sin(angle)
#     y1=x1*cos(angle)+y1*sin(angle)
#     x2=x2*cos(angle)-y2*sin(angle)
#     y2=x2*cos(angle)+y2*sin(angle)
#     pygame.draw.line(screen,red,(x1,y1),(x2,y2),2)

# def main():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#         screen.fill(black)
        


#         rotate(100,100,600,600)
        
        
#         pygame.display.flip()

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()

# import pygame
# import sys
# import time

# pygame.init()
# w, h = 1000, 1000
# screen = pygame.display.set_mode((w, h))

# white = (255, 255, 255)
# red = (255, 0, 0)
# black = (0, 0, 0)

# def translate(x1, y1, x2, y2):
    
#     pygame.draw.line(screen, white, (x1, y1), (x2, y2), 2)
#     pygame.display.flip()
#     time.sleep(0.5)  

#     i = 1
#     while i < 15:
#         x1 = x1 + 10
#         y1=y1
#         x2 = x2 + 10
#         y2=y2

#         pygame.draw.line(screen, red, (x1, y1), (x2, y2), 2)
#         pygame.display.flip()   
#         time.sleep(0.5)         

#         i += 1

# def main():
#     running = True
#     screen.fill(black)

#     translate(100, 100, 600, 600)

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#     pygame.quit()
#     sys.exit()

# if __name__ == "__main__":
#     main()


import pygame
import sys
from math import *

pygame.init()

w,h=(800,600)
screen=pygame.display.set_mode((w,h))

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)

def translation(x1,y1,x2,y2,tx,ty):
    pygame.draw.line(screen, white, (x1,y1), (x2,y2), 2)
    x1=x1+tx
    y1=y1+ty
    x2=x2+tx
    y2=y2+ty
    pygame.draw.line(screen, red, (x1,y1), (x2,y2), 2)

def scaling(x1,y1,x2,y2,sx,sy):
    pygame.draw.line(screen, white, (x1,y1), (x2,y2), 2)
    x1=x1*sx
    y1=y1*sy
    x2=x2*sx
    y2=y2*sy
    pygame.draw.line(screen, green, (int(x1),int(y1)), (int(x2),int(y2)), 2)
    


def rotation(x1,y1,x2,y2,angle):
    rad = - radians(angle)
    pygame.draw.line(screen, white, (x1,y1), (x2,y2), 2)
    x = x2 - x1
    y = y2 - y1

    xr = x * cos(rad) - y * sin(rad)
    yr = x * sin(rad) + y * cos(rad)

    x2r = x1 + xr
    y2r = y1 + yr

    pygame.draw.line(screen,blue,(x1, y1),(int(x2r), int(y2r)),2)

def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        translation(300,300,200,200,50,25)
        scaling(200,50,300,50,1.5,1.5)
        rotation(0,0,150,150,40)

        pygame.display.flip()

if __name__ == "__main__":
    main()