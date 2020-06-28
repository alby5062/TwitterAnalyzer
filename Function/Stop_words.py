from nltk.corpus import stopwords
from termcolor import colored


def stop_words(stemmed_word):
    stop_words = stopwords.words('english')
    result_stop = []
    for s in stemmed_word:
        if s not in stop_words:
            result_stop.append(s)
    print(colored("[REMOVE STOP WORDS]", "green"))
    print(result_stop)
    return result_stop
