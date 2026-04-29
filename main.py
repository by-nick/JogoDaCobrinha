import pygame
from pygame import K_a, K_s, K_d, K_w
from random import randint

pygame.init() # inicia todas as var e eventos do pygame

xInimigo = randint(40,600)
yInimigo = randint(50,430)

window = pygame.display.set_mode((1280,720)) #janela do pygame
pygame.display.set_caption('First Game') #nome para janela

x = 1280/2
y = 720/2

relogio = pygame.time.Clock()

while True: #loop da janela
    relogio.tick(30)
    window.fill((0,0,0))
    for event in pygame.event.get(): #loop dos comandos e eventos
        if event.type == pygame.QUIT:
            pygame.quit() # coondição para quando o player clicar no x da janela e fechar 100% o jogo
            exit()
            
    '''if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 20 
            elif event.key == pygame.K_s:
                y += 20
            elif event.key == pygame.K_d:
                x += 20
            elif event.key == pygame.K_w:
                y -=20
            '''
            
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        x -= 20
    elif teclas[pygame.K_s]:
        y += 20
    elif teclas[pygame.K_d]:
        x += 20
    elif teclas[pygame.K_w]:
        y -=20
        
        
    player = pygame.draw.rect(window, (0,0,255), (x, y, 40, 50))
    inimigo = pygame.draw.rect(window, (255, 0, 0), (xInimigo,yInimigo,40,50))
    
    if player.colliderect(inimigo):
        xInimigo = randint(40,600)
        yInimigo = randint(50,430)

    pygame.display.update() #a cada atualização do loop principal, ela atualiza a tela do jogo
