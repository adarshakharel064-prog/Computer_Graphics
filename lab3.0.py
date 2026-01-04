import pygame
import sys
pygame.init()
w,h=800,600
screen=pygame.display.set_mode((w,h))

white=(255,255,255)
black=(0,0,0)

def BLS(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if(x2>x1):
        lx=1
    else:
        lx=-1
    
    if(y2>y1):
        ly=1
    else:
        ly=-1
    screen.set_at((x1,y1),white)  
    
    
    if(dx>dy):    
        pk=2*dy-dx
        
        for i in range (1,dx+1):
            if(pk<0):
                x1+=lx
                pk+=2*dy
            else:        
                x1+=lx
                y1+=ly  
                pk+=2*dy -2*dx 
            screen.set_at((x1,y1),white)   
     
    else:
        pk=2*dx-dy
        
        for i in range (1,dy+1):
            if(pk<0):
                y1+=ly
                pk+=2*dx
            else:        
                x1+=lx
                y1+=ly  
                pk+=2*dx -2*dy 
            screen.set_at((x1,y1),white)                          
        
def main():
    while True:
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        screen.fill(black)
         
        BLS(400,50,100,400)
        BLS(100,400,700,400)
        BLS(700,400,400,50)
        BLS(100,200,400,550)
        BLS(400,550,700,200)
        BLS(700,200,100,200)
        pygame.display.flip()  

if __name__=="__main__":
    main() 