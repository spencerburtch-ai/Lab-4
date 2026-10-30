def makeDictionary(names, scores):
    return dict(zip(names, scores))


def calculateAverage(scoreDict):
    return sum(scoreDict.values()) / len(scoreDict)


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
print(scoreDict)
