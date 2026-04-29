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
xmaca = randint(40,600)  
ymaca = randint(50,430)

#var para importar fonte usando biblioteca do pygame 
fonte = pygame.font.SysFont('Arial', 40, True, True)

window = pygame.display.set_mode((1280,720)) #janela do pygame
pygame.display.set_caption('First Game') #nome para janela

#local onde o player irar spawnar (no meio da tela)
xplayer = 1280/2 
yplayer = 720/2

pontos = 0 #var para os pontos
relogio = pygame.time.Clock()#var para o fps
listaPlayer = []

#função para aumentar o tamanho da cobra enquanto ela come a maçã
def tamanhoPlayer(listaPlayer):
    #para a posição x e y na lista player
    for XeY in listaPlayer:
        #ele desenha uma um bloco verde atras da cobra
        pygame.draw.rect(window, (0,255,0), (XeY[0], XeY[1], 20,20) )

#loop da janela
while True:
    relogio.tick(20) #fps do jogo
    window.fill((255,255,255)) #limpeza da tela
    mensagem = f'Pontos: {pontos}' #mensagem que será escrita no canto da tela
    juntandoTexto = fonte.render(mensagem, False, (0,0,0))
    
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
        xplayer -= 20
    elif teclas[pygame.K_s]:
        yplayer += 20
    elif teclas[pygame.K_d]:
        xplayer += 20
    elif teclas[pygame.K_w]:
        yplayer -=20
        
    #retangulo do player (azul)    
    player = pygame.draw.rect(window, (0,255,0), (xplayer, yplayer, 20, 20))
    
    #retangulo do inimigo (vermelho)
    maca = pygame.draw.rect(window, (255, 0, 0), (xmaca,ymaca,20,20)) 
    
    #sistema de colisão
    if player.colliderect(maca):
        #ao colidir o retangulo do inimigo muda para um lugar aleatorio da janela no intervalo descrito em x e y
        xmaca = randint(40,600) 
        ymaca = randint(50,430)
        
        #incremento dos pontos
        pontos += 1
        colatagem.play()
    
    #listas para armazenar valores 
    #lista da cabeça, armazenando valores x e y, ja que a cobra coleta as maçãs com a cabeça
    listaCabeca = []
    listaCabeca.append(xplayer)
    listaCabeca.append(yplayer)
    
    #lista do player pegando os valores armazenados na cabeça de cada maçã que ela coletou
    listaPlayer.append(listaCabeca)
    
    #chamando a função e anexando o parametro da lista da cobra
    tamanhoPlayer(listaPlayer)

    #faz a mensagem de pontos aparecer na tela
    window.blit(juntandoTexto, (450,40))
    pygame.display.update() #a cada atualização do loop principal, ela atualiza a tela do jogo
