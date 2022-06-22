from turtle import done
import pygame
import numpy as np
import pyautogui

pygame.init()

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

def startGame():
    screen = pygame.display.set_mode((700,600))  
    done = False  

    xcoord=[50,150,250,350,450,550,650]
    ycoord=[50,150,250,350,450,550]

    matrix = np.zeros(shape=(6,7), dtype=int)

    for i in xcoord:
        for j in ycoord:
            pygame.draw.circle(screen,(255,255,255),[i,j],35)

    colChosen=-1
    chance=1
    currHeight=[0]*7
    count=0
    s=""

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
                    else:
                        colChosen=-1
                    if(colChosen!=-1 and currHeight[colChosen]<6):
                        count+=1
                        if(count==42):
                            s="Game Over! It's a Draw!"
                            done=True
                        currHeight[colChosen]+=1
                        newx=xcoord[colChosen]
                        newy=600-ycoord[currHeight[colChosen]-1]
                        col = colChosen
                        row = 6-currHeight[colChosen]
                        matrix[row][col] = 1
                        print(matrix)

                        pygame.draw.circle(screen,(255,0,0),[newx,newy],35)
                        
                        ans = check(matrix, row, col)
                        if ans == 1:
                            s="Player 1 Won!"
                            done = True
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
                    else:
                        colChosen=-1
                    if(colChosen!=-1 and currHeight[colChosen]<6):
                        count+=1
                        if(count==42):
                            s="Game Over! It's a Draw!"
                            done=True
                        currHeight[colChosen]+=1
                        newx=xcoord[colChosen]
                        newy=600-ycoord[currHeight[colChosen]-1]
                        col = colChosen
                        row = 6-currHeight[colChosen]
                        matrix[row][col] = 2
                        print(matrix)
                        print(ans)

                        pygame.draw.circle(screen,(255,255,0),[newx,newy],35)
                        
                        ans=check(matrix, row, col)
                        if ans == 1:
                            s="Player 2 Won!"
                            done = True
                        chance=1
                    print("Currently chosen Column by Player",chance,"is:",colChosen)   
        pygame.display.flip() 
    pyautogui.alert(s)
    

mainScreen = pygame.display.set_mode((700,600))  

input_box1 = pygame.Rect(250, 100, 140, 32)
input_box2 = pygame.Rect(250, 175, 140, 32)

col_box1 = pygame.Rect(450, 100, 32, 32)
col_box2 = pygame.Rect(450, 175, 32, 32)

active=False
input1Entered=False
input2Entered=False
txt1='Player 1'
txt2='Player 2'

while not active:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            active = True
        if(event.type == pygame.MOUSEBUTTONDOWN):
            if(input_box1.collidepoint(event.pos)):
                input1Entered = True
                input2Entered = False
            elif(input_box2.collidepoint(event.pos)):
                input2Entered = True
                input1Entered = False
            else:
                input1Entered = False
                input2Entered = False
        if(event.type == pygame.KEYDOWN):
            if(input1Entered):
                if(event.key==pygame.K_RETURN):
                    print(txt1)
                    txt1='Player 1'
                elif(event.key==pygame.K_BACKSPACE):
                    txt1=txt1[:-1]
                else:
                    txt1+=event.unicode
            if(input2Entered):
                if(event.key==pygame.K_RETURN):
                    print(txt2)
                    txt2='Player 2'
                elif(event.key==pygame.K_BACKSPACE):
                    txt2=txt2[:-1]
                else:
                    txt2+=event.unicode

    font = pygame.font.Font(None, 32)
    mainScreen.fill((30, 30, 30))
    head1_surf = font.render("Player 1: ",True,'white')
    head2_surf = font.render("Player 2: ",True,'white')
    txt1_surface = font.render(txt1, True, 'white')
    txt2_surface = font.render(txt2, True, 'white')
    mainScreen.blit(head1_surf, (input_box1.x-125, input_box1.y+5))
    mainScreen.blit(txt1_surface, (input_box1.x+5, input_box1.y+5))
    mainScreen.blit(head2_surf, (input_box2.x-125, input_box2.y+5))
    mainScreen.blit(txt2_surface, (input_box2.x+5, input_box2.y+5))
    pygame.draw.rect(mainScreen, 'white', input_box1, 2)
    pygame.draw.rect(mainScreen, 'white', input_box2, 2)
    pygame.draw.rect(mainScreen,'red',col_box1)
    pygame.draw.rect(mainScreen,'yellow',col_box2)

    pygame.display.flip()      
            
