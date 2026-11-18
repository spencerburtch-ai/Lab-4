#Spencer Burtch- Lab 4- Pirate Translator 

translationDictionary = {
    "hello": "avast",
    "excuse": "arrr",
    "sir": "matey",
    "boy": "matey",
    "man": "matey",
    "madam": "proud beauty",
    "woman": "proud beauty",
    "officer": "foul blaggart",
    "the": "th'",
    "my": "me",
    "your": "yer",
    "is": "be",
    "are": "be",
    "kitchen": "galley",
    "hotel": "fleabag inn"
}
#Def toPirate function that takes a sentance input and translate it. 
def toPirate(sentence):
#Sentance split that splits the sentence into a list of words and creates an empty list to hold the translated words.
    words = sentence.split()
    translated = []
    #Loop that checks every word, then lowercases it with the word.lower() and checks if it is in the translationDictionary.
    for word in words:
        #get function that checks if the word is in the translationDictionary and if it is, it returns the translated word. If it is not, it returns the original word. 
        pirateWord = translationDictionary.get(word.lower(), word)
        #if statement that checks if the first Letter of the word is uppercase and if it is, it capitalizes the translated word.
        if word[0].isupper():
            pirateWord = pirateWord.capitalize()
        #Append function adds the translated word to the end of the list. 
        translated.append(pirateWord)
    #The join function will combine the translated words into a single string with spaces in between each word and return it. 
    return " ".join(translated)
#Assigning the input command to the variable sentence and printing the translated sentence using the toPirate function. 
sentence = input("Enter an English sentence: ")
print(toPirate(sentence))