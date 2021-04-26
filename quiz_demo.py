# question 

class Question:
    def __init__(self, text, choices, answer):
        self.text= text
        self.choices= choices
        self.answer= answer

    def Checkanswer(self, answer):
        return self.answer == answer    

"""
print(q1.Checkanswer("python"))
print(q2.Checkanswer("python"))
print(q3.Checkanswer("python"))"""


#Quiz
class Quiz:
    def __init__(self, question):
        self.question=question
        self.score=0
        self.questionIndex = 0

    def getQuestions(self):
        return self.question[self.questionIndex] 

    def  displayQuestions(self):
        question=self.getQuestions()
        print(f"soru {self.questionIndex+1}: {question.text} ")

        for q in question.choices:
            print("-" + q )

        answer= input("cevap: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestions()

        if  question.Checkanswer(answer): 
            self.score+=1
        self.questionIndex+= 1   
        
    def loadQuestion(self):
        if len(self.question)== self.questionIndex:
            self.showScore()
        else :
            self.displayProgress()
            self.displayQuestions()     
    
    def showScore(self):
        print("score: " , self.score)

    def displayProgress(self):
        totalQuestion=len(self.question)
        questionnumber=self.questionIndex+1

        if questionnumber > totalQuestion:
            print(" quiz bitti.")
        else :
            print (f"Question {questionnumber}  of {totalQuestion} ".center(100,"*"))    




q1=Question("en iyi programlama dili hangisidir?",["c#", "python","javascript", "java" ],"python")
q2=Question("en popüler programlama dili hangisidir?",["c#", "python","javascript", "java" ],"python")
q3=Question("en çok kazandıranprogramlama dili hangisidir?",["c#", "python","javascript", "java" ],"python")
question = [ q1, q2, q3]

quiz =Quiz(question)

quiz.loadQuestion()