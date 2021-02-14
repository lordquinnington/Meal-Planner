#~~~~~ Meal Planner ~~~~~#

import csv, random, datetime

def readCSVFile(name):
    with open(name+".csv") as file:
        array = list(csv.reader(file))

    return array

def filterByProperty(prop,rProp):      # prop => property of it, r => required
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

    return "No meal options"

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
    
    return days[dayToday], dayToday

def generateNewRandomMeal(name):
    mealsArray = readCSVFile(name)

    if len(mealsArray) != 0:
        potentialMeals = combineMultipleFilters([filterMeals(mealsArray,None,'n',None),filterMeals(mealsArray,None,'s',None)])

        if len(potentialMeals) == 1:
            return potentialMeals[0]
        
        x = random.randint(0,len(potentialMeals)-1)

        return potentialMeals[x]

    return "No meal options"
