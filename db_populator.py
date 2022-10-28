#!/usr/bin/env python3

# from pymongo import MongoClient
from mongoengine import *


class Password(Document):
    number = StringField(required=True, unique=True, max_length=5)
    word = StringField(required=True, unique=True, max_length=15)
    def __init__(self, number, word, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.number=number
        self.word=word

# client = MongoClient(host='localhost', port=27017)
client = connect('Passwords', host='localhost', port=27017)

try:  
    with open('dicewaredictionary.txt', 'r') as f:
        for line in f.readlines():
            words = line.split()
            for i in range(0, len(words), 2):
                try: 
                    word = Password(words[i], words[i + 1])
                    word.save()
                except NotUniqueError as err:
                    print("NotUniqueError on word: " + words[i + 1] + " " + "number: " + words[i])
                    f.close()
                    client.close()
                    exit()
                except Exception as e:
                    print(e)
                    f.close()
                    client.close()
                    exit()
    f.close()
except Exception as e:
    print(e)


"""
# Connecting to database with PyMongo client
database = client.test

collection = database.testCollection1

cursor = collection.find()
for record in cursor:
    print(record)
"""

"""
# Working with db through MongoEngine
try:
    word1 = Password('11111', 'a')
    word1.save()
except NotUniqueError as err:
    print("Tried to add non-unique password: ", err)
"""

"""
try: 
    word1 = Password.objects(number='11111', word='a')
    word1.delete()
except Exception as err:
    print("Error: ", err)
"""

client.close()

