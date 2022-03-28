import random
# import quiz_questions
def quiz_generator(quest_ans):
    keys_list = list(quest_ans)
    values_list = list(quest_ans.values())
    quiz_1 = random.sample(keys_list, 5)
    d_quiz_1 = {}
    correct_answers = {}
    for question in quiz_1:
        correct_answer = quest_ans.get(question)
        correct_answers.update({question: correct_answer})
        wrong_answers = random.sample(values_list, 3)
        wrong_answers.append(correct_answer)
        answers = wrong_answers
        random.shuffle(answers)
        d_quiz_1.update({question: answers})
    return d_quiz_1, correct_answers
# capitals=quiz_questions.capitals
# a,b=quiz_generator(capitals)
# print(a)
# print(b)
