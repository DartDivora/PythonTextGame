import random, json

debug = False

def debugPrint(text):
    if debug:
        print(str(text))

def randomWord(words):
    random_word = words[random.randint(0, (len(words) - 1))]
    debugPrint(random_word)
    return random_word

def randomDescription():
    description = "You enter into a " + randomWord(adjectives) + " " + randomWord(rooms) + "."
    debugPrint(description)
    return description

def rand_num_gen(Min,Max):
    #Generates random number from a range of 2 numbers passed into the function
    random_number = random.randint(Min,Max)
    debugPrint(random_number)
    return random_number        

with open('files/words.json') as wordsFile:    
    wordsJSON = json.load(wordsFile)
adjectives = wordsJSON["adjectives"].split("|")
rooms = wordsJSON["rooms"].split("|")
debugPrint(adjectives)
debugPrint(rooms)




427/350

