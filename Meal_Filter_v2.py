#~~~~~ Filter Meals ~~~~~#

def filterProperty(prop,rProp):
    # takes a property and checks it against the required property
    # designed to be used in an external loop
    
    if prop == rProp:
        return True

    return False


def retrievePossibleMeals(meals,filters):
    # takes the array of meals and filters required
    # retrieves an array of the possible meals for each filter and puts them into one big array

    unfilteredMeals = []

    for i in range(len(filters)):
        tempArray1 = []

        for j in range(len(meals)):

            for k in range(len(filters[i])):
            
                if meals[j][0] not in unfilteredMeals:
                
                    if filterProperty(filters[i][k],meals[j][i+1]):
                        tempArray1.append(meals[j][0])

        unfilteredMeals.append(tempArray1)

    return unfilteredMeals


def combineFilters(allPossibleMeals):
    # takes the bog array of each possible meal for each filter
    # returns an array with all the items matching the filters

    potentialMeals = []

    for i in range(len(allPossibleMeals)):

        for j in range(len(allPossibleMeals[i])):
            counter = 0     # counter to count if the value is in the other arrays of filtered items

            for k in range(len(allPossibleMeals)):
                
                if allPossibleMeals[i][j] in allPossibleMeals[k]:
                    counter += 1

            if counter == len(allPossibleMeals):
                potentialMeals.append(allPossibleMeals[i][j])

    potentialMeals = list(set(potentialMeals))
    
    return potentialMeals


def getOptions(mealsArray,filters):
    # takes filters array and the meals array parameter so csv doesnt have to be imported in this file
    # returns back an array of all the meals which match the filters given

    temp1 = retrievePossibleMeals(mealsArray,filters)
    options = combineFilters(temp1)

    return options
