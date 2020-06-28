import json
from typing import List

from termcolor import colored


def slang_words(result_lwc):
    with open('C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/slang_words.txt','r') as file:
        slang_words_json = json.load(file)
        print(colored("[-File status: Open]","green"))
        print(colored("[-File status: Close]","red"))

    # file = open("Resource/results.txt","w",encoding = 'utf-8')

    result_slang = []

    for r in result_lwc:
        slang = []
        r_split = r.split()
        for rs in r_split:
            if rs in slang_words_json:
                slang.append(slang_words_json.get(rs) + " ")
            else:
                slang.append(rs + " ")
        slang = ' '.join(slang)
        result_slang.append(slang)
    print(colored("[REMOVE SLANG]","green"))
    for r in result_slang:
        print(r)
    return result_slang
