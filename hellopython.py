#! /usr/bin/env python3
# -*- coding: utf-8 -*-



import pygame
from pygame.locals import *
from datetime import timedelta, datetime, date, time
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

pygame.init()

ecran = pygame.display.set_mode((700, 450))
image = pygame.image.load("maquette2.png").convert_alpha()
serpent = pygame.image.load("serpent.jpg").convert_alpha()
font = pygame.font.Font(None, 25)
chrono = datetime.combine(date.today(), time(0, 0))
label = _make_chrono_label(chrono)
fps_clock = pygame.time.Clock()
#ecran.blit(image, (0, 0))
Sx=8
Sy=6
jeu = True
def new_func():
    jeu = False
while jeu:
    ecran.blit(image, (0, 0))
    ecran.blit(serpent, (95+Sx*30, 30+Sy*30))
    dt = fps_clock.tick(60)
    chrono, label = update(chrono, label, dt) 
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_DOWN :
                Sy+=1
            elif event.key == K_UP :
                Sy-=1 
            elif event.key == K_RIGHT :
                Sx+=1
            elif event.key== K_LEFT:
                Sx-=1
            if event.key == K_SPACE:
                jeu = False
                print("Fermer la fenetre")
    #print(Sx)
    ecran.blit(label, (520, 10))
    if Sx == 0 or Sx == 17:
        jeu = False
    elif Sy == 0 or Sy== 13:
        jeu = False 
    
    pygame.display.flip()
    























"""pygame.init()
clock = pygame.time.Clock()

CIEL = 0, 200, 255
ORANGE = 255, 100, 0

def main():
    fenetre = pygame.display.set_mode((699, 467))

    loop = True
    while loop:
        background = pygame.Surface(fenetre.get_size())
        background.fill(CIEL)

        # Définition de la police
        bigText = pygame.font.SysFont('freesans', 36)

        # Définition du texte
        # render(text, antialias, rgb color tuple)
        title_text = bigText.render("Moustapha SOKHNA",True, ORANGE)
        # Position: horizontal au centre , vertical = 50
        # Le centre du texte est au centre quelque soit le texte
        # Le texte est inscrit dans un rectangle
        textpos = title_text.get_rect()
        # Placement du texte en x et y
        textpos.centerx = fenetre.get_rect().centerx
        textpos.centery = 50

        # Collage du texte sur le fond
        background.blit(title_text, textpos)

        # Ajout du fond dans la fenêtre
        fenetre.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # Actualisation de l'affichage
        pygame.display.flip()
        # 10 fps
        clock.tick(10)

if __name__ == '__main__':
    main()"""