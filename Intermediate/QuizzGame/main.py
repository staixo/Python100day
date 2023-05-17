import random
class Question:
    def __init__(self, prompt, answer):
        print("Question is : " + prompt)
        self.prompt = prompt
        self.answer = answer
    def addrandomanswer(self):
        self.answer = random.random()

question=Question("Comment je m'appelle ?","Henri")
print(question.answer)
question.addrandomanswer()
print(question.answer)