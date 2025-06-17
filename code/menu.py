#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.const import COLOR_ORANGE
from code.const import WIN_WIDTH
from code.const import MENU_OPTION
from code.const import COLOR_WHITE
from code.const import COLOR_YELLOW

class Menu:
    #construtor da classe.
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()#carrega a imagem do jogo.
        self.rect = self.surf.get_rect(left=0,top=0)#cria o retangulo da tela.
    def run(self, ):
        menu_option = 0
        #toca musica no game.
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)#(-1) faz a musica tocar sem parar.
        
        while True:    
            self.window.blit(source=self.surf, dest=self.rect)
            #define os textos da tela.
            self.menu_text(50, "Mountain",COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter",COLOR_ORANGE, ((WIN_WIDTH / 2), 120))
            #cria um loop para pegar os textos que estão em MENU_OPTION e adicionar na tela e dar características.
            for i in range(len(MENU_OPTION)):
                if i == menu_option: 
                    self.menu_text(30, MENU_OPTION[i],COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i],COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))
            
            pygame.display.flip()

            #checa eventos.
            for event in pygame.event.get(): #pega todos os eventos que acontecem na tela(expl: click, fechar, diminuir etc...)
                if event.type == pygame.QUIT: # se o evento for igual a fechar ->
                    pygame.quit() # fecha a janela.
                    quit() #fecha.
                
                if event.type == pygame.KEYDOWN:# se for o evento de tecla precssionada.
                    if event.key == pygame.K_DOWN:# se for o evento de tecla par baixo.
                        if menu_option < len(MENU_OPTION) - 1:# enquanto menu_option for menor que o tamanho do MENU.
                            menu_option += 1                  #incrementa +1.
                        else: 
                            menu_option = 0                   # se for maior que o tamanho do MENU ele volta para o lemento na posição 1.
                    
                    if event.key == pygame.K_UP:# se for o evento de tecla para cima.
                        if menu_option > 0:     # enquanto menu_option for maior que 0.
                            menu_option -= 1    # descrementa 1. tira 1.
                        else: 
                            menu_option = len(MENU_OPTION) - 1  # se for menor que 0 ele volta para o ultimo elemento do MENU.
                    
                    if event.key == pygame.K_RETURN: # tecla ENTER.
                        return MENU_OPTION[menu_option]
                
           
    
    #função que adiciona e cracteriza a imagem.               
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typerwriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() 
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)