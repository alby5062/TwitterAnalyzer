from collections import Counter
from termcolor import colored
import pprint


def count_freq(result_stop):
    count_freq = Counter(result_stop).most_common()
    print(colored("[-File status: Open]","green"))

    file = open("C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/results.txt","w",encoding = 'utf-8')

    print(colored("[-File status: Writing]","yellow"))

    file.write("---- Count word frequency ---- \n \n")

    for c in count_freq:
        print(c)
        string = c[0] + ":" + str(c[1])
        file.write(string + "\n")

    file.close()
    print(colored("[-File status: Close]", "red"))
    print(colored("[COUNT FREQUENCY]", "green"))
    pprint.pprint(count_freq)
    return count_freq
