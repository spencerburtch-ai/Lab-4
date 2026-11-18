
#Defining the countWords Function
#The .split() method breaks a string into a list wherever it finds spaces.
#The len() function returns the number of items in the list.
def countWords(sentence):
    return len(sentence.split())

#Defining Sentence as an input command
sentence = input("Enter a sentence: ")
#str(countWords(sentence)) converts the number of words returned by the function into a string so it can be joined with "Number of words: " and printed as one message.
print("Number of words: " + str(countWords(sentence)))

