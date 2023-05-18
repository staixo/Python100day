
import data
import quizzclass

questionlist = []
for question in data.question_data:
    questionlist.append(quizzclass.Question(question["text"],question["answer"]))

quizz = quizzclass.Quizz(questionlist)


play = True
while play:
    answer = quizz.nextquestion() 
    myanswer =""
    while myanswer != "True" and myanswer != "False":
        myanswer = input("Your answer is : ")
    if myanswer == answer:
        print(answer)
        quizz.addscore()
    else:
        play = False
