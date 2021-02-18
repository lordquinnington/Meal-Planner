#~~~~~ Retrieves Cache ~~~~~#

from Meal_Planner import readCSVFile
import csv

def getMealIdeaCache():
    fileCache = readCSVFile("Meal_Idea_Filter_Cache")

    cache = []

    for i in range(len(fileCache)):
        for j in range(len(fileCache[i])):
            if fileCache[i][j] == 'True':
                cache.append(True)

            else:
                cache.append(False)

    return cache

def writeMealIdeaCache(cch):

    toWrite = [[str(cch[0]),str(cch[1])],[str(cch[2]),str(cch[3]),str(cch[4])],[str(cch[5]),str(cch[6]),str(cch[7]),str(cch[8]),str(cch[9]),str(cch[10])]]

    with open("Meal_Idea_Filter_Cache.csv","w",newline='') as file:
        CSVWriter = csv.writer(file,delimiter=',')

        for row in toWrite:
            CSVWriter.writerow(row)

def convertCacheToFilters(cache):
