def countWords(sentence):
    return len(sentence.split())


sentence = input("Enter a sentence: ")
print(f"Number of words: {countWords(sentence)}")
