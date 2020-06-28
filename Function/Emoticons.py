from termcolor import colored


def emoticons(remove_USR_URL):
    pos_emoticons = ['B-)',':)',':-)',":')",":'-)",':D',':-D',':\'-)',":')",':o)',':]',':3',':c)',':>','=]','8)','=)', \
 \
                     ':}',':^)','8-D','8D','x-D','xD','X-D','XD','=-D','=D','=-3','=3','B^D',':-))',':*',':^*',
                     '( \'}{\' )', \
 \
                     '^^','(^_^)','^-^',"^.^","^3\^","\^L\^"]

    neg_emoticons = [':(',':-(',":'(",":'-(",'>:[',':-c',':c',':-<',':<',':-[',':[',':{',':\'-(',':\'(', \
 \
                     ' _( ',':\'[',"='(","' [","='[", \
 \
                     ":'-<",":' <",":'<","=' <","='<","T_T","T.T","(T_T)","y_y","y.y","(Y_Y)", \
 \
                     ";-;",";_;",";.;",":_:","o .__. o",".-."]

    emoticons_pos = dict()
    emoticons_neg = dict()

    for w in remove_USR_URL:
        if w in pos_emoticons:
            if w in emoticons_pos:
                emoticons_pos[w] += 1
            else:
                emoticons_pos[w] = 1
        elif w in neg_emoticons:
            if w in emoticons_neg:
                emoticons_neg[w] += 1
            else:
                emoticons_neg[w] = 1

    print(colored("[DICT EMOTICONS POS]","green"))
    for e in emoticons_pos:
        print(e + ": " + str(emoticons_pos[e]))
    print("\n")

    print(colored("[DICT EMOTICONS NEG]","green"))
    for e in emoticons_neg:
        print(e + ": " + str(emoticons_neg[e]))

    return remove_USR_URL
