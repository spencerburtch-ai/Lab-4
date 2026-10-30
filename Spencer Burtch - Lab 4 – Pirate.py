translationDictionary = {
    "hello": "Avast",
    "excuse": "Arrr",
    "sir": "Matey",
    "boy": "Matey",
    "man": "Matey",
    "madam": "Proud beauty",
    "woman": "Proud beauty",
    "officer": "Foul blaggart",
    "the": "Th'",
    "my": "Me",
    "your": "Yer",
    "is": "Be",
    "are": "Be",
    "kitchen": "Galley",
    "hotel": "Fleabag inn"
}

def toPirate(sentence):
    words = sentence.split()
    translated = []

    for word in words:
        pirateWord = translationDictionary.get(word.lower(), word)

        if word[0].isupper():
            pirateWord = pirateWord.capitalize()

        translated.append(pirateWord)

    return " ".join(translated)

sentence = input("Enter an English sentence: ")
print(toPirate(sentence))