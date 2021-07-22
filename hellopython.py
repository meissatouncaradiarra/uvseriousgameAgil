#! /usr/bin/env python3
# -*- coding: utf-8 -*-



import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((700, 450))
image = pygame.image.load("maquette2.png").convert_alpha()
serpent = pygame.image.load("serpent.png").convert_alpha()
ecran.blit(image, (0, 0))

Sx=8
Sy=6
#ecran.blit(serpent, (95+Sx*30, 30+Sy*30))

jeu = True
while jeu:
    ecran.blit(serpent, (95+Sx*30, 30+Sy*30))
    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                perso_x = event.pos[0] - 15
                perso_y = event.pos[1] - 15

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if Sy >= 10:
                    Sy -= 1
            if event.key == K_DOWN:
                if Sy <= 160:
                    Sy += 1
            if event.key == K_LEFT:
                if Sx >= 10:
                    Sx -= 1
            if event.key == K_RIGHT:
                if Sx <= 160:
                    Sx += 1

        
        
            
    pygame.display.flip()
    if event.type == QUIT:
            jeu = False