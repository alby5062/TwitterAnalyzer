from termcolor import colored


def process_hashtag(remove_USR_URL):
    print(colored("[-File status: Open]", "green"))
    file = open("C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/hashtags.txt","w",encoding = 'utf-8')
    hashtag = ''
    for w in remove_USR_URL:
        if w.startswith('#'):
            hashtag += w
    print(colored("[-File status: Writing]","yellow"))

    file.write(hashtag)

    counts = dict()

    for h in hashtag:
        if h in counts:
            counts[h] += 1
        else:
            counts[h] = 1
    for x,y in counts.items():
        print(x + ": ",y)

    print(colored("[-File status: Close]","red"))
    file.close()
    print(colored("[HASHTAG PROCESSED]", "green"))
    print(hashtag)
    return remove_USR_URL
