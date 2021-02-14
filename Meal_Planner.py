#~~~~~ Meal Planner ~~~~~#

import csv, random
import datetime

def readMealsFile():
    with open("Meals.csv") as mealsFile:
        mealsArray = list(csv.reader(mealsFile))

    return mealsArray

def filterByProperty(prop,rProp):      # prop => property of it
    if rProp == prop:
        return True

    return False

def filterMeals(mealsArray,veggie,meal,meat):
    potentialMeals = []
    typeVeggie = []
    typeMeal = []
    typeMeat = []

    for i in range(len(mealsArray)):
        if veggie == None:
            for j in range(len(mealsArray)):
                typeVeggie.append(mealsArray[j][0])
        else:
            if filterByProperty(veggie,mealsArray[i][1]) == True:
                typeVeggie.append(mealsArray[i][0])

        if meal == None:
            for j in range(len(mealsArray)):
                typeMeal.append(mealsArray[j][0])
        else:
            if filterByProperty(meal,mealsArray[i][2]) == True:
                typeMeal.append(mealsArray[i][0])

        if meat == None:
            for j in range(len(mealsArray)):
                typeMeat.append(mealsArray[j][0])
        else:
            if filterByProperty(meat,mealsArray[i][3]) == True:
                typeMeat.append(mealsArray[i][0])

    for i in range(len(mealsArray)):
        try:
            if typeVeggie[i] in typeMeal and typeVeggie[i] in typeMeat:
                potentialMeals.append(typeVeggie[i])

        except IndexError:
            break

    return potentialMeals

def combineMultipleFilters(pPotentialMeals):
    potentialMeals = pPotentialMeals[0]
    for i in range(1,len(pPotentialMeals)):
        for j in range(len(pPotentialMeals[i])):
            if pPotentialMeals[i][j] not in potentialMeals:
                potentialMeals.append(pPotentialMeals[i][j])

    return potentialMeals

def generateMeal(potentialMeals):
    if len(potentialMeals) != 0:
        return potentialMeals[random.randint(0,len(potentialMeals)-1)]

    return None

def reverseBoolean(previous):
    if previous == True:
        return False

    return True

def getCurrentDate():
    today = datetime.date.today()
    
    return today.strftime("%d/%m/%y")

def getCurrentDay():
    days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    
    today = str(datetime.date.today())

    x1 = list(today)     # annoyingly have to convert the date into the correct format
    
    x2 = ""
    for i in range(4):
        x2 += x1[i]
    x2 = int(x2)

    x3 = ""
    for i in range(2):
        x3 += x1[5+i]
    x3 = int(x3)
    
    x4 = ""
    for i in range(2):
        x4 += x1[8+i]
    x4 = int(x4)
    
    y = datetime.date(x2,x3,x4)
    dayToday = y.weekday()
    
    return days[dayToday]

##mealsArray = readMealsFile()
##potentialMeals = filterMeals(mealsArray,'n','n','b')
##potentialMeals2 = filterMeals(mealsArray,'n','n','c')
##potentialMeals3 = filterMeals(mealsArray,'y','n','v')
##
##print(potentialMeals)
##print(len(potentialMeals))
##
##print(potentialMeals2)
##print(len(potentialMeals2))
##
##print(potentialMeals3)
##print(len(potentialMeals3))
##
##allPotentialMeals = [potentialMeals,potentialMeals2,potentialMeals3]
##meals = combineMultipleFilters(allPotentialMeals)
##
##print(meals)
##print(len(meals))
##
##for i in range(7):
##    print(generateMeal(meals))

print(getCurrentDay())
