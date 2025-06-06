#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import WIN_WIDTH, WIN_HEIGTH
from code.menu import Menu
import pygame
class Game:
    def __init__(self,):
        pygame.init() #inicializa o pygame.
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGTH)) #cria uma janela com width = 800 e heigth = 500.

    def run(self, ):
        while True: #manter janela em loop.
            #chama o menu.
            menu = Menu(self.window)
            menu.run()
            
            
            
                    