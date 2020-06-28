from nltk import WordNetLemmatizer
from termcolor import colored


def word_lemmatizer(result_pos_tagging):
    tag = {'N': 'n',
           'V': 'v',
           'J': 'a',
           'S': 's',
           'R': 'r'}
    lemmatized_words = []
    lemmatizer = WordNetLemmatizer()

    for r in result_pos_tagging:
        tags = r[1]
        if tags[0] in tag.keys():
            possss = tag.get(tags[0])
        else:
            possss = 'n'
        lemmatized_words.append(lemmatizer.lemmatize(r[0],pos = possss))
    print(colored("[LEMMATIZED WORDS]", "green"))
    print(lemmatized_words)
    return lemmatized_words
