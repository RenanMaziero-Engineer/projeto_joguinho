#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Const import MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self,):
        pygame.init() #inicializa o pygame.
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #cria uma janela com width = 800 e heigth = 500.

    def run(self, ):
        while True: #manter janela em loop.
            #chama o menu.
            menu = Menu(self.window)
            menu_return = menu.run()# executa o menu.
            
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:# traz a opçãos do menu.
                level = Level(self.window, 'level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[4]:# traz a opção 4 do menu e fecha o jogo.
                pygame.quit()
                quit() 
            else:
                pass 
            
            
                    