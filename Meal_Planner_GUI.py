#~~~~~ Meal Planner GUI ~~~~~#

import pygame
from time import sleep
from Meal_Output_Generator_Size import findSize, findPlanSize, findMBDSize
from Meal_Planner import generateNewRandomMeal, mealByDayBox, getShortDate, getMealPlan, newMealPlan, getMealForDay, reverseBoolean, generateMealIdea
from Cache import *

def MPGUImain():
    pygame.init()
    display = pygame.display.set_mode((950,611))
    pygame.display.set_caption("Meal Planner")

    version = "1.0.0"
    mealGeneratedOutput = ""
    dayToEdit = ""
    dayDiff = 0
    mealByDay = mealByDayBox(dayDiff)
    mealForDay = getMealForDay(dayDiff)
    weekDiff = 0
    shortDate = getShortDate(weekDiff)
    mealPlan = getMealPlan(weekDiff)
    daysOfWeek = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    daysOfWeekLong = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    running = True
    inMain = True
    outMain = False
    popupScreenActive = False
    mealIdeaFilterScreen = False
    editPlanDayScreen = False
    addMealToPlanScreen = False

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
            
            if (20) < mousePos[0] < (500) and (70*i+80) < mousePos[1] < (70*i+140) and popupScreenActive == False:
                pygame.draw.rect(display,lightPurple,(20,70*i+80,480,60),border_radius=8)
                pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8,width=2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8)
                    pygame.draw.rect(display,purple,(20,70*i+80,480,60),border_radius=8,width=2)

                    if i == 0:
                        popupScreenActive = True
                        mealIdeaFilterScreen = True

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
        
        if (28) < mousePos[0] < (96) and (336) < mousePos[1] < (364) and popupScreenActive == False:     # "add..." button logic 
            pygame.draw.rect(display,grey,(28,336,68,28),border_radius=4)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(28,336,68,28),border_radius=4)

                popupScreenActive = True
                addMealToPlanScreen = True
            
        pygame.draw.rect(display,orange,(28,336,68,28),border_radius=4,width=1)     # outline for the "Add..." button
        display.blit(text4.render("Add...",False,orange),(37,339))     # text for the "Add..." button
        
        if mealGeneratedOutput != "":     # displaying the meal generated
            x, y = findSize(len(list(mealGeneratedOutput)))
            mealOutputText = pygame.font.SysFont('verdana',x)
            display.blit(mealOutputText.render(mealGeneratedOutput,False,purple),(110,292+y))
            
        if (480) < mousePos[0] < (496) and (305) < mousePos[1] < (322) and popupScreenActive == False:     # cross button logic
            pygame.draw.rect(display,grey,(481,306,14,15),border_radius=3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(481,306,14,15),border_radius=3)

                mealGeneratedOutput = ""

            pygame.draw.rect(display,red,(480,305,16,17),border_radius=3,width=1)

        display.blit(text5.render("x",False,red),(483,298))      # cross button to remove item generated
        

        ################################ meal by day box ################################

        pygame.draw.rect(display,semiDarkGrey,(20,390,480,155),border_radius=5)     # main box for the current day meal
        pygame.draw.rect(display,purple,(20,390,480,155),border_radius=5,width=2)

        display.blit(text6.render(mealByDay[1],False,lightGrey),(43,395))     # date and day text
        display.blit(text6.render(mealByDay[0],False,lightGrey),(270,395))

        if (457) < mousePos[0] < (484) and (398) < mousePos[1] < (463) and popupScreenActive == False:     # arrow button logic
            pygame.draw.rect(display,grey,(457,399,27,65),border_radius=3)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(457,399,27,65),border_radius=3)

                if dayDiff < 14:
                    dayDiff += 1
                    mealByDay = mealByDayBox(dayDiff)
                    mealForDay = getMealForDay(dayDiff)
            
            pygame.draw.rect(display,purple,(457,399,27,65),border_radius=3,width=1)

        if (457) < mousePos[0] < (484) and (472) < mousePos[1] < (537) and popupScreenActive == False:
            pygame.draw.rect(display,grey,(457,472,27,65),border_radius=3)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,semiDarkGrey,(457,472,27,65),border_radius=3)

                if dayDiff > -14:
                    dayDiff -= 1
                    mealByDay = mealByDayBox(dayDiff)
                    mealForDay = getMealForDay(dayDiff)
            
            pygame.draw.rect(display,purple,(457,472,27,65),border_radius=3,width=1)

        pygame.draw.line(display,purple,start_pos=(470,460),end_pos=(470,410),width=3)     # lines for body of arrows
        pygame.draw.line(display,purple,start_pos=(470,475),end_pos=(470,525),width=3)

        pygame.draw.polygon(display,purple,((470,401),(460,416),(480,416)))     # triangles for the arrows
        pygame.draw.polygon(display,purple,((470,534),(460,519),(480,519)))     # top vertex, left vertex, right vertex

        if mealForDay[1] == '':
            x1,y1,x2,y2 = findMBDSize(len(mealForDay[0]),False,None)
            mealForDayText = pygame.font.SysFont('verdana',x1)
            display.blit(mealForDayText.render(mealForDay[0],False,purple),(43,440+y1))

        else:
            x1,y1,x2,y2 = findMBDSize(len(mealForDay[0]),True,len(mealForDay[1]))
            mealForDayText = pygame.font.SysFont('verdana',x1)
            display.blit(mealForDayText.render(mealForDay[0],False,purple),(43,440+y1))
            mealForDayTextVeggie = pygame.font.SysFont('verdana',x2)
            display.blit(mealForDayTextVeggie.render(mealForDay[1],False,purple),(43,440+y2))

        
        ################################ bottom buttons ################################

        for i in range(2):     # buttons at the bottom of the screen
            pygame.draw.rect(display,semiDarkGrey,(250*i+20,555,230,45),border_radius=8)
            pygame.draw.rect(display,grey,(250*i+20,555,230,45),border_radius=8,width=2)

            if (250*i+20) < mousePos[0] < (250*i+250) and (555) < mousePos[1] < (600) and popupScreenActive == False:     # button logic
                pygame.draw.rect(display,lightPurple,(250*i+20,555,230,45),border_radius=8)
                pygame.draw.rect(display,purple,(250*i+20,555,230,45),border_radius=8,width=2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,purple,(250*i+20,555,230,45),border_radius=8)
                    pygame.draw.rect(display,purple,(250*i+20,555,230,45),border_radius=8,width=2)

                    if i == 1:
                        newMealPlan(weekDiff)
                        mealPlan = getMealPlan(weekDiff)

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

            if (530) < mousePos[0] < (587) and (74*i+63) < mousePos[1] < (74*i+90) and popupScreenActive == False:     # edit button logic
                pygame.draw.rect(display,grey,(530,74*i+63,57,27),border_radius=4)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,semiDarkGrey,(530,74*i+63,57,27),border_radius=4)

                    popupScreenActive = True
                    editPlanDayScreen = True
                    dayToEdit = daysOfWeekLong[i]

            pygame.draw.rect(display,orange,(530,74*i+63,57,27),border_radius=4,width=1)
            display.blit(text5.render("Edit",False,orange),(540,74*i+63))


        ################################ week commencing stuff ################################

        display.blit(text1.render(shortDate,False,orange),(643,543))     # week commencing date

        if (541) < mousePos[0] < (631) and (562) < mousePos[1] < (589) and popupScreenActive == False:     # arrow button logic
            pygame.draw.rect(display,semiDarkGrey,(541,562,91,29),border_radius=3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,darkGrey,(541,562,91,29),border_radius=3)

                if weekDiff > -2:
                    weekDiff -= 1
                    shortDate = getShortDate(weekDiff)
                    mealPlan = getMealPlan(weekDiff)
            
            pygame.draw.rect(display,purple,(541,562,91,29),border_radius=3,width=1)

        if (802) < mousePos[0] < (892) and (562) < mousePos[1] < (589) and popupScreenActive == False:
            pygame.draw.rect(display,semiDarkGrey,(802,562,92,29),border_radius=3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(display,darkGrey,(802,562,92,29),border_radius=3)

                if weekDiff < 2:
                    weekDiff += 1
                    shortDate = getShortDate(weekDiff)
                    mealPlan = getMealPlan(weekDiff)
            
            pygame.draw.rect(display,purple,(802,562,92,29),border_radius=3,width=1)

        pygame.draw.line(display,purple,start_pos=(628,576),end_pos=(558,576),width=3)     # lines for main body of arrow
        pygame.draw.line(display,purple,start_pos=(805,576),end_pos=(875,576),width=3)

        pygame.draw.polygon(display,purple,((890,576),(875,565),(875,587)))     # triangles for the arrows
        pygame.draw.polygon(display,purple,((543,576),(558,565),(558,587)))     # left/right vertex, top vertex, bottom vertex


        ################################ displaying week plan stuff ################################

        for i in range(7):
            if mealPlan[i][1] == '':
                x1,y1,x2,y2 = findPlanSize(len(mealPlan[i][0]),False,None)
                mealPlanDay = pygame.font.SysFont('verdana',x1)
                display.blit(mealPlanDay.render(mealPlan[i][0],False,purple),(604,74*i+17+y1))

            else:
                x1,y1,x2,y2 = findPlanSize(len(mealPlan[i][0]),True,len(mealPlan[i][1]))
                mealPlanDay = pygame.font.SysFont('verdana',x1)
                display.blit(mealPlanDay.render(mealPlan[i][0],False,purple),(604,74*i+17+y1))
                mealPlanDayVeggie = pygame.font.SysFont('verdana',x2)
                display.blit(mealPlanDayVeggie.render(mealPlan[i][1],False,purple),(604,74*i+17+y2))



        ####################################################################################
        ############################### new meal idea button ###############################
        ####################################################################################

        if popupScreenActive == True and mealIdeaFilterScreen == True:
            pygame.draw.rect(display,semiDarkGrey,(175,155,600,300),border_radius=10)
            pygame.draw.rect(display,lightPurple,(175,155,600,300),border_radius=10,width=3)

            ################################ cross button ################################

            if (747) < mousePos[0] < (763) and (167) < mousePos[1] < (182):     # cross button logic
                pygame.draw.rect(display,grey,(748,168,14,15),border_radius=3)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,semiDarkGrey,(748,168,14,15),border_radius=3)

                    popupScreenActive = False
                    mealIdeaFilterScreen = False

                pygame.draw.rect(display,red,(747,167,16,17),border_radius=3,width=1)

            display.blit(text5.render("x",False,red),(750,160))      # cross button to remove item generated
            
            ################################ filters available ################################

            display.blit(text1.render("Filters",False,lightGrey),(400,160))
            
            display.blit(text3.render("Veggie",False,lightGrey),(215,225))
            display.blit(text3.render("Type of Meal",False,lightGrey),(390,225))
            display.blit(text3.render("Meat",False,lightGrey),(630,225))

            options = ["yes","no","normal","soup","roast","beef","pork","fish","chicken","veggie","other"]

            chosenFilters = getMealIdeaCache()
            
            for i in range(2):
                display.blit(text5.render(options[i],False,purple),(240,25*i+261))      # vegetarian options

                if (215) < mousePos[0] < (227) and (25*i+270) < mousePos[1] < (25*i+282):
                    pygame.draw.rect(display,grey,(215,25*i+270,12,12),border_radius=6)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        chosenFilters[i] = reverseBoolean(chosenFilters[i])

                if chosenFilters[i]:
                    pygame.draw.rect(display,orange,(215,25*i+270,12,12),border_radius=6)

                pygame.draw.rect(display,orange,(215,25*i+270,12,12),border_radius=6,width=1)
                

            for i in range(3):
                display.blit(text5.render(options[i+2],False,purple),(425,25*i+261))     # meal type options

                if (400) < mousePos[0] < (412) and (25*i+270) < mousePos[1] < (25*i+282):
                    pygame.draw.rect(display,grey,(400,25*i+270,12,12),border_radius=6)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        chosenFilters[i+2] = reverseBoolean(chosenFilters[i+2])

                if chosenFilters[i+2]:
                    pygame.draw.rect(display,orange,(400,25*i+270,12,12),border_radius=6)

                pygame.draw.rect(display,orange,(400,25*i+270,12,12),border_radius=6,width=1)
                

            for i in range(6):
                display.blit(text5.render(options[i+5],False,purple),(655,25*i+261))     # meat type options

                if (630) < mousePos[0] < (642) and (25*i+270) < mousePos[1] < (25*i+282):
                    pygame.draw.rect(display,grey,(630,25*i+270,12,12),border_radius=6)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        chosenFilters[i+5] = reverseBoolean(chosenFilters[i+5])

                if chosenFilters[i+5]:
                    pygame.draw.rect(display,orange,(630,25*i+270,12,12),border_radius=6)

                pygame.draw.rect(display,orange,(630,25*i+270,12,12),border_radius=6,width=1)

            writeMealIdeaCache(chosenFilters)

            ################################ reset button ################################

            if (191) < mousePos[0] < (271) and (171) < mousePos[1] < (201):
                pygame.draw.rect(display,grey,(191,171,80,30),border_radius=4)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,semiDarkGrey,(191,171,80,30),border_radius=4)

                    chosenFilters = [False for i in range(11)]
                    writeMealIdeaCache(chosenFilters)

            pygame.draw.rect(display,orange,(191,171,80,30),border_radius=4,width=1)
            display.blit(text5.render("Reset",False,orange),(203,173))

            ################################ generate button ################################

            if (380) < mousePos[0] < (570) and (380) < mousePos[1] < (430):
                pygame.draw.rect(display,grey,(380,380,190,50),border_radius=4)     # generate button logic

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,semiDarkGrey,(380,380,190,50),border_radius=4)

                    popupScreenActive = False
                    mealIdeaFilterScreen = False

                    filters = convertCacheToFilters(chosenFilters)
                    mealGeneratedOutput = generateMealIdea(filters)
                    
            pygame.draw.rect(display,purple,(380,380,190,50),border_radius=4,width=2)
            display.blit(text3.render("Generate",False,lightGrey),(417,388))



        #####################################################################################
        ############################### edit meal plan button ###############################
        #####################################################################################

        if popupScreenActive == True and editPlanDayScreen == True:
            pygame.draw.rect(display,semiDarkGrey,(175,155,600,300),border_radius=10)
            pygame.draw.rect(display,lightPurple,(175,155,600,300),border_radius=10,width=3)

            ################################ cross button ################################

            if (747) < mousePos[0] < (763) and (167) < mousePos[1] < (182):     # cross button logic
                pygame.draw.rect(display,grey,(748,168,14,15),border_radius=3)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(display,semiDarkGrey,(748,168,14,15),border_radius=3)

                    popupScreenActive = False
                    editPlanDayScreen = False

                pygame.draw.rect(display,red,(747,167,16,17),border_radius=3,width=1)

            display.blit(text5.render("x",False,red),(750,160))      # cross button to remove item generated

            ################################ edit menu ################################

            display.blit(text1.render("Edit "+dayToEdit,False,lightGrey),(300,160))



        #######################################################################################
        ############################### add meal to plan button ###############################
        #######################################################################################

        if popupScreenActive == True and addMealToPlanScreen == True:
            if mealGeneratedOutput == "" or mealGeneratedOutput == "No meal options":
                popupScreenActive = False
                addMealToPlanScreen = False

            else:
                pygame.draw.rect(display,semiDarkGrey,(175,155,600,300),border_radius=10)
                pygame.draw.rect(display,lightPurple,(175,155,600,300),border_radius=10,width=3)

                ################################ cross button ################################

                if (747) < mousePos[0] < (763) and (167) < mousePos[1] < (182):     # cross button logic
                    pygame.draw.rect(display,grey,(748,168,14,15),border_radius=3)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(display,semiDarkGrey,(748,168,14,15),border_radius=3)

                        popupScreenActive = False
                        addMealToPlanScreen = False

                    pygame.draw.rect(display,red,(747,167,16,17),border_radius=3,width=1)

                display.blit(text5.render("x",False,red),(750,160))      # cross button to remove item generated

                ################################ edit menu ################################

                display.blit(text1.render("Add to...",False,lightGrey),(365,160))

                for i in range(7):
                    display.blit(text5.render(daysOfWeekLong[i],False,purple),(275,25*i+241))      # days to add to

                    if (250) < mousePos[0] < (262) and (25*i+250) < mousePos[1] < (25*i+262):
                        pygame.draw.rect(display,grey,(250,25*i+250,12,12),border_radius=6)

                        #if event.type == pygame.MOUSEBUTTONDOWN:
                            #chosenFilters[i] = reverseBoolean(chosenFilters[i])

                    #if chosenFilters[i]:
                        #pygame.draw.rect(display,orange,(215,25*i+270,12,12),border_radius=6)

                    pygame.draw.rect(display,orange,(250,25*i+250,12,12),border_radius=6,width=1)
            


        ##################################################################################
        ############################## updating the display ##############################
        ##################################################################################

        pygame.display.flip()
        sleep(0.082)

    pygame.quit()    

MPGUImain()
