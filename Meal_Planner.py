#~~~~~ Meal Planner ~~~~~#

import csv, random, datetime
from Meal_Filter_v2 import getOptions

def readCSVFile(name):
    with open(name+".csv") as file:
        array = list(csv.reader(file))

    return array

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
        potentialMeals = combineMultipleSameFilters([filterMeals(mealsArray,None,'n',None),filterMeals(mealsArray,None,'s',None)])

        if len(potentialMeals) == 1:
            return potentialMeals[0]
        
        x = random.randint(0,len(potentialMeals)-1)

        return potentialMeals[x]

    return "No meal options"

def mealByDayBox(dayDiff):
    days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    
    date = getCurrentDate()
    day, pos = getCurrentDay()

    if dayDiff != 0:
        if dayDiff > 0:

            ##### day #####
            for i in range(dayDiff):
                pos += 1
                
                if pos == 7:
                    pos = 0

            ##### date #####
            x = datetime.datetime.now() + datetime.timedelta(days=dayDiff)
            date = x.strftime("%d/%m/%y")

        else:
            dayDiff = dayDiff * -1

            ##### day #####
            for i in range(dayDiff):
                pos -= 1
                
                if pos == -1:
                    pos = 6

            ##### date #####
            x = datetime.datetime.now() - datetime.timedelta(days=dayDiff)
            date = x.strftime("%d/%m/%y")

    day = days[pos]    

    return [date,day]

def getWeekCommencing():
    ignore, pos = getCurrentDay()

    wc = datetime.datetime.now() - datetime.timedelta(days=pos)

    return wc

def getShortDate(weekDiff):
    wc = getWeekCommencing()

    if weekDiff >= 0:
        x = wc + datetime.timedelta(weeks=weekDiff)

    else:
        weekDiff = weekDiff * -1

        x = wc - datetime.timedelta(weeks=weekDiff)

    weekCommencing = x.strftime("%d/%m")

    return weekCommencing

def generateMealPlan():
    template = readCSVFile("Meal_Plan_Defaults")
    mealsArray = readCSVFile("Meals")

    weekPlan = []

    for i in range(7):
        mealForDay = []

        options = getOptions(mealsArray,template[i])
        meal = generateMeal(options)

        mealForDay.append(meal)
        mealForDay.append('')     # blank for veggie meal

        weekPlan.append(mealForDay)

    return weekPlan

def writeMealPlanFile(mealPlan,fileNumber):
    with open("Meal_Plan_"+fileNumber+".csv","w",newline='') as planFile:
        CSVWriter = csv.writer(planFile,delimiter=',')
        for row in mealPlan:
            CSVWriter.writerow(row)

def getMealPlan(weekDiff):
    mealPlanFile = str(weekDiff + 2)

    mealPlan = readCSVFile("Meal_Plan_"+mealPlanFile)

    if len(mealPlan) == 0:
        mealPlan = generateMealPlan()
        writeMealPlanFile(mealPlan,mealPlanFile)

        return mealPlan

    return mealPlan
    
    
    






    
