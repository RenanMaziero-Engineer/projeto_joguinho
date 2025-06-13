#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import COLOR_ORANGE
from code.const import WIN_WIDTH
from code.const import MENU_OPTION
from code.const import COLOR_WHITE

class Menu:
    #construtor da classe.
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')#carrega a imagem do jogo.
        self.rect = self.surf.get_rect(left=0,top=0)#cria o retangulo da tela.
    def run(self, ):
        #toca musica no game.
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)#(-1) faz a musica tocar sem parar.
        
        while True:    
            self.window.blit(source=self.surf, dest=self.rect)
            #define os textos da tela.
            self.menu_text(50, "Mountain",COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter",COLOR_WHITE, ((WIN_WIDTH / 2), 120))
            #cria um loop para pegar os textos que estão em MENU_OPTION e adicionar na tela e dar características.
            for i in range(len(MENU_OPTION)):
                self.menu_text(30, MENU_OPTION[i],COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            
            pygame.display.flip()

            #checa eventos.
            for event in pygame.event.get(): #pega todos os eventos que acontecem na tela(expl: click, fechar, diminuir etc...)
                if event.type == pygame.QUIT: # se o evento for igual a fechar ->
                    pygame.quit() # fecha a janela.
                    quit() #fecha.
    #função que adiciona e cracteriza a imagem.               
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typerwriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() 
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)