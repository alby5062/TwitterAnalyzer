from nltk import LancasterStemmer
from termcolor import colored


def stemmed_words(lemmatized_words):
    lancaster_stemmer = LancasterStemmer()
    stemmed_word = [lancaster_stemmer.stem(l) for l in lemmatized_words]
    print(colored("[STEMMED WORDS]", "green"))
    print(stemmed_word)
    return stemmed_word
