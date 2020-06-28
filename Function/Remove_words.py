from nltk.corpus import words
from termcolor import colored


def remove_words(result_slang):
    result_remove = []
    for r in result_slang:
        phrase = []
        word = r.split()
        for w in word:
            if w in words.words():
                phrase.append(w)
        result_remove.append(phrase)
    print(colored("[REMOVE WORDS]", "green"))
    print(result_remove)
    return result_remove
