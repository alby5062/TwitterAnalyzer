from nltk import sent_tokenize
from termcolor import colored


def sentence_tokenize(remove_USR_URL):
    result_remove = ' '.join(remove_USR_URL)
    sentences = sent_tokenize(result_remove)
    print(colored("[SENTENCE TOKENIZE]","green"))
    print(sentences)
    return sentences
