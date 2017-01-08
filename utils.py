import random, json

debug = True

def debugPrint(text):
    if debug:
        print(str(text))

def randomWord(words):
    random_word = words[random.randint(0, (len(words) - 1))]
    debugPrint(random_word)
    return random_word

def randomDescription():
    description = "you enter into a " + randomWord(adjectives) + " " + randomWord(rooms)
    debugPrint(description)

def Rand_Num_Gen(Min,Max):
    #Generates random number from a range of 2 numbers passed into the function
    Random_Number = random.randint(Min,Max)
    debugPrint(Random_Number)
    return Random_Number        

with open('files/words.json') as wordsFile:    
    wordsJSON = json.load(wordsFile)
adjectives = wordsJSON["adjectives"].split("|")
rooms = wordsJSON["rooms"].split("|")
debugPrint(adjectives)
debugPrint(rooms)





