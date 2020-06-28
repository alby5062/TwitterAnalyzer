from termcolor import colored


def punctuation_mark(sentences):
    result_pm = []
    punctuation_marks = [',','?','!','.',';',':','\\','/','(',')','&','_','+','=','<','>','"']
    for s in sentences:
        new = s
        for p in punctuation_marks:
            if new.find(p) > -1:
                new = new.replace(p,' ')
        result_pm.append(new)
    print(colored("[REMOVE PUNCTUATION]","green"))
    for r in result_pm:
        print(r)
    return result_pm
