#Setup de Entrada - Import Bibliotecas-----------------------------------------#
import pygame, sys

#Setup de Entrada - Definições --------------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Tela de Entrada')
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))


font = pygame.font.SysFont(None, 30)

#As imagens
imageinicial = pygame.image.load("telainicial.jpg")
imageinicial_rect = imageinicial.get_rect()
opcao = pygame.image.load("opcao.jpg")
opcao_rect = opcao.get_rect()



pygame.mixer.music.set_volume(0.50)
pygame.mixer.music.load("Dragonball.mp3")
pygame.mixer.music.play(-1)




#Definição de Escrita de Texto-------------------------------------------------#
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

#Definição de ações do Menu Inicial--------------------------------------------#
def main_menu():
    while True:
        screen.blit(imageinicial, imageinicial_rect)

        

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 300, 200, 50)
        button_3 = pygame.Rect(300, 400, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                exite()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Jogar', font, (255, 255, 255), screen, 372, 215)
        draw_text('Opções', font, (255, 255, 255), screen, 363, 315)
        draw_text('Sair', font, (255, 255, 255), screen, 378, 415)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
        
#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def game():
    running = True
    while running:
        screen.blit(imageinicial, imageinicial_rect)
        
        draw_text('Meu Jogo', font, (0, 0, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def options():
    running = True
    while running:
        screen.blit(opcao, opcao_rect)
        
        
        draw_text('Opções', font, (0, 0, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.display.update()
        mainClock.tick(60)

def exite():
    pygame.quit()
    sys.exit()

           
main_menu()