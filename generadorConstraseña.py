import random

abcdario='abcdefghijklmnñopqrstuvwxyz'

print(str(random.randrange(10))+random.choice(str.upper(abcdario))+str(random.randrange(10))+str(random.randrange(10))+random.choice(abcdario)+str(random.randrange(10))+random.choice(abcdario)+random.choice(abcdario)+random.choice(str.upper(abcdario))+random.choice(str.upper(abcdario))+random.choice(str.upper(abcdario)))