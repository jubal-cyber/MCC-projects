#Developed a simple ball motion animation using Python and Pygame with adjustable speed and interactive controls.
import pygame, sys
#to star pygame
pygame.init()
s = pygame.display.set_mode((400,400))

y = 200
v = int(input("Enter the velocity of the ball: "))
#for continuos run
while True:
    s.fill((45,223,255))#45, 223, 255
    pygame.draw.circle(s, (227,60,199), (200,y), 30)#RGB: (227, 60, 199)
#4 vertical movement
    y += v
    if y > 370 or y < 30:
        v = -v

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()


