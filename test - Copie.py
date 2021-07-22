import pygame
from pygame.locals import *
 
pygame.init()
 
#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((700, 450))
 
#Chargement et collage du fond
fond = pygame.image.load("gazon.jpg").convert()
fenetre.blit(fond, (0,0))
 
#Chargement et collage du personnage
perso = pygame.image.load("serpent_d.png").convert_alpha()
perso_x = 335
perso_y = 210
#fenetre.blit(perso, (perso_x,perso_y))
 
#Rafraîchissement de l'écran
pygame.display.flip()
 
#BOUCLE INFINIE
continuer = 1
while continuer:
    fenetre.blit(perso, (perso_x,perso_y))
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT: # or (event.type == KEYDOWN and event.key == K_ESCAPE):
            continuer = 0
 
        
 
        if event.type == KEYDOWN:
 
            if event.key == K_UP:
                if perso_y >= 10:
                    perso = pygame.image.load("serpent_h.png").convert_alpha()
                    perso_y -= 10
 
            if event.key == K_DOWN:
                if perso_y <= 415:
                    perso = pygame.image.load("serpent_b.png").convert_alpha()
                    perso_y += 10
 
            if event.key == K_LEFT:
                if perso_x >= 6:
                    perso = pygame.image.load("serpent_g.png").convert_alpha()
                    perso_x -= 10
 
            if event.key == K_RIGHT:
                if perso_x <= 660:
                    perso = pygame.image.load("serpent_d.png").convert_alpha()
                    perso_x += 10
 
 
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (perso_x, perso_y))
    #Rafraichissements
    pygame.display.flip()
