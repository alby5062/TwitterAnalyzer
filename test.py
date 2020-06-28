import glob,os,json,csv
from collections import Counter

root = "C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/Risorse lessicali/"
conScore = "C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/Risorse lessicali/ConScore"


def removeUnderscore(l,result):
    for w in l:
        if '_' in w:
            result.append(w)
    remove_w = [w for w in l if w not in result]
    return remove_w


'''def count(remove_w):
    for w in remove_w:
        if w in words_dict:
            words_dict[w] += 1
        else:
            words_dict[w] = 1'''


def processWord(subdir,file,freq_emo_dict,filenames):
    f = open(subdir + '/' + file,'r',encoding = 'utf8',errors = 'ignore')
    words = f.read()
    f.close()

    l = words.split()
    result = []

    filename = file.strip('.txt')  # store file name w/o .txt
    if (file != "GI_POS.txt") & (file != "GI_NEG.txt"):
        head,sep,tail = filename.partition('_')
        filename = head
    else:
        filename = file.strip('.txt')

    remove = removeUnderscore(l, result)  # remove underscore

    for word in remove:
        if word not in freq_emo_dict:
            freq_emo_dict[word] = filenames.copy()
        freq_emo_dict[word][filename] += 1

    return


def risorse_lessicali():
    emo_dict = dict()
    for subdir,dirs,files in os.walk(root):
        if subdir != root:
            for file in files:
                words_dict = dict()

                f = open(subdir + '/' + file,'r',encoding = 'utf8',errors = 'ignore')
                words = f.read()
                f.close()

                l = words.split()
                result = []

                filename = file.strip('.txt')  # store file name w/o .txt

                remove = removeUnderscore(l, result)  # remove underscore

                count = Counter(remove)

                for r in count:
                    list_perc = []
                    perc = 100 * (count[r]) / len(remove)
                    list_perc.append((filename,perc))
                    words_dict[r] = list_perc

            emo_dict[str(os.path.basename(os.path.normpath(subdir)))] = words_dict

    with open('risorse_lessicali.json','w') as fp:
        json.dump(emo_dict,fp,indent = 4)
        print("---- Json file: 'risorse_lessicali.json' created ----")

    freq_emo_dict = dict()
    filenames = dict()

    for subdir,dirs,files in os.walk(os.path.normpath(root)):
        if subdir != root:
            if subdir != conScore:
                for file in files:
                    if (file != "GI_POS.txt") & (file != "GI_NEG.txt"):
                        head,sep,tail = file.partition('_')  # remove emotion from filename
                        filename = head.strip('.txt')
                        filenames[filename] = 0
                    else:
                        filename = file.strip('.txt')
                        filenames[filename] = 0
            else:
                for file in files:
                    filename,sep,tail = file.partition('.')
                    filenames[filename] = 0

    print(filenames)

    total_emo_dict = dict()
    for subdir,dirs,files in os.walk(root):
        freq_emo_dict = dict()
        if subdir != root:

            emotion = os.path.basename(subdir).lower()
            if subdir != conScore:
                # print(conScore)
                # print(subdir)
                # print("!=conScore")
                for file in files:
                    processWord(subdir,file,freq_emo_dict,filenames)
            else:
                # print("COGLIONE SONO QUI")
                for file in files:
                    if ".txt" in file:
                        f = open(subdir + '/' + file,'r',encoding = 'utf8',errors = 'ignore')
                        words = f.readlines()
                        f.close()

                        filename,sep,tail = file.partition('.')
                        for line in words:
                            words = line.split()

                            word = words[0]
                            value = int(words[1])

                            if word not in freq_emo_dict:
                                freq_emo_dict[word] = filenames.copy()
                            freq_emo_dict[word][filename] = value
                    elif ".tsv" in file:
                        with open(subdir + '/' + file,'r',encoding = 'utf8',errors = 'ignore') as tsvfile:
                            reader = csv.reader(tsvfile,delimiter = '\t')

                            filename,sep,tail = file.partition('.')
                            for row in reader:

                                word = row[0]
                                value = float(row[1])

                                if word not in freq_emo_dict:
                                    freq_emo_dict[word] = filenames.copy()
                                freq_emo_dict[word][filename] = value

                    elif '.csv':
                        with open(subdir + '/' + file,'r',encoding = 'utf8',errors = 'ignore') as csvfile:
                            reader = csv.reader(csvfile,delimiter = '\t')

                            filename,sep,tail = file.partition('.')
                            for row in reader:

                                word = row[0]
                                value = float(row[1])

                                if word not in freq_emo_dict:
                                    freq_emo_dict[word] = filenames.copy()
                                freq_emo_dict[word][filename] = value

                    total_emo_dict[emotion] = freq_emo_dict

                print("finish TRATTAMENTO RISORSE")
    return total_emo_dict[emotion]
