import pygame

pygame.init() # inicia todas as var e eventos do pygame

window = pygame.display.set_mode((1280,720)) #janela do pygame
pygame.display.set_caption('First Game') #nome para janela

x = 720/2
y = 0

relogio = pygame.time.Clock()

while True: #loop da janela
    relogio.tick(30)
    window.fill((0,0,0))
    for event in pygame.event.get(): #loop dos comandos e eventos
        if event.type == pygame.QUIT:
            pygame.quit() # coondição para quando o player clicar no x da janela e fechar 100% o jogo
            


        pygame.draw.rect(window, (0,0,255), (x, y, 40, 50))
        if y >= 1280:
            y = 0
        y += 5

        pygame.display.update() #a cada atualização do loop principal, ela atualiza a tela do jogo
