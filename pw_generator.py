#!/usr/bin/env python3

import secrets

secure_rng = secrets.SystemRandom()

for i in range(6):
    num = ''
    for i in range(5):
        num = num + str(secure_rng.randrange(1, 7))
    print(num)
