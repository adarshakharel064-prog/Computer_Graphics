# import pygame
# import sys

# pygame.init()
# w,h=800,800
# screen=pygame.display.set_mode((w,h))
# white=(255,255,255)
# black=(0,0,0)

# def dda(x1,y1,x2,y2):
#     dx=x2-x1
#     dy=y2-y1
#     if abs(dx)>abs(dy):
#         step=dx
#     else:
#         step=dy

#     xinc=dx/step
#     yinc=dy/step

#     for i  in range (1,step+1):
#         x1+=xinc
#         y1+=yinc
#         screen.set_at((round(x1),round(y1)),white)

# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             screen.fill(black)
    
#     dda(150,0,50,100)    
#     dda(50,100,50,200)    
#     dda(250,100,250,200)    
#     dda(150,0,250,100)    
#     dda(100,150,100,200)    
#     dda(200,150,200,200)    
#     dda(50,200,250,200)
#     dda(100,150,200,150)
#     dda(50,100,250,100)
#     dda(150,0,50,100)
#     pygame.display.flip()    


# import pygame
# import sys
# pygame.init()
# w,h=800,600
# screen=pygame.display.set_mode((w,h))

# white=(255,255,255)
# black=(0,0,0)

# def bls(x1,y1,x2,y2):
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)

#     if(x2>x1):
#         lx=1
#     else:
#         lx=-1

#     if(y2>y1):
#         ly=1
#     else:
#         ly=-1

#     if(dx>dy):
#         p=2*dy-dx
#         for i in range (1,dx+1):
#             if(p<0):
#                 x1+=lx
#                 p=p+2*dy

#             else:
#                 x1+=lx
#                 y1+=ly
#                 p=p+2*dy-2*dx

#             screen.set_at((x1,y1),white)    

#     else:
#         p=2*dx-dy
#         for i in range (1,dy+1):
#             if(p<0):
#                 y1+=ly
#                 p=p+2*dx

#             else:
#                 x1+=lx
#                 y1+=ly
#                 p=p+2*dx-2*dy

#             screen.set_at((x1,y1),white)      


# def main():
#     while True:
#         for event in pygame.event.get():
#                 if event.type==pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#         screen.fill(black)
         
#         bls(400,50,100,400)
#         bls(100,400,700,400)
#         bls(700,400,400,50)
#         bls(100,200,400,550)
#         bls(400,550,700,200)
#         bls(700,200,100,200)
#         pygame.display.flip()  

# if __name__=="__main__":
#     main()                  



# import pygame
# import sys
# pygame.init()
# w,h=800,600
# screen=pygame.display.set_mode((w,h))

# white=(255,255,255)
# black=(0,0,0)
       
# def circle(xc,yc,r):
#     x=0
#     y=r
#     p=1-r

#     while(x<=y):
#         screen.set_at((xc+x,yc+y),white)
#         screen.set_at((xc-x,yc+y),white)
#         screen.set_at((xc+x,yc-y),white)
#         screen.set_at((xc-x,yc-y),white)
#         screen.set_at((xc+y,yc+x),white)
#         screen.set_at((xc-y,yc+x),white)
#         screen.set_at((xc+y,yc-x),white)
#         screen.set_at((xc-y,yc-x),white)

#         if(p<0):
#              x+=1
#              p=p+2*x+1
#         else:
#              x+=1
#              y-=1
#              p=p+2*(x-y)+1
             
    
# def main():
#     while True:
#         for event in pygame.event.get():
#                 if event.type==pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#         screen.fill(black)
         
#         circle(100,100,30)
#         pygame.display.flip()  

# if __name__=="__main__":
#     main()           

import pygame
import sys

pygame.init()

w,h = 800,600
screen = pygame.display.set_mode((w,h))

white = (255,255,255)
black = (0,0,0)


def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    # Region 1
    while 2*ry2*x < 2*rx2*y:
        screen.set_at((xc + x, yc + y), white)
        screen.set_at((xc - x, yc + y), white)
        screen.set_at((xc + x, yc - y), white)
        screen.set_at((xc - x, yc - y), white)

        if p1 < 0:
            x = x + 1
            y = y
            p1 = p1 + 2*ry2*x + ry2
        else:
            x = x + 1
            y = y - 1
            p1 = p1 + 2*ry2*x - 2*rx2*y + ry2

    # Region 2
    p2 = (ry2 * (x + 0.5) * (x + 0.5)) + (rx2 * (y - 1) * (y - 1)) - (rx2 * ry2)

    while y >= 0:
        screen.set_at((xc + x, yc + y), white)
        screen.set_at((xc - x, yc + y), white)
        screen.set_at((xc + x, yc - y), white)
        screen.set_at((xc - x, yc - y), white)

        if p2 > 0:
            y = y - 1
            x = x
            p2 = p2 + rx2 - 2*rx2*y
        else:
            x = x + 1
            y = y - 1
            p2 = p2 + 2*ry2*x - 2*rx2*y + rx2


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(black)
        midpoint_ellipse(300,300,50,100)
        pygame.display.flip()


if __name__ == "__main__":
    main()