#!/usr/bin/env python3

from mongoengine import *


class Password(Document):
    number = StringField(required=True, unique=True, max_length=5)
    word = StringField(required=True, unique=True, max_length=15)
    def __init__(self, number, word, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.number=number
        self.word=word

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

client.close()

