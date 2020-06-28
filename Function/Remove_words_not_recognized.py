from nltk.corpus import words
from termcolor import colored


def remove_not_recognized(result_slang):
    result_remove = []
    for r in result_slang:
        word = r.split()
        i = 0

        for w in word:
            if len(word) == 1 or w not in words.words():

                for i in range(0,len(word)):
                    new_word = ""
                    new_word2 = ""

                    if i != 0 and i != len(word) - 1:
                        new_word = word[i - 1] + word[i] + word[i + 1]
                        new_word2 = word[i - 1] + word[i]
                    elif i == len(word) - 1:
                        new_word = word[i - 1] + word[i]
                    elif i == 0:
                        new_word = word[i] + word[i + 1]

                    if new_word in words.words() and new_word not in result_remove:
                        result_remove.append(new_word)

                    if new_word2 in words.words() and new_word not in result_remove:
                        result_remove.append(new_word2)

            elif w in words.words() and len(w) != 1:
                result_remove.append(w)
    print(colored("[REMOVE NOT RECOGNIZED WORDS]","green"))
    print(result_remove)
    return result_remove
