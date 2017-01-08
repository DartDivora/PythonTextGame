import random, json

with open('files/words.json') as wordsFile:    
    wordsJSON = json.load(wordsFile)
adjectives = wordsJSON["adjectives"].split("|")
rooms = wordsJSON["rooms"].split("|")
print(adjectives)
print(rooms)

def randomWord(words):
    random_word = words[random.randint(0, (len(words) - 1))]
    print(random_word)
    return random_word

print("you enter into a " + randomWord(adjectives) + " " + randomWord(rooms))


