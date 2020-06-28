import pymongo
import pprint
from termcolor import colored


def database_mongo(count_freq):

    # Database Connection INFO
    conn_string = "mongodb://localhost:27017/"
    name_db = "Maadb"
    name_collection = "tweet"
    collection_anger = "anger"
    collection_anticipation = "anticipation"
    collection_disgust = "disgust"
    collection_fear = "fear"
    collection_joy = "joy"
    collection_sadness = "sadness"
    collection_surprise = "surprise"
    collection_trust = "trust"

    # Connection
    connection = pymongo.MongoClient(conn_string)
    database = connection[name_db]
    print(colored("[MONGODB CONNECTION at *" + conn_string + "*]", "green"))
    print(colored("[DATABASE *" + name_db + "*]", "green"))


    collection = database[name_collection]
    anger = database[collection_anger]
    anticipation = database[collection_anticipation]
    disgust = database[collection_disgust]
    fear = database[collection_fear]
    joy = database[collection_joy]
    sadness = database[collection_sadness]
    surprise = database[collection_surprise]
    trust = database[collection_trust]

    collection.drop()

    # Insert data
    for w in count_freq:
        tweet = [{"word": w[0],
                  "freq": str(w[1])}]
        collection.insert_many(tweet)

    pprint.pprint(count_freq)

