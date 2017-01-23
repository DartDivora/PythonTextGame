def askQuestion(question, answer):
    result = input(question).strip().lower()
    if result == answer.strip().lower():
        return True
    else:
        return False



#example, feel free to delete
print(str(askQuestion("Please say hello: ","hello")))

