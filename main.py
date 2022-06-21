import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode((700,600))  
done = False  

xcoord=[50,150,250,350,450,550,650]
ycoord=[50,150,250,350,450,550]

matrix = np.zeros(shape=(6,7), dtype=int)

def check(matrix, row, col):
    
    currp = matrix[row][col]

    #check down
    if row<=2:
        if(matrix[row][col]==matrix[row+1][col]==matrix[row+2][col]==matrix[row+3][col]==currp):
            return 1
    

    #check horizontal

    #3 left 0 right     6>=col>=3
    #2 left 1 right     5>=col>=2
    #1 left 2 right     4>=col>=1
    #0 left 3 right     3>=col>=0

    if(3<=col<=6):
        if(matrix[row][col]==matrix[row][col-1]==matrix[row][col-2]==matrix[row][col-3]==currp):
            return 1
    
    if(2<=col<=5):
        if(matrix[row][col-2]==matrix[row][col-1]==matrix[row][col]==matrix[row][col+1]==currp):
            return 1
    
    if(1<=col<=4):
        if(matrix[row][col-1]==matrix[row][col]==matrix[row][col+1]==matrix[row][col+2]==currp):
            return 1
    
    if(0<=col<=3):
        if(matrix[row][col]==matrix[row][col+1]==matrix[row][col+2]==matrix[row][col+3]==currp):
            return 1


    #top right and bot left
    # 0 bot left and 3 top right    3<=row<=5 and 0<=col<=3
    if(3<=row<=5 and 0<=col<=3):
        if(matrix[row][col]==matrix[row-1][col+1]==matrix[row-2][col+2]==matrix[row-3][col+3]==currp):
            return 1

    # 1 bot left and 2 top right    2<=row<=4 and 1<=col<=4 
    if(2<=row<=4 and 1<=col<=4):
        if(matrix[row+1][col-1]==matrix[row][col]==matrix[row-1][col+1]==matrix[row-2][col+2]==currp):
            return 1

    # 2 bot left and 1 top right    1<=row<=3 and 2<=col<=5
    if(1<=row<=3 and 2<=col<=5):
        if(matrix[row+2][col-2]==matrix[row+1][col-1]==matrix[row][col]==matrix[row-1][col+1]==currp):
            return 1
    # 3 bot left and 0 top right    0<=row<=2 and 3<=col<=6
    if(0<=row<=2 and 3<=col<=6):
        if(matrix[row+3][col-3]==matrix[row+2][col-2]==matrix[row+1][col-1]==matrix[row][col]==currp):
            return 1
            
    #top left and bot right
        
    # 0 bot right and 3 top left    3<=row<=5 and 3<=col<=6
    if(3<=row<=5 and 3<=col<=6):
        if(matrix[row][col]==matrix[row-1][col-1]==matrix[row-2][col-2]==matrix[row-3][col-3]==currp):
            return 1

    # 1 bot right and 2 top left    2<=row<=4 and 2<=col<=5 
    if(2<=row<=4 and 2<=col<=5):
        if(matrix[row+1][col+1]==matrix[row][col]==matrix[row-1][col-1]==matrix[row-2][col-2]==currp):
            return 1

    # 2 bot right and 1 top left    1<=row<=3 and 1<=col<=4
    if(1<=row<=3 and 1<=col<=4):
        if(matrix[row+2][col+2]==matrix[row+1][col+1]==matrix[row][col]==matrix[row-1][col-1]==currp):
            return 1
    # 3 bot right and 0 top left    0<=row<=2 and 0<=col<=3
    if(0<=row<=2 and 0<=col<=3):
        if(matrix[row+3][col+3]==matrix[row+2][col+2]==matrix[row+1][col+1]==matrix[row][col]==currp):
            return 1
        
    return 0

for i in xcoord:
    for j in ycoord:
        pygame.draw.circle(screen,(255,255,255),[i,j],35)

colChosen=-1
chance=1
currHeight=[0]*7
count=0
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
                    count+=1
                    if(count==42):
                        done=True
                    currHeight[colChosen]+=1
                    newx=xcoord[colChosen]
                    newy=600-ycoord[currHeight[colChosen]-1]
                    col = colChosen
                    row = 6-currHeight[colChosen]
                    matrix[row][col] = 1
                    print(matrix)
                    ans = check(matrix, row, col)

                    if ans == 1:
                        print(chance, "Player WON")
                        done = True

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
                    count+=1
                    if(count==42):
                        done=True
                    currHeight[colChosen]+=1
                    newx=xcoord[colChosen]
                    newy=600-ycoord[currHeight[colChosen]-1]
                    col = colChosen
                    row = 6-currHeight[colChosen]
                    matrix[row][col] = 2
                    print(matrix)
                    ans=check(matrix, row, col)
                    print(ans)
                    if ans == 1:
                        print(chance, "Player WON")
                        done = True

                    pygame.draw.circle(screen,(255,255,0),[newx,newy],35)
                    chance=1
                print("Currently chosen Column by Player",chance,"is:",colChosen)   
    pygame.display.flip() 

    
    

