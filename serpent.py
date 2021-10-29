import pygame
import time
import random
from datetime import timedelta, datetime, date, time

pygame.init()

white = (255, 255, 255)
red=(255,0,0)
vert = (255, 255, 255)
dis_width = 700
dis_height  = 460
ecran = pygame.display.set_mode((dis_width, dis_height))
image = pygame.image.load("fond.png").convert_alpha()
ecran.blit(image, (0, 0))

score = pygame.image.load("pomme.png").convert_alpha()

chro = pygame.image.load("chrono.png").convert_alpha()

clock = pygame.time.Clock()

pygame.display.set_caption('Snake serious')
 
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)

def affichage_case(x,y,image_file):
        img = pygame.image.load(image_file)
        ecran.blit(img, (95+x*30, 30+y*30))

def affichage_serpent(liste):
    for i in range(len(liste)):
        affichage_case(liste[i][0],liste[i][1],liste[i][2])



def our_snake(snake_list,orientation,orientationq):

    if len(snake_list)==1 :
        if orientation=="g" : snake_list[0][2] = "gauche.png"
        if orientation=="d" : snake_list[0][2] = "droite.png"
        if orientation=="h" : snake_list[0][2] = "tetehaut.png"
        if orientation=="b" : snake_list[0][2] = "bas.png"
            
    else :
        for x in range(len(snake_list)):
            
            if orientation=="g" :
                if x==len(snake_list)-1: snake_list[x][2] = "gauche.png"
                elif x==0 :
                    if(orientationq=="g") : snake_list[x][2] = "queued.png"
                    elif(orientationq=="d") : snake_list[x][2] = "queueg.png"
                    elif(orientationq=="h") : snake_list[x][2] = "queueb.png"
                    elif(orientationq=="b") : snake_list[x][2] = "queueh.png"            
                    
            elif orientation=="d" :
                if x==len(snake_list)-1: snake_list[x][2] = "droite.png"
                elif x==0 :
                    if(orientationq=="g") : snake_list[x][2] = "queued.png"
                    elif(orientationq=="d") : snake_list[x][2] = "queueg.png"
                    elif(orientationq=="h") : snake_list[x][2] = "queueb.png" #######################
                    elif(orientationq=="b") :snake_list[x][2] = "queueh.png"
                
                    
            elif orientation=="h":
                if x==len(snake_list)-1: snake_list[x][2] = "tetehaut.png"            
                elif x==0 :
                    if(orientationq=="g") : snake_list[x][2] = "queued.png"  
                    elif(orientationq=="d") : snake_list[x][2] = "queueg.png"   ###################                                
                    elif(orientationq=="h") : snake_list[x][2] = "queueb.png"        
                    elif(orientationq=="b") : snake_list[x][2] = "queueh.png"                    
                
                
            elif orientation=="b" :
                if x==len(snake_list)-1: snake_list[x][2] = "bas.png"                
                elif x==0 :
                    if(orientationq=="g") : snake_list[x][2] = "queued.png"                       
                    elif(orientationq=="d") : snake_list[x][2] = "queueg.png"                        
                    elif(orientationq=="h") :snake_list[x][2] = "queueb.png"                        
                    elif(orientationq=="b") :snake_list[x][2] = "queueh.png"                       
                
            if x != len(snake_list)-1 and x != 0:
                if (snake_list[x+1][0]) == snake_list[x][0] :
                    snake_list[x][2] = "corpsv.jpg"    
                else: snake_list[x][2] = "corpsh.jpg"                  
                

 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    ecran.blit(mesg, [200, 30+7*30])


def Your_score(score):
    value = score_font.render("     : "+str(score), True, vert)
    ecran.blit(value, [99, 2])


def My_chrono(chrono):
    value = score_font.render("     : " + str(chrono), True, vert)
    ecran.blit(value, [480, 2])


def Dessin_damier():
    for i in range(13):
        if (i % 2) == 0:
            for j in range(17):
                if (j % 2) == 0:
                    affichage_case(j,i,"carre1.png")
                    
                else:
                    affichage_case(j,i,"carre2.png")
                    
        else:
            for j in range(17):
                if (j % 2) == 0:
                    affichage_case(j,i,"carre2.png")
                    
                else:
                    affichage_case(j,i,"carre1.png")
                    

#Chrono début
font = pygame.font.Font(None, 25)
def _make_chrono_label(chrono):
    "Crée une Surface représentant le temps du chrono"
    return font.render(chrono.strftime("%H : %M : %S"),
                       True, (255, 255, 255))
 
def update(chrono, label, dt):
    """Mise à jour du temps écoulé.
 
    dt est le nombre de millisecondes
    """
    old_chrono = chrono
    chrono += timedelta(milliseconds=dt)
    # Comme le chrono n'indique pas les fractions de secondes,
    # on ne met à jour le label que si quelque chose de visible a changé
    if old_chrono.second != chrono.second:
        label = _make_chrono_label(chrono)
    return chrono, label

#chrono fin

def gameLoop():
    #chrono début
    chrono1 = datetime.combine(date.today(), time(0, 0))
    label = _make_chrono_label(chrono1)
    fps_clock = pygame.time.Clock()
    #chrono fin
    jeu=True
    game_close = False
    Sx=8
    Sy = 6
    vitesse = 1
    

    Sx_change = 0       
    Sy_change = 0

    snake_List = []
    
    Length_of_snake = 1

    orientation = "g"
    orientationq = "g"
    chrono = 0

    avant_queuex=0
    avant_queuey=0
    if Length_of_snake >1 :
        avant_queuex = snake_List[1][0]
        avant_queuex = snake_List[1][0]
    foodx = random.randint(4,13)
    foody = random.randint(5,10)
    poisonx = random.randint(4,13)
    poisony = random.randint(5,10)

    print(str(foodx))
    print(str(foody))

    
    while jeu:


        #chrono debut
        dt = fps_clock.tick(60)
        chrono1, label = update(chrono1, label, dt) 
    
        #chrono fin
        while game_close == True:
            ecran.blit(image, (0, 0))
            ecran.blit(score, (95,0 ))
            ecran.blit(chro, (480, 2))
            Dessin_damier()
            message("Perdu! Appuyer Q-Quitter ou R-Rejouer", red)
            Your_score(Length_of_snake - 1)
            #value = score_font.render("     : " + str(chrono), True, vert)
            #ecran.blit(value, [470, 2])

            #chrono debut

            ecran.blit(label, (520, 10))

            #chrono fin


            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        jeu = False
                        game_close = False
                    if event.key == pygame.K_r:
                        chrono=0
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
        
        
        if Sx < 1 or Sx >=16 or Sy < 1 or Sy >=12 :
            
            game_close = True
            pygame.mixer.music.load("perdre.mp3") ################################################################""
            pygame.mixer.music.play()

        Sx += Sx_change
        Sy += Sy_change

        ecran.blit(image, (0, 0))
        ecran.blit(score, (95,0 ))
        ecran.blit(chro, (480,0 ))
        #ecran.blit(jeux, (95, 60))
        Dessin_damier()
        Your_score(Length_of_snake - 1)
        #My_chrono(pygame.time.get_ticks()//1000)
        chrono = pygame.time.get_ticks()//1000
        pommerouge = pygame.image.load("pomme.png")
        ecran.blit(pommerouge, (95+foodx*30, 30+foody*30))

        #chrono debut

        ecran.blit(label, (520, 10))

        #chrono fin

        affichage_case(poisonx,poisony,"pommepoison.png")

        snake_Head = []
        snake_Head.append(Sx)
        snake_Head.append(Sy)
        snake_Head.append("gauche.png")
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        """ for x in range(Length_of_snake):
            if snake_List[x][0]==snake_Head[0] and snake_List[x][1]==snake_Head[1] and x!=Length_of_snake-1:
                if x == snake_Head:
                    pygame.mixer.music.load("perdre.mp3") ################################################################""
                    pygame.mixer.music.play()
                    game_close = True """
    
        for x in snake_List[:-1]:
            if x == snake_Head:
                pygame.mixer.music.load("perdre.mp3") ################################################################""
                pygame.mixer.music.play()
                game_close = True 
        #orientation queue debut
        if Length_of_snake == 2 :
            if orientation == "d" :
                orientationq = "d"
            elif orientation == "g" :
                orientationq = "g"
            if orientation == "h" :
                orientationq = "h"
            elif orientation == "b" :
                orientationq = "b"
        elif Length_of_snake >2 :
            if avant_queuex +1 == snake_List[1][0] :
                orientationq = "d"
                
            elif avant_queuex -1 == snake_List[1][0] :
                orientationq = "g"
                
            elif avant_queuey +1 == snake_List[1][1] :
                orientationq = "b"
                
            elif avant_queuey -1 == snake_List[1][1] :
                orientationq = "h"
        our_snake(snake_List,orientation,orientationq)
        affichage_serpent(snake_List)
        
        pygame.display.update()
        
        if Sx == foodx and Sy == foody:
            foodx = random.randint(4,13)
            foody = random.randint(5,10)
            pygame.mixer.music.load("mange1.mp3") #######################################################################################################
            pygame.mixer.music.play()
            Length_of_snake += 1
        
        if Length_of_snake >2 :
            avant_queuey = snake_List[1][1]
            avant_queuex = snake_List[1][0]
        #orientation queue fin
        if Sx == poisonx and Sy == poisony:
            #poisonx = random.randint(4,13)
            #poisony = random.randint(5,10)
            pygame.mixer.music.load("perdre.mp3") ################################################################""
            pygame.mixer.music.play()
            game_close=True
        if chrono % 7 == 0 :
            poisonx = random.randint(4,13)
            poisony = random.randint(5,10)
            """ if (Length_of_snake - 1) % 2 == 0:
                vitesse = Length_of_snake """
        
        clock.tick(vitesse)
    
    pygame.quit()
    quit()
gameLoop()