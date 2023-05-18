import random
class Question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

    def getprompt(self):
        return self.prompt
    
    def getanswer(self):
        return self.answer

    def addrandomanswer(self):
        self.answer = random.random()

class Quizz:
    id=-1

    def __init__(self,questionlist):
        self.questionlist = questionlist
        self.score = 0

    def addscore(self):
        self.score += 1
        print("Your score is : " + str(self.score))
        return self.score

    def nextquestion(self):
        self.id += 1
        print(self.questionlist[self.id].getprompt())
        return self.questionlist[self.id].getanswer()