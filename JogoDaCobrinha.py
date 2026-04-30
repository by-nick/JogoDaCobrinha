import pygame
from pygame import K_a, K_s, K_d, K_w, K_r
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

#velocidade de moviemnto da cobra
velocidade = 10

#controles de x e y no teclado 
xCont = velocidade
yCont = 0

pontos = 0 #var para os pontos
relogio = pygame.time.Clock()#var para o fps
listaPlayer = [] #lista que do player 
tamInicial = 5 # tamanho predefinido do player, tamanho inicial
morreu = False

#função para aumentar o tamanho da cobra enquanto ela come a maçã
def tamanhoPlayer(listaPlayer):
    #para a posição x e y na lista player
    for XeY in listaPlayer:
        #ele desenha uma um bloco verde atras da cobra
        pygame.draw.rect(window, (0,255,0), (XeY[0], XeY[1], 20,20) )
 
 
#função para reiniciar jogo apos morrer       
def reiniciar():
    #tornando as var globais dentro da função
    global pontos, tamInicial, xplayer, yplayer, listaPlayer, listaCabeca, xmaca, ymaca, morreu
   
    #redefinindo os valores iniciais das var apos morrer
    pontos = 0
    tamInicial = 5
    xplayer = 1280/2 
    yplayer = 720/2
    listaPlayer = []
    listaCabeca = []
    xmaca = randint(40,600)  
    ymaca = randint(50,430)
    morreu = False


#loop da janela
while True:
    relogio.tick(30) #fps do jogo
    window.fill((255,255,255)) #limpeza da tela
    mensagem = f'Pontos: {pontos}' #mensagem que será escrita no canto da tela
    juntandoTexto = fonte.render(mensagem, False, (0,0,0))
    
    for event in pygame.event.get(): #loop dos comandos e eventos
        if event.type == pygame.QUIT:
            # coondição para quando o player clicar no x da janela e fechar 100% o jogo
            pygame.quit() 
            exit()
    
        # para que a cobra cobtinue com o seu tamanho ao parar de pressionar a tecla de movimento        
        if event.type == pygame.KEYDOWN:
                if event.key == K_a:
                    # se eu apertar para ir para a esquerda e a minha var esta com valor positivo (para direita), ela vai bloquear o botao
                    if xCont == velocidade:
                        pass
                    else:
                        xCont = -velocidade
                        #necessário zerar o x ou o y para que ela nao se movimente na diagonal 
                        yCont = 0
                elif event.key == K_s:  
                    if yCont == -velocidade:
                        pass
                    else:
                        yCont = velocidade
                        xCont = 0
                elif event.key == K_d:
                    if xCont == -velocidade:
                        pass
                    else:
                        xCont = velocidade
                        yCont = 0
                elif event.key == K_w:
                    if yCont == velocidade:
                        pass
                    else:
                        yCont =- velocidade
                        xCont = 0
    
    xplayer += xCont
    yplayer += yCont    


    #codigo para o computador ver se tem alguma tecla pressionada e realizar determinada ação
    '''teclas = pygame.key.get_pressed() 

    if teclas[pygame.K_a]:
        xCont -=velocidade
        yCont = 0
    elif teclas[pygame.K_s]:
        yCont = velocidade
        xCont = 0
    elif teclas[pygame.K_d]:
        xCont = velocidade
        yCont = 0
    elif teclas[pygame.K_w]:
        yCont = velocidade
        xCont = 0
    '''
    
    
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
        tamInicial += 1
    
    #listas para armazenar valores 
    #lista da cabeça, armazenando valores x e y, ja que a cobra coleta as maçãs com a cabeça
    listaCabeca = []
    listaCabeca.append(xplayer)
    listaCabeca.append(yplayer)
    
    #se o tamanho do player for maior que o tamanho definido inicial
    if len(listaPlayer) > tamInicial:
        #deletará a coleta mais antiga 
        del listaPlayer[0]
    
    #lista do player pegando os valores armazenados na cabeça de cada maçã que ela coletou
    listaPlayer.append(listaCabeca)
    
    #se a lista cabeça tiver o mesmo valor que lista player
    if listaPlayer.count(listaCabeca) > 1:
        #adicionando mensagem para reiniciar
        fonte2 = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Você perdeu! Pressione R para jogar novamente'
        juntandoTexto = fonte2.render(mensagem, True, (255, 0, 0))
        
        #pega o centro do retangulo que fica ao redor da mensagem, ou seja, a tela branca
        retTexto = juntandoTexto.get_rect()
        #a var morreu passa a ser veidadeiro
        morreu = True
        #enquanto morreu for verdadeiro
        while morreu:
            #ao morrer a tela ficar 100% branca
            window.fill((255,255,255))
            #inicializará o evento do botão de reiniciair
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_r:
                        reiniciar()
                        
            #e adiciona no meio da tela utilizando sua largura e altura origial descrito no código           
            retTexto.center = (1280//2, 720//2)            
            #exibe a mensagem na tela branca de game over
            window.blit(juntandoTexto, retTexto)            
            #atualiza a tela para que fique branca            
            pygame.display.update()
            
    if xplayer > 1280:
        xplayer = 0
    elif xplayer < 0:
        xplayer = 1280
    elif yplayer < 0:
        yplayer = 720
    elif yplayer > 720:
        yplayer = 0
    
    #chamando a função e anexando o parametro da lista da cobra
    tamanhoPlayer(listaPlayer)

    #faz a mensagem de pontos aparecer na tela
    window.blit(juntandoTexto, (450,40))
    pygame.display.update() #a cada atualização do loop principal, ela atualiza a tela do jogo
