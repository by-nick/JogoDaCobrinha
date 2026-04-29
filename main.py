import pygame
from pygame import K_a, K_s, K_d, K_w
from random import randint

pygame.init() # inicia todas as var e eventos do pygame

#método para abaixar o som da musica, valores entre 0 e 1
pygame.mixer.music.set_volume(0.4)
#var para carregar musica
musicaFundo = pygame.mixer.music.load('musicas/BoxCat Games - CPU Talk.mp3')
#da play na musica e toca repetidas vezes por conta do -1
pygame.mixer.music.play(-1)

#som para a coleta de pontos
colatagem = pygame.mixer.Sound('musicas/smw_coin.wav')

# valores pre determinados da var do inimigo para que ele respawne em lugar alaetorio no mapa
xInimigo = randint(40,600)  
yInimigo = randint(50,430)

#var para importar fonte usando biblioteca do pygame 
fonte = pygame.font.SysFont('Arial', 40, True, True)

window = pygame.display.set_mode((1280,720)) #janela do pygame
pygame.display.set_caption('First Game') #nome para janela

#local onde o player irar spawnar (no meio da tela)
x = 1280/2 
y = 720/2

pontos = 0 #var para os pontos
relogio = pygame.time.Clock()#var para o fps

#loop da janela
while True:
    relogio.tick(30) #fps do jogo
    window.fill((0,0,0)) #limpeza da tela
    mensagem = f'Pontos: {pontos}' #mensagem que será escrita no canto da tela
    juntandoTexto = fonte.render(mensagem, False, (255,255,255))
    
    for event in pygame.event.get(): #loop dos comandos e eventos
        if event.type == pygame.QUIT:
            # coondição para quando o player clicar no x da janela e fechar 100% o jogo
            pygame.quit() 
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
    
    #codigo para o computador ver se tem alguma tecla pressionada e realizar determinada ação
    teclas = pygame.key.get_pressed() 

    if teclas[pygame.K_a]:
        x -= 20
    elif teclas[pygame.K_s]:
        y += 20
    elif teclas[pygame.K_d]:
        x += 20
    elif teclas[pygame.K_w]:
        y -=20
        
    #retangulo do player (azul)    
    player = pygame.draw.rect(window, (0,0,255), (x, y, 40, 50))
    
    #retangulo do inimigo (vermelho)
    inimigo = pygame.draw.rect(window, (255, 0, 0), (xInimigo,yInimigo,40,50)) 
    
    #sistema de colisão
    if player.colliderect(inimigo):
        #ao colidir o retangulo do inimigo muda para um lugar aleatorio da janela no intervalo descrito em x e y
        xInimigo = randint(40,600) 
        yInimigo = randint(50,430)
        
        #incremento dos pontos
        pontos += 1
        colatagem.play()

    window.blit(juntandoTexto, (450,40))
    pygame.display.update() #a cada atualização do loop principal, ela atualiza a tela do jogo
