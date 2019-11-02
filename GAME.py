import pygame
import time
import random
pygame.init()
display_x = 400
display_y = 600
white=(255,255,255)
red=(200,0,0)
bright_red=(255,0,0)
dblue=(0,50,255)
blue=(0,150,255)
back_grd=(0,250,250)
green=(0,200,0)
bright_green=(0,255,0)
black=(0,0,0)
gamedisplay=pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('BALL RUNNER')
clock=pygame.time.Clock()
detect_x=60
detective = pygame.image.load('detective.png')
pygame.display.set_icon(detective)
crashsound = pygame.mixer.Sound("C:\\Users\\user\\Desktop\\pygame\\crash.wav")
Y_cor=-100
X_cor=random.randrange(0,display_x)
block_w=random.randrange(10,75)
block_h=random.randrange(10,75)
pause=False

def set_score(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("score: "+str(count),True,white)
    gamedisplay.blit(text,(0,0))

def object_(X_cor, Y_cor,block_w,block_h,color):
    pygame.draw.rect( gamedisplay, color, [ X_cor, Y_cor, block_w, block_h] )
    

def car(x,y):
    gamedisplay.blit(detective,(x,y))


def text_OBJ(text,font,color):
    text_surf=font.render( text, True, color)
    return text_surf,text_surf.get_rect()#it gives a rect around the text


    
def hit(text,color):
    pygame.mixer.Sound.play(crashsound)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gamedisplay.fill(back_grd)
        font=pygame.font.SysFont("comicsansms",50)
        text_surf,text_rect = text_OBJ("YOU CRASHED!!",font,blue)#text_surf contains the message and text_rect is the reference to the position of the text box. 
        text_rect.center = ((display_x*.5),(display_y*.5))
        gamedisplay.blit(text_surf,text_rect)
        button("REPLAY",40,350,100,30,green,bright_green,"play")
        button("QUIT!",260,350,100,30,red,bright_red,"quit")

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,act):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
       
      
    if (x<mouse[0]<x+w and y<mouse[1]<y+h):
        pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and act=="play":
            game_loop()
        elif click[0]==1 and act=="quit":
            pygame.quit()
            quit()
        elif click[0]==1 and act=="none":
            unpause()
    else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
    small_text=pygame.font.SysFont("comicsansms",20)
    textsurf,textrect=text_OBJ(msg,small_text,black)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplay.blit(textsurf,textrect)

def first_page():
    start=True
    while start:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(back_grd)
        font=pygame.font.SysFont("comicsansms",50)
        text_surf,text_rect = text_OBJ("BALL RUNNER",font,blue)#text_surf contains the message and text_rect is the reference to the position of the text box. 
        text_rect.center = ((display_x*.5),(display_y*.5))
        gamedisplay.blit(text_surf,text_rect)
        button("START",40,350,100,30,green,bright_green,"play")
        button("QUIT!",260,350,100,30,red,bright_red,"quit")
   

        
        pygame.display.update()
        clock.tick(15)
   

def paused():
    
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gamedisplay.fill(back_grd)
        font=pygame.font.SysFont("comicsansms",50)
        text_surf,text_rect = text_OBJ("PAUSED",font,blue)#text_surf contains the message and text_rect is the reference to the position of the text box. 
        text_rect.center = ((display_x*.5),(display_y*.5))
        gamedisplay.blit(text_surf,text_rect)
        button("CONTINUE",40,350,120,30,green,bright_green,"none")
        button("QUIT!",260,350,100,30,red,bright_red,"quit")
   

        
        pygame.display.update()
        clock.tick(15)
def unpause():
    global pause
    pause=False
def game_loop():
    global pause
    count=0
    Y_cor=-100
    X_cor=random.randrange(0,display_x)
    x = (display_x*0.50)
    y = (display_y-detect_x)
    crashed=False
    x_change=0
    y_change=0
    Y_cor=-500
    X_cor=random.randrange(0,display_x)
    block_w=random.randrange(60,85)
    block_h=random.randrange(60,85)
    speed=4
    while not crashed:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change=-5
                if event.key == pygame.K_RIGHT:
                    x_change =+5
                if event.key == pygame.K_UP:
                    y_change=-5
                if event.key == pygame.K_DOWN:
                    y_change=5
                if  event.key == pygame.K_p:
                    pause=True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change=0
                    y_change=0
        x+=x_change
        y+=y_change
        gamedisplay.fill(back_grd)
        pygame.draw.line(gamedisplay,black,(5,0),(5,display_y),3)
        pygame.draw.line(gamedisplay,black,(display_x-5,0),(display_x-5,display_y),3)
        car(x,y)
        set_score(count)
        object_(X_cor, Y_cor,block_w, block_h,dblue)
        Y_cor+=speed
        rand_y=random.randrange(display_y/2,display_y)
        if Y_cor>display_y:
            Y_cor=-100
            X_cor=random.randrange(0,display_x)
            block_w=random.randrange(60,85)
            block_h=random.randrange(60,85)
            count+=1
            m=count/10
            l=m
            if(l==int(m)):
                speed+=int(m)
                l=m
        else:
             block_w = block_w
             block_h = block_h


        if Y_cor<=y<= Y_cor+block_h and X_cor<=x<=X_cor+block_w or Y_cor<=y+detect_x<= Y_cor+block_h and X_cor<=x+detect_x<=X_cor+block_w :
            hit('YOU HIT!!',red)

        #if Y_cor>rand_y:
            #object_(X_cor, Y_cor,block_w, block_h,blue)


        #position..
        if x>(display_x-detect_x):
            x=display_x-detect_x
        elif x<0:
            x=0
            #hit('YOU HIT')
        if y>display_y-detect_x:
            y=display_y-detect_x
        elif y<0:
            y=0

        #if(y==0):
         #   hit('YOU WIN!!',green)
            
        pygame.display.update()
        clock.tick(120)
first_page()
pygame.quit()
quit()
