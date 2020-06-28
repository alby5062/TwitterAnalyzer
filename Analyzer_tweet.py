from Function.Remove_USR_URL import remove_USR_URL
from Function.Process_hashtag import process_hashtag
from Function.Emoticons import emoticons
from Function.Emoji import emoji
from Function.Sentence_tokenize import sentence_tokenize
from Function.Lower_case import lower_case
from Function.Slang_words import slang_words
from Function.POS_tagging import pos_tagging
from Function.Word_lemmatizer import word_lemmatizer
# from Function.Stemmed_words import stemmed_words
from Function.Stop_words import stop_words
from Function.Count_freq import count_freq
from Function.Postgresql import database_sql
from Function.Remove_words_not_recognized import remove_not_recognized
# from Function.MongoDB import database_mongo
from Function.Word_cloud import word_cloud
from termcolor import colored
import os

rootdir = "C:/Users/alby5/PycharmProjects/TwitterAnalyzer/Resource/Twitter_messaggi"
print(colored("Directory: " + rootdir,"green"))



for subdir,dirs,files in os.walk(rootdir):

    emotions = dict()
    emo_files = []

    for file in files:
        print(colored("[-File status: Open]","green"))
        f = open(subdir + '/' + file,'r',encoding = 'utf8',errors = 'ignore')
        print(colored("[-File status: Reading]","yellow"))
        resource_sent = f.read()
        f.close()
        print(colored("[-File status: Close]","red"))
        # resource_sent.encode('unicode-escape')
        emo_files = file.strip(".txt")

        print(colored("[File: " + emo_files + "]","green"))

        print(colored("[START ANALYSIS]","green"))
        freq = count_freq \
            (stop_words
             (word_lemmatizer
              (pos_tagging
               (remove_not_recognized
                (slang_words
                 (lower_case
                  (sentence_tokenize
                   (emoji
                    (emoticons
                     (process_hashtag
                      (remove_USR_URL(resource_sent))))))))))))

        # Database Upload
        print(colored("[POSTGRESQL]","yellow"))
        database_sql()
        print(colored("[MONGODB]","yellow"))
        # database_mongo(freq)

        # Word cloud
        print(colored("[WORD CLOUD CREATED]","green"))
        emotions[emo_files] = freq
        word_cloud(freq)

    '''' # Analysis Tweet
        print(colored("[START ANALYSIS]","green"))
        freq = count_freq \
            (stop_words
             (stemmed_words
              (word_lemmatizer
               (pos_tagging
                (remove_not_recognized
                 (slang_words
                  (lower_case
                   (sentence_tokenize
                    (emoji
                     (emoticons
                      (process_hashtag
                       (remove_USR_URL(resource_sent)))))))))))))'''
