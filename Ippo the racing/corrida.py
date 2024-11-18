from CarRacing  import *
import time
import pygame

import random

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH, HEIGHT = (800,600)
FPS = 30

pygame.init()
pygame.mixer.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game da Corrida")
clock = pygame.time.Clock()

Sound = pygame.mixer.music.load("Manuel.mp3")
Sound = pygame.mixer.music.play(-1)

RED = (255, 0, 0)


# declaração dos objetos
carro = Carro()
adversario = Adversario()
pista = Pista()

#loop do jogo
crashed = False
quit = False
while not quit:    
    # inicializações
    crashed = False
    adversario.car_x = random.randrange(300, 450)
    adversario.car_y = -600
    carro.car_x = 350
    pista.count = 0
    adversario.car_speed = 10
    pista.bg_speed = 5    
    while not crashed and not quit:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True       
            # Movimentos do carro com as teclas Direita/Esquerda
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT):
                    carro.car_x -= 50
                if (event.key == pygame.K_RIGHT):
                    carro.car_x += 50
                print ("x: {x}, y: {y}".format(x=carro.car_x, y=carro.car_y))
        tela.fill(BLACK)
        pista.desenha(tela)
        adversario.desenha(tela)
        adversarioPassou = adversario.atualiza()
        carro.desenha(tela)           
        if adversarioPassou:
                pista.atualiza()
        # check  de colisão entre carros
        crashed =  carro.colidiu(adversario)
        if crashed:
            pista.display_message(tela,"Game Over !!!")   
        pygame.display.update()
        pygame.display.flip()          
    time.sleep(2)

    
pygame.quit()
