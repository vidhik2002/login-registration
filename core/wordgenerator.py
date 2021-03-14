import random

count = 0
miss = 0
WORDS = ('north', 'sound', 'west', 'east')
word = random.choice(WORDS)

typed_word = input()

while word:
    if word == typed_word:
        count += 1
    elif word != typed_word or word == "":
        miss += 1



