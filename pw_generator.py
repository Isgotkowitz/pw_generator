#!/usr/bin/env python3

import secrets
from mongoengine import *

class Password(Document):
    number = StringField(required=True, unique=True, max_length=5)
    word = StringField(required=True, unique=True, max_length=15)
    def __init__(self, number, word, *args, **kwargs):
        super(Document, self).__init__(*args, **kwargs)
        self.number=number
        self.word=word

secure_rng = secrets.SystemRandom()

client = connect('Passwords', host='localhost', port=27017)

new_password = ''
for i in range(6):
    num = ''
    for i in range(5):
        num = num + str(secure_rng.randrange(1, 7))
    try:
        queryset = Password.objects
        for words in queryset.filter(number=num):
            new_password = new_password + words.word
        if i < 5:
            new_password = new_password + " "
    except Exception as e:
        print("Error: ", e)
        exit()

print("Your newest password: " + new_password)

client.close()
