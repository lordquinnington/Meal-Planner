#~~~~~ Filter Meals ~~~~~#

def filterByProperty(prop,rProp):      # prop => property of it, r => required
    if rProp == prop:
        return True

    return False

def filterMeals(mealsArray,filters):
    veggie = filters[0]
    meal = filters[1]
    meat = filters[2]
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
        if filters[i] != None:
            if len(filters[i]) > 1:
                for j in range(len(filters[i])-1):
                    for k in range(1,len(filters[i])):
                        f1 = [0 for l in range(len(filters))]
                        f1[i] = filters[i][j]
                        for m in range(len(f1)):
                            if f1[m] == 0 :
                                f1[m] = None
                        m1 = filterMeals(mealsArray,f1)
                        
                        f2 = [0 for l in range(len(filters))]
                        f2[i] = filters[i][k]
                        for m in range(len(f2)):
                            if f2[m] == 0 :
                                f2[m] = None
                        m2 = filterMeals(mealsArray,f2)
            









    
