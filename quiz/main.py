import html
from urllib.request import urlopen
import json
import random

url = 'https://opentdb.com/api.php?amount=1000&type=multiple'
response = urlopen(url)
data_json = json.loads(response.read())

questions = 10
score = 0
questionNumbers = {}
answers = {}
userAnswer = 'q'

questions = int(input("How many questions do you want to answer: "))

for i in range(questions):
    answers[i] = {"A": "", "B": "", "C": "", "D": ""}

for i in range(questions):
    questionNumbers[i] = random.randint(0, 49)

for i in questionNumbers:
    if (data_json["results"][questionNumbers[i]]["type"] == "multiple"):
        incorrectAnswers = html.unescape(data_json["results"][questionNumbers[i]]["incorrect_answers"])
        incorrectAnswers.append(html.unescape(data_json["results"][questionNumbers[i]]["correct_answer"]))

        random.shuffle(incorrectAnswers)

        answers[i]["A"] = html.unescape(incorrectAnswers[0])
        answers[i]["B"] = html.unescape(incorrectAnswers[1])
        answers[i]["C"] = html.unescape(incorrectAnswers[2])
        answers[i]["D"] = html.unescape(incorrectAnswers[3])

for i in questionNumbers:
    print("---- Question", i+1, "----")
    print("Category:\n", html.unescape(data_json["results"][questionNumbers[i]]['category']))
    print("Difficulty:\n", html.unescape(data_json["results"][questionNumbers[i]]['difficulty']))
    print("Question:\n", html.unescape(data_json["results"][questionNumbers[i]]['question']))
    for j in range(4):
        print(list(answers[i].keys())[j], "-", list(answers[i].values())[j])

    userAnswer = input("Your answer: ")
    userAnswer = userAnswer.upper()

    if (userAnswer.upper() not in ('A', 'B', 'C', 'D')):
        while (userAnswer.upper() not in ('A', 'B', 'C', 'D')):
            userAnswer = input("Answer a, b, c or d. Your answer: ")
            userAnswer = userAnswer.upper()

    if (answers[i][userAnswer] == data_json["results"][questionNumbers[i]]['correct_answer']):
        score+=1
        print("Correct answer!!!")
    else:
        print("Incorect answer :(")
        print("The correct answer was", html.unescape(data_json["results"][questionNumbers[i]]['correct_answer']))

print("---- End of the game ----")
print("Your score was " + str(score) + "/" + str(questions))









