#~~~~~ Filter Meals ~~~~~#

import csv ########

def filterProperty(prop,rProp):
    # takes a property and checks it against the required property
    # designed to be used in an external loop
    
    if prop == rProp:
        return True

    return False


def retrievePossibleMeals(meals,filters):
    # takes the array of meals and filters required

    unfilteredMeals = []

    for i in range(len(filters)):
        tempArray1 = []

        for j in range(len(meals)):
            tempArray2 = []

            for k in range(len(filters[i])):
            
                if meals[j][0] not in unfilteredMeals:
                
                    if filterProperty(filters[i][k],meals[j][i+1]):
                        tempArray2.append(meals[j][0])

            if len(tempArray2) != 0:
                tempArray1.append(tempArray2)

        unfilteredMeals.append(tempArray1)

    return unfilteredMeals
                    
def readCSVFile():
    with open("Meals.csv") as file:
        array = list(csv.reader(file))

    return array

x = readCSVFile()
print(retrievePossibleMeals(x,['y','rs','v']))
