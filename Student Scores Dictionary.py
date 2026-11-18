
#Spencer Burtch- Lab 4 - Names and Scores functions. 

#defining the makeDictionary function that takes two lists, names and scores, and creates a dictionary with names as keys and scores as values.
def makeDictionary(names, scores):
    scoreDict = {}
    #range function is used to loop through the length of the names list and assign each name as a key and the corresponding score as a value in the scoreDict dictionary.   
    for i in range(len(names)):
        scoreDict[names[i]] = scores[i]

    return scoreDict

#Adds all the scores using sum() and divides by the number of entries using len() to find the average.
def calculateAverage(scoreDict):
    return sum(scoreDict.values()) / len(scoreDict)

#Defining the two lists, one stored as names, the other as the scores.
names = ["Joe", "Tom", "Barb", "Sue", "Sally"]
scores = [10, 23, 13, 18, 12]
#Defining scoreDict by making a new dictionary with both the scores and names together.
scoreDict = makeDictionary(names, scores)
print(scoreDict)
#Prints the score for Barb stored in the Dictionary 
print(scoreDict["Barb"])
#Adds John and makes his score 19
scoreDict["John"] = 19
print(scoreDict)
#Gets all the scores and sorts them from lowest to highest.
sortedScores = sorted(scoreDict.values())
print(sortedScores)
#Calculates and prints the average of all scores in the dictionary.
print(calculateAverage(scoreDict))
#Updates Sally's score from 12 to 13
scoreDict["Sally"] = 13
print(scoreDict) 
#Removes Tom's score from dictionary
del scoreDict["Tom"]
#Final printing of the scoreDict will all the changes above.
print(scoreDict)
