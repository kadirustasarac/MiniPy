import random


class Question():

    allQuestions = []
    rightindex = 0
    def __init__(self,question,correctAnswer,wrongAnswer = []):
        self.question = question
        self.correctAnswer = correctAnswer
        self.allQuestionsNS = wrongAnswer
        self.allQuestionsNS.append(correctAnswer) 
        self.num = len(self.allQuestionsNS)

    
    def SetAnswers(self):
        listOfNum = []
        for a in range(0,self.num):
            while True:
                rnd = random.randrange(0,self.num)
                if(rnd not in listOfNum):
                    listOfNum.append(rnd)
                    self.allQuestions.append(self.allQuestionsNS[rnd])
                    if(rnd == len(self.allQuestionsNS)-1):
                        self.rightindex = len(self.allQuestions)-1
                    break
            

    def AskQuestion(self):
        
        print(self.question)
        for a in range(0,self.num):
            print("{}- {} ".format(a,self.allQuestions[a]))
        
        answer = input()
        if(answer == str(self.rightindex)):
            print("Nice amigo")
        else:
            print("Wrong")

        # print(self.allQuestions,self.allQuestionsNS)

num1 = Question("Have you ever had gay thoughts ?","Yes",["No eww","I am heterosexual(lies)","ur mum(kys)"])
num1.SetAnswers()
num1.AskQuestion()

