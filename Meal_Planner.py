#~~~~~ Meal Planner ~~~~~#

import csv

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

    #print(typeVeggie)
    #print(typeMeal)
    #print(typeMeat)

    for i in range(len(mealsArray)):
        try:
            if typeVeggie[i] in typeMeal and typeVeggie[i] in typeMeat:
                potentialMeals.append(typeVeggie[i])

        except IndexError:
            break

    return potentialMeals

mealsArray = readMealsFile()
potentialMeals = filterMeals(mealsArray,'n','n',None)

print(potentialMeals)
print(len(potentialMeals))
