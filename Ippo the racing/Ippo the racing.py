import random
from time import sleep

import pygame

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#classe Pista e todas definições associada a ela
class Pista:
    def __init__(self):
        self.bgImg = pygame.image.load("Rua.jpg")
        videoinfo = pygame.display.Info() 
        self.bg_x1 = (videoinfo.current_w / 2) - (360 / 2)
        self.bg_x2 = (videoinfo.current_w / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 5
        self.count = 0
        
    def atualiza(self):
        self.count += 1
        self.bg_speed += 1  

        
    def desenha(self,tela):
        tela.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        tela.blit(self.bgImg, (self.bg_x2, self.bg_y2))
        self.highscore(tela)
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed
        videoinfo = pygame.display.Info()  #  se fossse pygame 2.0 tinha soluçao melhor
        if self.bg_y1 >= videoinfo.current_h:
            self.bg_y1 -= 2*videoinfo.current_h
        if self.bg_y2 >= videoinfo.current_h:
            self.bg_y2 -= 2*videoinfo.current_h
    
    def display_message(self,tela, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, RED)
        tela.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit(tela)
    
    def highscore(self,tela):
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Score : " + str(self.count), True, WHITE)
        tela.blit(text, (5,5))
    
    def display_credit(self,tela):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Obrigado por jogar!", True, WHITE)
        tela.blit(text, (600, 520))        
        
#classe carro (do jogador) e todas as definições associadas a ele.    
class Carro:
    def __init__(self):
        image = 'Carro.png'
        self.carImg = pygame.image.load( image)
        self.car_speed = 0
        videoinfo = pygame.display.Info() 
        self.car_x = videoinfo.current_w * 0.45
        self.car_y = videoinfo.current_h * 0.8
        self.car_width = 49
        self.car_height = 100

    def desenha(self, display):
        display.blit(self.carImg, (self.car_x, self.car_y))

    def colidiu(self,outroCarro):
        crashed = False
        if self.car_y < outroCarro.car_y + outroCarro.car_height:
            if self.car_x > outroCarro.car_x and self.car_x < outroCarro.car_x + outroCarro.car_width or self.car_x + self.car_width > outroCarro.car_x and self.car_x + self.car_width < outroCarro.car_x + outroCarro.car_width:
                crashed = True
        if self.car_x < 290 or self.car_x > 460:
            crashed = True
        return crashed
    
#classe Adversário e todas as definições assocaidos a ele.       
class Adversario:
    def __init__(self):
        image = 'Pedra.png'
        self.carImg = pygame.image.load( image)
        self.car_speed = 10
        self.car_x = random.randrange(310, 450)
        self.car_y = -600
        self.car_width = 49
        self.car_height = 100
  
    def desenha(self, display):
        display.blit(self.carImg, (self.car_x, self.car_y))
        
    def atualiza(self):
        self.car_y += self.car_speed
        if self.passou():
            self.car_speed += 1
            return True
        return False

    def passou(self):
        videoinfo = pygame.display.Info() 
        if self.car_y > videoinfo.current_h:
            self.car_y = 0 - self.car_height
            self.car_x = random.randrange(310, 450)
            return  True
        return False
