import pygame

#inicializa o pygame.
pygame.init()

#criar janela.
window = pygame.display.set_mode(size=(800, 500))
#loop para manter a janela aberta.
while True:
    for event in pygame.event.get():
        #fecha janela.
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
       
