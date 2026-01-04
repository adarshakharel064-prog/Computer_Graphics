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
    print(x1,y1) 
    
    
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
            print(x1,y1)  
     
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
            print(x1,y1)                          

BLS(10,20,30,40)        