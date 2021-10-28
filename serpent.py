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


def our_snake(snake_list,orientation,orientationq):

    if len(snake_list)==1 :
        if orientation=="g" :
            serpent = pygame.image.load("gauche.png")
            ecran.blit(serpent, (95+snake_list[0][0]*30, 30+snake_list[0][1]*30))
        if orientation=="d" :
            serpent = pygame.image.load("droite.png")
            ecran.blit(serpent, (95+snake_list[0][0]*30, 30+snake_list[0][1]*30))
        if orientation=="h" :
            serpent = pygame.image.load("tetehaut.png")
            ecran.blit(serpent, (95+snake_list[0][0]*30, 30+snake_list[0][1]*30))
        if orientation=="b" :
            serpent = pygame.image.load("bas.png")
            ecran.blit(serpent, (95+snake_list[0][0]*30, 30+snake_list[0][1]*30))
    else :
        for x in range(len(snake_list)):
            
            if orientation=="g" :
                if x==len(snake_list)-1:
                    serpent = pygame.image.load("gauche.png")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                elif x==0 :
                    if(orientationq=="g") :
                        serpent = pygame.image.load("queued.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="d") :
                        serpent = pygame.image.load("queueg.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="h") :
                        serpent = pygame.image.load("queueb.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="b") :
                        serpent = pygame.image.load("queueh.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                else :
                    serpent = pygame.image.load("corps.jpg")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
            elif orientation=="d" :
                if x==len(snake_list)-1:
                    serpent = pygame.image.load("droite.png")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                elif x==0 :
                    if(orientationq=="g") :
                        serpent = pygame.image.load("queued.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="d") :
                        serpent = pygame.image.load("queueg.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="h") :
                        serpent = pygame.image.load("queueb.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="b") :
                        serpent = pygame.image.load("queueh.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                else :
                    serpent = pygame.image.load("corps.jpg")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
            if orientation=="h":
                if x==len(snake_list)-1:
                    serpent = pygame.image.load("tetehaut.png")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                elif x==0 :
                    if(orientationq=="g") :
                        serpent = pygame.image.load("queued.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="d") :
                        serpent = pygame.image.load("queueg.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="h") :
                        serpent = pygame.image.load("queueb.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="b") :
                        serpent = pygame.image.load("queueh.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                else :
                    serpent = pygame.image.load("corps.jpg")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
            elif orientation=="b" :
                if x==len(snake_list)-1:
                    serpent = pygame.image.load("bas.png")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                elif x==0 :
                    if(orientationq=="g") :
                        serpent = pygame.image.load("queued.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="d") :
                        serpent = pygame.image.load("queueg.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="h") :
                        serpent = pygame.image.load("queueb.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                    elif(orientationq=="b") :
                        serpent = pygame.image.load("queueh.png")
                        ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
                else :
                    serpent = pygame.image.load("corps.jpg")
                    ecran.blit(serpent, (95+snake_list[x][0]*30, 30+snake_list[x][1]*30))
 
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
                    carre = pygame.image.load("carre1.png")
                    ecran.blit(carre, (95+j*30, 30+i*30))
                else:
                    carre = pygame.image.load("carre2.png")
                    ecran.blit(carre, (95+j*30, 30+i*30))
        else:
            for j in range(17):
                if (j % 2) == 0:
                    carre = pygame.image.load("carre2.png")
                    ecran.blit(carre, (95+j*30, 30+i*30))
                else:
                    carre = pygame.image.load("carre1.png")
                    ecran.blit(carre, (95+j*30, 30+i*30))

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
            message("Perdu! Appuyer Q-Quitter ou C-Rejouer", red)
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
                    if event.key == pygame.K_c:
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

        pommenoire= pygame.image.load("pommepoison.png")
        ecran.blit(pommenoire, (95+poisonx*30, 30+poisony*30))

        snake_Head = []
        snake_Head.append(Sx)
        snake_Head.append(Sy)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
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