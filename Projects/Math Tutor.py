#import modules
from random import randrange as r
from time import time as t
# ask how many questions user wants
number_questions = int(input('How many questions do you want?'))
max_num = int(input('Highest number used in practice?: '))
#set score start at zero
score = 0
answer_list = []
#loop through number of questions
start = t()
# create two random numbers and calc answer
for q in range(number_questions):
    num1, num2 = r(1,max_num+1), r(1,max_num+1)
    ans = num1*num2
    my_ans = int(input(f'{num1} X {num2} = '))
    answer_list.append(f'{num1} X {num2} = {ans} you:{my_ans}')
    if my_ans == ans:
        score +=1
    end = t()
print(f'Thank you for playing! \nYou got {score} out of {number_questions} { round(score/number_questions*100)}%) correct in {round(end-start, 1)} seconds ({end-start/number_questions, 1}) seconds/question')

for a in answer_list:
    print(a)

# show user the question
# capture answer and modify user score
# output final score 