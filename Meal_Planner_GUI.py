#~~~~~ Meal Planner GUI ~~~~~#

import pygame
from time import sleep
from Meal_Output_Generator_Size import findSize
from Meal_Planner import getCurrentDate, getCurrentDay, generateNewRandomMeal

def MPGUImain():
    pygame.init()
    display = pygame.display.set_mode((950,611))
    pygame.display.set_caption("Meal Planner")

    version = "1.0.0"
    mealGeneratedOutput = ""
    date = getCurrentDate()
    day, ignore = getCurrentDay()
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
    red = (227,32,32,255)     # cross button

    text1 = pygame.font.SysFont('verdana',50)     # meal planner text
    text2 = pygame.font.SysFont('verdana',22)     # info text
    text3 = pygame.font.SysFont('verdana',26)     # "Meal:" text in meal generator output box and buttons at bottom of the screen
    text4 = pygame.font.SysFont('verdana',17)     # "Add..." text in meal generator output box
    text5 = pygame.font.SysFont('verdana',20)     # cross button and edit buttons
    text6 = pygame.font.SysFont('verdana',35)     # meal idea buttons and meal by day date text
    text7 = pygame.font.SysFont('verdana',30)     # days of the week font

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mousePos = pygame.mouse.get_pos()
        display.fill(darkGrey)

        ################################################################################
        ################################ left hand side ################################
        ################################################################################

        ################################ GUI info ################################

        display.blit(text1.render("Meal Planner",False,lightGrey),(20,0))     # draws main meal planner text in top left
        display.blit(text2.render("version",False,lightGrey),(363,5))     # version text
        display.blit(text2.render(version,False,orange),(448,5))     # version text
        display.blit(text2.render("Mattyou Quinn",False,lightGrey),(352,28))     # author credit lol
        

        ################################ meal idea buttons ################################

        for i in range(3):     # new meal idea, random meal idea, try something new boxes
            pygame.draw.rect(display,semiDarkGrey,(20,70*i+80,480,60),border_radius=8)
            pygame.draw.rect(display,grey,(20,70*i+80,480,60),border_radius=8,width=2)
            
            if (20) < mousePos[0] < (500) and (70*i+80) < mousePos[1] < (70*i+140):
                pygame.draw.rect(display,lightPurple,(20,70*i+80,480,60),border_radius=8)
                pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8,width=2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8)
                    pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8,width=2)

                    if i == 1:
                        mealGeneratedOutput = generateNewRandomMeal("Meals")

                    if i == 2:
                        mealGeneratedOutput = generateNewRandomMeal("New_Meals")

        display.blit(text6.render("New Meal Idea",False,lightGrey),(130,86))     # meal idea buttons text
        display.blit(text6.render("Random Meal Idea",False,lightGrey),(95,156))
        display.blit(text6.render("Try Something New",False,lightGrey),(86,226))
        

        ################################ meal output box ################################

        pygame.draw.rect(display,semiDarkGrey,(20,300,480,70),border_radius=5)     # meal generator output box background
        pygame.draw.rect(display,purple,(20,300,480,70),border_radius=5,width=2)     # meal generator output box outline
        display.blit(text3.render("Meal:",False,lightGrey),(28,303))
        
        if (28) < mousePos[0] < (96) and (336) < mousePos[1] < (364):     # "add..." button logic 
            pygame.draw.rect(display,grey,(28,336,68,28),border_radius=4)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(28,336,68,28),border_radius=4)
            
        pygame.draw.rect(display,orange,(28,336,68,28),border_radius=4,width=1)     # outline for the "Add..." button
        display.blit(text4.render("Add...",False,orange),(37,339))     # text for the "Add..." button
        
        if mealGeneratedOutput != "":     # displaying the meal generated
            x, y = findSize(len(list(mealGeneratedOutput)))
            mealOutputText = pygame.font.SysFont('verdana',x)
            display.blit(mealOutputText.render(mealGeneratedOutput,False,purple),(110,292+y))
            
        if (480) < mousePos[0] < (496) and (305) < mousePos[1] < (322):     # cross button logic
            pygame.draw.rect(display,grey,(481,306,14,15),border_radius=3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(481,306,14,15),border_radius=3)

                mealGeneratedOutput = ""

            pygame.draw.rect(display,red,(480,305,16,17),border_radius=3,width=1)

        display.blit(text5.render("x",False,red),(483,298))      # cross button to remove item generated
        

        ################################ meal by day box ################################

        pygame.draw.rect(display,semiDarkGrey,(20,390,480,155),border_radius=5)     # main box for the current day meal
        pygame.draw.rect(display,purple,(20,390,480,155),border_radius=5,width=2)

        display.blit(text6.render(day,False,lightGrey),(43,395))     # date and day text
        display.blit(text6.render(date,False,lightGrey),(245,395))

        if (457) < mousePos[0] < (484) and (398) < mousePos[1] < (463):     # arrow button logic
            pygame.draw.rect(display,grey,(457,399,27,65),border_radius=3)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(457,399,27,65),border_radius=3)
            
            pygame.draw.rect(display,purple,(457,399,27,65),border_radius=3,width=1)

        if (457) < mousePos[0] < (484) and (472) < mousePos[1] < (537):
            pygame.draw.rect(display,grey,(457,472,27,65),border_radius=3)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(457,472,27,65),border_radius=3)
            
            pygame.draw.rect(display,purple,(457,472,27,65),border_radius=3,width=1)

        pygame.draw.line(display,purple,start_pos=(470,460),end_pos=(470,410),width=3)     # lines for body of arrows
        pygame.draw.line(display,purple,start_pos=(470,475),end_pos=(470,525),width=3)

        pygame.draw.polygon(display,purple,((470,401),(460,416),(480,416)))     # triangles for the arrows
        pygame.draw.polygon(display,purple,((470,534),(460,519),(480,519)))     # top vertex, left vertex, right vertex


        
        ################################ bottom buttons ################################

        for i in range(2):     # buttons at the bottom of the screen
            pygame.draw.rect(display,semiDarkGrey,(250*i+20,555,230,45),border_radius=8)
            pygame.draw.rect(display,grey,(250*i+20,555,230,45),border_radius=8,width=2)

            if (250*i+20) < mousePos[0] < (250*i+250) and (555) < mousePos[1] < (600):     # button logic
                pygame.draw.rect(display,lightPurple,(250*i+20,555,230,45),border_radius=8)
                pygame.draw.rect(display,purple,(250*i+20,555,230,45),border_radius=8,width=2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,purple,(250*i+20,555,230,45),border_radius=8)
                    pygame.draw.rect(display,purple,(250*i+20,555,230,45),border_radius=8,width=2)

        display.blit(text3.render("Settings",False,lightGrey),(83,560))
        display.blit(text3.render("New Plan",False,lightGrey),(325,560))
            

        ###############################################################################
        ############################### right hand side ###############################
        ###############################################################################

        ################################ main box outline ################################

        pygame.draw.rect(display,semiDarkGrey,(520,20,400,525),border_radius=4)     # meal plan week background
        pygame.draw.rect(display,purple,(520,20,400,525),border_radius=4,width=3)     # meal plan week outline

        for i in range(6):
            pygame.draw.line(display,purple,start_pos=(520,74*i+96),end_pos=(918,74*i+96),width=2)     # dividers for each day

        for i in range(7):
            display.blit(text7.render(daysOfWeek[i],False,lightGrey),(530,74*i+23))     # adds the days of the week

            if (530) < mousePos[0] < (587) and (74*i+63) < mousePos[1] < (74*i+90):     # edit button logic
                pygame.draw.rect(display,grey,(530,74*i+63,57,27),border_radius=4)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,semiDarkGrey,(530,74*i+63,57,27),border_radius=4)

            pygame.draw.rect(display,orange,(530,74*i+63,57,27),border_radius=4,width=1)
            display.blit(text5.render("Edit",False,orange),(540,74*i+63))

        pygame.display.flip()
        sleep(0.082)

    pygame.quit()    

MPGUImain()
