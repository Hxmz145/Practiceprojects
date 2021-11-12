import pygame
import random
from random import randrange
pygame.init()
starter = False
VEL = 10

pressed = pygame.key.get_pressed()
WHITE = (255,255,255)
RED = (252,0,0)
GREEN = (0,255,9)
BLUE = (0,68,255)

pygame.init()
WINDOW = screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption("Piano of COLORS")
clock = pygame.time.Clock()






color1 = random.randint(0,255)
color2 = random.randint(0,255)
color3 = random.randint(0,255)
COLORS1 = [color1,color2,color3]
test_surface = pygame.Surface((100,200))
test_surface.fill(WHITE)
color12 = random.randint(0,255)
color22 = random.randint(0,255)
color23 = random.randint(0,255)
COLORS2 = [color12,color22,color23]
test_surface2 = pygame.Surface((100,200))
test_surface2.fill(WHITE)
color21 = random.randint(0,255)
color25 = random.randint(0,255)
color39 = random.randint(0,255)
COLORS3 = [color21,color25,color39]
test_surface3 = pygame.Surface((100,200))
test_surface3.fill(WHITE)
color31 = random.randint(0,255)
color32 = random.randint(0,255)
color33 = random.randint(0,255)
COLORS4 = [color31,color32,color33]
test_surface4 = pygame.Surface((100,200))
test_surface4.fill(WHITE)
color41 = random.randint(0,255)
color42 = random.randint(0,255)
color43 = random.randint(0,255)
COLORS5 = [color41,color42,color43]
test_surface5 = pygame.Surface((100,200))
test_surface5.fill(WHITE)

screen.blit(test_surface,(0,0))
screen.blit(test_surface2,(200,0))
screen.blit(test_surface3,(400,0))
screen.blit(test_surface4,(600,0))
screen.blit(test_surface5,(800,0))



Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            test_surface2.fill(COLORS1)
            screen.blit(test_surface2,(200,100))
#Controls are a,s,d,f,g
        if pressed[pygame.K_s]:
            test_surface.fill(COLORS2)
            screen.blit(test_surface,(0,100))
        if pressed[pygame.K_d]:
            test_surface3.fill(COLORS3)
            screen.blit(test_surface3,(400,100))
        if pressed[pygame.K_f]:
            test_surface4.fill(COLORS4)
            screen.blit(test_surface4,(600,100))
        if pressed[pygame.K_g]:
            test_surface5.fill(COLORS5)
            screen.blit(test_surface5,(800,100))

    pygame.display.update()
    clock.tick(500)
pygame.quit()
