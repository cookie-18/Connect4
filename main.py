import pygame

pygame.init()
screen = pygame.display.set_mode((700,600))  
done = False  

xcoord=[50,150,250,350,450,550,650]
ycoord=[50,150,250,350,450,550]


for i in xcoord:
    for j in ycoord:
        pygame.draw.circle(screen,(255,255,255),[i,j],35)

colChosen=-1
chance=1
currHeight=[0]*7
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
        elif event.type==pygame.MOUSEBUTTONDOWN:
            isPressed=pygame.mouse.get_pressed()[0]    
            if(isPressed and chance==1):        
                x,y=pygame.mouse.get_pos()
                if(15<=x<=85):
                    colChosen=0
                elif(115<=x<=185):
                    colChosen=1
                elif(215<=x<=285):
                    colChosen=2
                elif(315<=x<=385):
                    colChosen=3
                elif(415<=x<=485):
                    colChosen=4
                elif(515<=x<=585):
                    colChosen=5
                elif(615<=x<=685):
                    colChosen=6
                if(currHeight[colChosen]<6):
                    currHeight[colChosen]+=1
                    newx=xcoord[colChosen]
                    newy=600-ycoord[currHeight[colChosen]-1]
                    pygame.draw.circle(screen,(255,0,0),[newx,newy],35)
                    chance=2
                print("Currently chosen Column by Player",chance,"is:",colChosen)    
            elif(isPressed and chance==2):        
                x,y=pygame.mouse.get_pos()
                if(15<=x<=85):
                    colChosen=0
                elif(115<=x<=185):
                    colChosen=1
                elif(215<=x<=285):
                    colChosen=2
                elif(315<=x<=385):
                    colChosen=3
                elif(415<=x<=485):
                    colChosen=4
                elif(515<=x<=585):
                    colChosen=5
                elif(615<=x<=685):
                    colChosen=6
                if(currHeight[colChosen]<6):
                    currHeight[colChosen]+=1
                    newx=xcoord[colChosen]
                    newy=600-ycoord[currHeight[colChosen]-1]
                    pygame.draw.circle(screen,(255,255,0),[newx,newy],35)
                    chance=1
                print("Currently chosen Column by Player",chance,"is:",colChosen)   
    pygame.display.flip() 
    
print(34)
