import pygame
import time
import random


pygame.init()

white = (255, 255, 255)
red=(255,0,0)
dis_width = 700
dis_height  = 460
ecran = pygame.display.set_mode((dis_width, dis_height))
image = pygame.image.load("generale.jpg").convert_alpha()
ecran.blit(image, (0, 0))
jeux = pygame.image.load("jeux.png").convert_alpha()

score = pygame.image.load("score.png").convert_alpha()


clock = pygame.time.Clock()

pygame.display.set_caption('Snake game by Edureka')
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 20)
 

def our_snake(snake_list,orientation):
    
    for x in range(len(snake_list)):
        
        if orientation=="g" :
            if x==len(snake_list)-1:
                serpent = pygame.image.load("gauche.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
            else :
                serpent = pygame.image.load("queue.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
        elif orientation=="d" :
            if x==len(snake_list)-1:
                serpent = pygame.image.load("droite.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
            else :
                serpent = pygame.image.load("queue.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
        if orientation=="h":
            if x==len(snake_list)-1:
                serpent = pygame.image.load("haut.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
            else :
                serpent = pygame.image.load("queue.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
        elif orientation=="b" :
            if x==len(snake_list)-1:
                serpent = pygame.image.load("bas.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
            else :
                serpent = pygame.image.load("queue.png")
                ecran.blit(serpent, (95+snake_list[x][0]*15, 15+snake_list[x][1]*15))
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    ecran.blit(mesg, [200, 30+7*30])





def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    ecran.blit(value, [99, 2])



def gameLoop():
    jeu=True
    game_close = False
    Sx=16
    Sy = 15 

    Sx_change = 0       
    Sy_change = 0

    snake_List = []
    Length_of_snake = 1

    orientation = "g"


    foodx = random.randint(3,30)
    foody = random.randint(6,25)

    print(str(foodx))
    print(str(foody))

    while jeu:


        while game_close == True:
            ecran.blit(image, (0, 0))
            ecran.blit(score, (95,0 ))
            ecran.blit(jeux, (95, 60))
            message("Perdu! Appuyer Q-Quitter ou C-Rejouer", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        jeu = False
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Sx_change = -1
                    Sy_change = 0
                    orientation = "g"
                elif event.key == pygame.K_RIGHT:
                    Sx_change = 1
                    Sy_change = 0
                    orientation="d"
                elif event.key == pygame.K_UP:
                    Sy_change = -1
                    Sx_change = 0
                    orientation = "h"
                elif event.key == pygame.K_DOWN:
                    Sy_change = 1
                    Sx_change = 0
                    orientation = "b"
        
        
        if Sx < 2 or Sx >31 or Sy <5 or Sy> 26 :
            game_close = True
        

        Sx += Sx_change
        Sy += Sy_change

        ecran.blit(image, (0, 0))
        ecran.blit(score, (95,0 ))
        ecran.blit(jeux, (95, 60))
        
        pommevert = pygame.image.load("pomme.png")
        ecran.blit(pommevert, (95+foodx*15, 15+foody*15))

        

        snake_Head = []
        snake_Head.append(Sx)
        snake_Head.append(Sy)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_List,orientation)
        
        pygame.display.update()
        
        if Sx == foodx and Sy == foody:
            foodx = random.randint(3,30)
            foody = random.randint(6,25)
            Length_of_snake += 1
            
        clock.tick(1)
    
    pygame.quit()
    quit()
gameLoop()