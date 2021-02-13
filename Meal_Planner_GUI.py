#~~~~~ Meal Planner GUI ~~~~~#

import pygame
from time import sleep
from Meal_Planner import reverseBoolean

def MPGUImain():
    pygame.init()
    display = pygame.display.set_mode((950,601))
    pygame.display.set_caption("Meal Planner")

    version = "1.0.0"
    daysOfWeek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    running = True
    inMain = True
    outMain = False

    darkGrey = (61,57,58,255)     # background
    semiDarkGrey = (70,66,67,255)     # button colour
    grey = (87,86,86,255)     # button colour outline
    lightPurple = (156,105,224,255)     # button colour hover
    purple = (116,75,172,255)     # button colour pressed
    orange = (249,116,95,255)     # line colour
    lightGrey = (213,212,212,255)     # text colour

    text1 = pygame.font.SysFont('verdana',50)     # meal planner text
    text2 = pygame.font.SysFont('verdana',22)     # info text

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mousePos = pygame.mouse.get_pos()
        display.fill(darkGrey)

        display.blit(text1.render("Meal Planner",False,lightGrey),(20,0))     # draws main meal planner text in top left
        display.blit(text2.render("version",False,lightGrey),(363,5))     # version text
        display.blit(text2.render(version,False,orange),(448,5))     # version text
        display.blit(text2.render("Mattyou Quinn",False,lightGrey),(352,28))     # author credit lol

        pygame.draw.rect(display,semiDarkGrey,(520,20,400,525),border_radius=4)     # meal plan week background
        pygame.draw.rect(display,purple,(520,20,400,525),border_radius=4,width=3)     # meal plan week outline

        for i in range(3):     # new meal idea, random meal idea, try something new boxes
            pygame.draw.rect(display,semiDarkGrey,(20,70*i+80,480,60),border_radius=8)
            pygame.draw.rect(display,grey,(20,70*i+80,480,60),border_radius=8,width=2)
            
            if (20) < mousePos[0] < (500) and (70*i+80) < mousePos[1] < (70*i+140):
                pygame.draw.rect(display,lightPurple,(20,70*i+80,480,60),border_radius=8)
                pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8,width=2)

        pygame.display.flip()
        sleep(0.082)

    pygame.quit()    

MPGUImain()
