import psycopg2, pprint
from termcolor import colored
from test import risorse_lessicali


# from Trattamento_risorse_lessicali import total_emo_dict


def database_sql():
    try:
        # Define our connection string
        conn_string = "host='localhost' dbname='postgres' user='postgres' password='alberto'"

        # print the connection string we will use to connect
        print(colored("[Connecting to database	*" + conn_string + "*]","yellow"))

        # get a connection, if a connect cannot be made an exception will be raised here
        conn = psycopg2.connect(conn_string)

        # conn.cursor will return a cursor object, you can use this cursor to perform queries
        cursor = conn.cursor()
        print(colored("[Connected!]","green"))

        drops = (
            "DROP TABLE IF EXISTS ANGER",
            "DROP TABLE IF EXISTS ANTICIPATION",
            "DROP TABLE IF EXISTS DISGUST",
            "DROP TABLE IF EXISTS FEAR",
            "DROP TABLE IF EXISTS JOY",
            "DROP TABLE IF EXISTS SADNESS",
            "DROP TABLE IF EXISTS SURPRISE",
            "DROP TABLE IF EXISTS TRUST")

        commands = (
            "CREATE TABLE ANGER(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, "
            "anewAro INT, anewDown INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, GI_NEG INT, "
            "HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, "
            "listPosEffTerms INT, LIW_POS INT)",

            "CREATE TABLE ANTICIPATION(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, "
            "afinn INT, anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, "
            "GI_NEG INT, HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, "
            "listPosEffTerms INT, LIWC_POS INT)",

            "CREATE TABLE DISGUST(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, "
            "anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, "
            "GI_NEG INT, HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, "
            "listPosEffTerms INT, LIWC_CPOS INT)",

            "CREATE TABLE FEAR(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, "
            "anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, GI_NEG INT, "
            "HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, "
            "listPosEffTerms INT, LIWC_POS INT)",

            '''CREATE TABLE JOY(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, GI_NEG INT, HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, listPosEffTerms INT, LIWC_POS INT)''',
            '''CREATE TABLE SADNESS(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, GI_NEG INT, HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, listPosEffTerms INT, LIWC_POS INT)''',
            '''CREATE TABLE SURPRISE(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, GI_NEG INT, HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, listPosEffTerms INT, LIWC_POS INT)''',
            '''CREATE TABLE TRUST(Word CHAR(20) NOT NULL, EmoSN INT, NRC INT, sentisense INT, afinn INT, anewAro INT, anewDown INT, anewPleas INT, Dal_Activ INT, Dal_Imag INT, Dal_Pleas INT, GI_NEG INT, HL_negatives INT, listNegEffTerms INT, LIWC_NEG INT, GI_POS INT, HL_positives INT, listPosEffTerms INT, LIWC_POS INT)''')
        # {'EmoSN': 0, 'NRC': 0, 'sentisense': 0, 'afinn': 0, 'anewAro': 0, 'anewDom': 0, 'anewPleas': 0,
        # 'Dal_Activ': 0, 'Dal_Imag': 0, 'Dal_Pleas': 0, 'GI_NEG': 0, 'HL-negatives': 0, 'listNegEffTerms': 0,
        # 'LIWC-NEG': 0, 'GI_POS': 0, 'HL-positives': 0, 'listPosEffTerms': 0, 'LIWC-POS': 0}

        for drop in drops:
            cursor.execute(drop)

        for command in commands:
            cursor.execute(command)

        em_list = ['conScore','Anger','Anticipation','Disgust','Fear','Joy','Sadness','Surprise','Trust']
        total_emo_dict = risorse_lessicali()
        # pprint.pprint(total_emo_dict)

        for q in total_emo_dict:
            print(q)
            # print(total_emo_dict)
            if q in em_list:
                print("sono dentro")
                for k in total_emo_dict[q]:
                    m = []
                    for y in total_emo_dict[q][k]:
                        m.append(total_emo_dict[q][k][y])

                    populate = "INSERT INTO " + q + "(Word, EmoSN, NRC, sentisense, afinn, anewAro, anewDown, anewPleas, Dal_Activ, Dal_Imag, Dal_Pleas, GI_NEG, HL_negatives, listNegEffTerms, LIWC_NEG, GI_POS , HL_positives, listPosEffTerms , LIWC_POS) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    records_to_insert = (k,m[0],m[1],m[2],m[3],m[4],m[5],m[6],m[7],m[8],m[9],m[10],m[11],m[12],m[13],m[14],m[15],m[16],m[17])
                    cursor.execute(populate,records_to_insert)
                    print("INSERTTTTTT")

    finally:
        if conn:
            conn.commit()
            cursor.close()
            conn.close()
            print(colored("[Postgres connection is closed]","red"))
