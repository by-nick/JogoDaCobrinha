import pygame

pygame.init() # inicia todas as var e eventos do pygame

window = pygame.display.set_mode((1280,720)) #janela do pygame
pygame.display.set_caption('First Game') #nome para janela

while True: #loop da janela
    for event in pygame.event.get(): #loop dos comandos e eventos
        if event.type == pygame.QUIT:
            pygame.quit() # coondição para quando o player clicar no x da janela e fechar 100% o jogo
        

        pygame.draw.rect(window, (0,0,255), (200, 300, 40, 50))
        pygame.draw.circle(window, (255, 0, 0), (400, 200), 40)
        pygame.draw.line(window, (255,255,0), )
        pygame.display.update() #a cada atualização do loop principal, ela atualiza a tela do jogo
