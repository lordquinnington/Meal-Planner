#~~~~~ Filter Meals ~~~~~#


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

def combineMultipleDiffFilters(pPotentialMeals):     # only give it two
    potentialMeals = []

    for i in range(len(pPotentialMeals[0])):
        if pPotentialMeals[0][i] in pPotentialMeals[1]:
            potentialMeals.append(pPotentialMeals[0][i])

    return potentialMeals

def combineMultipleSameFilters(pPotentialMeals):     # only give it two
    potentialMeals = pPotentialMeals[0]

    for i in range(len(pPotentialMeals[1])):
        if pPotentialMeals[1][i] not in potentialMeals:
            potentialMeals.append(pPotentialMeals[1][i])

    return potentialMeals

def findOptions(mealsArray,filters):
    options = []

    for i in range(len(filters)):
        if 1 < len(filters[i]) <= 3:
            









    
