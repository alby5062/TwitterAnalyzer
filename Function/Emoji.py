import os,glob
from termcolor import colored


def emoji(remove_USR_URL):
    AdditionalEmoji = []
    EmojiNeg = []
    EmojiPos = []
    OthersEmoji = []

    os.chdir("C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/Emoji")
    for file in glob.glob("*.txt"):
        nomeLista = file.strip('.txt')
        lista = open(file, 'r', encoding = 'unicode-escape')
        if nomeLista == "AdditionalEmoji":
            for l in lista:
                AdditionalEmoji = l.split(",")
        elif nomeLista == "EmojiNeg":
            for l in lista:
                EmojiNeg = l.replace("\\\\", "\\")
        elif nomeLista == "EmojiPos":
            for l in lista:
                EmojiPos = l.replace("\\\\", "\\")
        elif nomeLista == "OthersEmoji":
            for l in lista:
                OthersEmoji = l.replace("\\\\", "\\")


    emoji_pos = dict()
    emoji_neg = dict()
    emoji_others = dict()
    emoji_additional = dict()

    for w in remove_USR_URL:
        if w in EmojiPos:
            if w in emoji_pos:
                emoji_pos[w] += 1
            else:
                emoji_pos[w] = 1
        elif w in EmojiNeg:
            if w in emoji_neg:
                emoji_neg[w] += 1
            else:
                emoji_neg[w] = 1
        elif w in OthersEmoji:
            if w in emoji_others:
                emoji_others[w] += 1
            else:
                emoji_others[w] = 1
        elif w in AdditionalEmoji:
            if w in emoji_additional:
                emoji_additional[w] += 1
            else:
                emoji_additional[w] = 1



    print(colored("[DICT EMOJI POS]","green"))
    for e in emoji_pos:
        print(e + ": " + str(emoji_pos[e]))
    print("\n")

    print(colored("[DICT EMOJI NEG]","green"))
    for e in emoji_neg:
        print(e + ": " + str(emoji_neg[e]))
    print("\n")

    print(colored("[DICT EMOJI OTHERS]","green"))
    for e in emoji_others:
        print(e + ": " + str(emoji_others[e]))
    print("\n")

    print(colored("[DICT ADDITIONAL EMOJI]","green"))
    for e in emoji_additional:
        print(e + ": " + str(emoji_additional[e]))
    print("\n")

    return remove_USR_URL
