from termcolor import colored


def remove_USR_URL(resource_sent):
    remove_words = ['URL','USERNAME']
    resource_sent_words = resource_sent.split()
    remove_USR_URL = [w for w in resource_sent_words if w not in remove_words]
    result_remove = ' '.join(remove_USR_URL)
    print(colored("[REMOVE USERNAME/URL]","green"))
    print(result_remove)
    return remove_USR_URL
