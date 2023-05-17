import random
import data
class Question:
    def __init__(self, prompt, answer):
        print("Question is : " + prompt)
        self.prompt = prompt
        self.answer = answer
    def addrandomanswer(self):
        self.answer = random.random()

class quizz:
    def __init__(self,questionlist):
        self.questionlist = questionlist
        self.score = 0
    def nextquestion(self):
        id = int(random.uniform(0,len(data.question_data)))
        self.questionlist.append=Question(question["text"],question["answer"])

questionlist = []
for question in data.question_data:
    questionlist.append=Question(question["text"],question["answer"])


    

play = True
while play:
    id = int(random.uniform(0,len(data.question_data)))
    
    myanswer =""
    while myanswer != "True" and myanswer != "False":
        myanswer = input("Your answer is : ")
    if myanswer == question.answer:
        print(question.answer)
    else:
        play = False
